import os
import sys
from time import sleep
from traceback import format_exc
from importlib import import_module, reload
from pysettings.text import MsgText, TextColor
from pysettings import tk
from PyOverlay.src.constants import STYLE_GROUP as SG
from threading import Thread

RUNNING_AS_COMPILED = False
if getattr(sys, 'frozen', False):  # Running as compiled
    RUNNING_AS_COMPILED = True
    BASE_PATH = os.path.join(os.path.expanduser("~"), "Documents", "PyOverlayPlugins") #C:\Users\langh\AppData\Local\Programs\Python\Python310\Lib\PyOverlay\src
    if not os.path.exists(BASE_PATH):
        os.mkdir(BASE_PATH)
    if not os.path.exists(os.path.join(BASE_PATH, "plugins")):
        os.mkdir(os.path.join(BASE_PATH, "plugins"))
    os.chdir(os.path.join(BASE_PATH, "plugins"))

else:
    BASE_PATH = os.getcwd()

class PluginManagerGUI(tk.Dialog):
    _OPEN = False
    def __init__(self, master):
        PluginManagerGUI._OPEN = True
        super().__init__(master, SG, False)

        self.setWindowSize(600, 450)
        self.setPositionOnScreen(350, 275)
        self.setResizeable(False)
        self.setTitle("Plugin Manager GUI")
        self.onCloseEvent(self._onCloseEvent)
        self.bind(self.close, tk.EventType.ESC)
        self.waiting = True
        self.openTextGUIs = []
        self.changedTextGUIs = []

        self.pluginFrame = tk.LabelFrame(self, SG).place(400, 0, 200, 150).setText("Selected Plugin")
        self.l_name = tk.Label(self.pluginFrame, SG).setText("Name: ").place(0, 0, 200, 25).setTextOrientation(tk.Anchor.LEFT)
        self.l_version = tk.Label(self.pluginFrame, SG).setText("Version: ").place(0, 20, 200, 25).setTextOrientation(tk.Anchor.LEFT)
        self.l_prio = tk.Label(self.pluginFrame, SG).setText("Priority: ").place(0, 40, 200, 25).setTextOrientation(tk.Anchor.LEFT)
        self.l_state = tk.Label(self.pluginFrame, SG).setText("State: ").place(0, 60, 200, 25).setTextOrientation(tk.Anchor.LEFT)

        legend = tk.LabelFrame(self, SG).setText("Legend").place(200, 150, 200, 150)

        tk.Label(legend, SG).place(10, 10, 10, 10).setBg("green")
        tk.Label(legend, SG).place(20, 5, 170, 16).setText(" = Running").setTextOrientation(tk.Anchor.LEFT)

        tk.Label(legend, SG).place(10, 10+15, 10, 10).setBg("red")
        tk.Label(legend, SG).place(20, 5+15, 170, 16).setText(" = Stopped (during runtime)").setTextOrientation(tk.Anchor.LEFT)

        tk.Label(legend, SG).place(10, 10+15*2, 10, 10).setBg("gray")
        tk.Label(legend, SG).place(20, 5+15*2, 170, 16).setText(" = Disabled (not started)").setTextOrientation(tk.Anchor.LEFT)

        tk.Label(legend, SG).place(10, 10+15*3, 10, 10).setBg("purple")
        tk.Label(legend, SG).place(20, 5+15*3, 170, 16).setText(" = Error").setTextOrientation(tk.Anchor.LEFT)

        control = tk.LabelFrame(self, SG).setText("Control").place(400, 150, 200, 150)
        self._disable = tk.Button(control, SG).setText("Disable").placeRelative(fixY=0, fixHeight=25, changeWidth=-5).setFg("red").setCommand(self.disenable)
        self._reload = tk.Button(control, SG).setText("Reload").placeRelative(fixY=25, fixHeight=25, changeWidth=-5).setCommand(self.reloadSelected)
        tk.Button(control, SG).setText("Disable all").placeRelative(fixY=50, fixHeight=25, changeWidth=-5).setCommand(self._disableAll)
        tk.Button(control, SG).setText("Enable all").placeRelative(fixY=75, fixHeight=25, changeWidth=-5).setCommand(self._enableAll)
        tk.Button(control, SG).setText("Reload all").placeRelative(fixY=100, fixHeight=25, changeWidth=-5).setCommand(self.reloadAll)

        console = tk.LabelFrame(self, SG).place(0, 300, 400, 150).setText("Console")
        self.console = tk.Text(console, SG, scrollAble=True, readOnly=True).placeRelative(changeWidth=-5, changeHeight=-20).setWrapping(tk.Wrap.NONE)

        desc = tk.LabelFrame(self, SG).setText("Description").place(400, 300, 200, 150)
        self.desc = tk.Text(desc, SG, readOnly=True, scrollAble=True).placeRelative(changeWidth=-5, changeHeight=-20).setStyle(tk.Style.FLAT).setWrapping(tk.Wrap.WORD)

        pl_list = tk.LabelFrame(self, SG).setText("Plugin list").place(0, 0, 200, 300)
        self.lis = tk.Listbox(pl_list, SG).placeRelative(changeWidth=-5, changeHeight=-20)
        self.lis.onSelectEvent(self.onListBoxSelect)
        self.lis.bind(self.onListBoxDoubleSelect, tk.EventType.DOUBBLE_LEFT)

        info = tk.LabelFrame(self, SG).place(200, 0, 200, 150).setText("Info")
        self._count = tk.Label(info, SG).setTextOrientation(tk.Anchor.LEFT).place(0, 0, 100, 25)
        self._runs = tk.Label(info, SG).setTextOrientation(tk.Anchor.LEFT).place(0, 20, 100, 25)
        self._sto = tk.Label(info, SG).setTextOrientation(tk.Anchor.LEFT).place(0, 40, 100, 25)
        self._disa = tk.Label(info, SG).setTextOrientation(tk.Anchor.LEFT).place(0, 60, 100, 25)
        self._errs = tk.Label(info, SG).setTextOrientation(tk.Anchor.LEFT).place(0, 60, 100, 25)



        self.indexPlugins()
        Thread(target=self._waitForEditorClose).start()
        self.show()
    def indexPlugins(self, sel=None):
        disa = 0
        active = 0
        inactive = 0
        err = 0

        self.lis.clear()
        for i, data in enumerate(PluginManager.PLUGIN_DATA):
            color = "green" if data["state"] == "active" else "red"
            color = "gray" if data["state"] == "disabled" else color
            color = "purple" if data["state"] == "error" else color
            if color == "green":
                active += 1
            elif color == "red":
                inactive += 1
            elif color == "gray":
                disa += 1
            elif color == "purple":
                err += 1

            self.lis.add(data["name"], color=color)
        if sel is not None: self.lis.setItemSelectedByName(sel)

        self._count.setText(f"Plugin count: {len(PluginManager.PLUGIN_DATA)}")
        self._runs.setText(f"Plugins running: {active}")
        self._sto.setText(f"Plugins stopped: {inactive}")
        self._disa.setText(f"Plugins disabled: {disa}")
        self._errs.setText(f"Errors: {err}")
    def onListBoxSelect(self, e):
        if isinstance(e, tk.Event):
            sel = self.lis.getSelectedItem()
            if sel is not None:
                data = PluginManager.PLUGIN_DATA_DICT[sel]
            else: return
        else: data = e

        self.l_name.setText("Name: "+data["name"])
        self.l_version.setText("Version: "+str(data["version"]))
        self.l_prio.setText("Priority: "+str(data["priority"]))

        self._disable.setEnabled()
        self._reload.setEnabled()
        if data["state"] == "active":
            self._disable.setText("Disable").setFg("red")
            color = "green"
            state = "running"
        elif data["state"] == "inactive":
            self._disable.setText("Enable").setFg("green")
            color = "red"
            state = "stopped"
        elif data["state"] == "disabled":
            self._disable.setText("Plugin Disabled in File!").setFg("black")
            self._disable.setDisabled()
            self._reload.setDisabled()
            color = "gray"
            state = "disabled"
        elif data["state"] == "error":
            self._disable.setText("Error! Reload to activate!").setFg("black")
            self._disable.setDisabled()
            color = "purple"
            state = "error"
        else:
            raise Exception("Unknown state: "+str(data["state"]))

        self.l_state.setText("State: "+state).setBg(color)
        self.desc.clear()
        self.desc.addText(str(data["description"]))

        self.console.clear()
        self.console.addText(str(data["console"]))
    def _waitForEditorClose(self):
        while True:
            sleep(.1)
            for text in self.openTextGUIs:
                if not text.saved and text not in self.changedTextGUIs:
                    self.changedTextGUIs.append(text)
                if text.closed:
                    if text in self.changedTextGUIs:
                        pluginName = os.path.splitext(os.path.split(text.currPath)[1])[0]
                        if tk.SimpleDialog.askOkayCancel(self, f"Plugin '{pluginName}' changed. Do you want to reload the plugin?"):
                            data = self.reload(PluginManager.PLUGIN_DATA_DICT[pluginName])
                            self.onListBoxSelect(data)
                            self.indexPlugins()
                            if data["state"] == "active": tk.SimpleDialog.askInfo(PluginManager.WINDOW,f"Plugins reloaded successfully!\n-{data['name']}")
                            self.lift()
                        self.changedTextGUIs.remove(text)
                    self.openTextGUIs.remove(text)
    def onListBoxDoubleSelect(self, e):
        sel = self.lis.getSelectedItem()
        if sel is not None:
            data = PluginManager.PLUGIN_DATA_DICT[sel]
            if "textEditorPlugin" in PluginManager.PLUGIN_DATA_DICT.keys():
                dataText = PluginManager.PLUGIN_DATA_DICT["textEditorPlugin"]
                if dataText["state"] == "active":
                    _gui = dataText["plugin"]._getPluginClass().openGUI(data.getRealPath())
                    self.waiting = True
                    self.openTextGUIs.append(_gui)
                else:
                    tk.SimpleDialog.askError(self, f"Plugin 'textEditorPlugin' has state {dataText['state']} \nenable is first to view other plugin's code!")
            else:
                tk.SimpleDialog.askError(self, f"Plugin 'textEditorPlugin' is not installed!\ You cannot view the plugin's code!")
    def disenable(self):
        sel = self.lis.getSelectedItem()
        if sel is not None:
            data = PluginManager.PLUGIN_DATA_DICT[sel]
            if data["state"] == "active":
                self.disablePlugin(data)
                self.indexPlugins()

            elif data["state"] == "inactive":
                self.enablePlugin(data)
                self.indexPlugins()

            self.lis.setItemSelectedByName(data["name"])
            self.onListBoxSelect(data)
    def _disableAll(self):
        PluginManagerGUI.disableAll()
        self.indexPlugins()
    @staticmethod
    def disableAll():
        disab = []
        cdisab = []
        for data in PluginManager.PLUGIN_DATA:
            if data["state"] == "active":
                disab.append(data)
            else:
                cdisab.append(data)
        out = tk.SimpleDialog.askOkayCancel(PluginManager.WINDOW, "Plugins to disable:\n -"+"\n -".join([i['name'] for i in disab])+"\nPlugins cant be disabled:\n -"+"\n -".join([i['name']+f"({i['state']})" for i in cdisab]))
        if not out: return
        for i in disab:
            PluginManagerGUI.disablePlugin(i)
    def _enableAll(self):
        PluginManagerGUI.enableAll()
        self.indexPlugins()
    @staticmethod
    def enableAll():
        disab = []
        cdisab = []
        for data in PluginManager.PLUGIN_DATA:
            if data["state"] == "inactive":
                disab.append(data)
            else:
                cdisab.append(data)
        out = tk.SimpleDialog.askOkayCancel(PluginManager.WINDOW, "Plugins to enable:\n -" + "\n -".join([i['name'] for i in disab]) + "\nPlugins cant be enabled:\n -" + "\n -".join([i['name'] + f"({i['state']})" for i in cdisab]))
        if not out: return
        for i in disab:
            PluginManagerGUI.enablePlugin(i)
    def reloadAll(self):
        pass
    def reloadSelected(self):
        sel = self.lis.getSelectedItem()
        if sel is not None:
            print(sel)
            data = PluginManager.PLUGIN_DATA_DICT[sel]
            self._reload.setText("Reloading...").setDisabled()
            print(data.data)
            data = self.reload(data)
            self._reload.setText("Reload").setEnabled()
            self.onListBoxSelect(data)
            self.indexPlugins()
            print(data.data)
            if data["state"] == "active": tk.SimpleDialog.askInfo(PluginManager.WINDOW, f"Plugins reloaded successfully!\n-{data['name']}")
            self.lift()
    @staticmethod
    def disablePlugin(data):
        data["state"] = "inactive"
    @staticmethod
    def enablePlugin(data):
        data["state"] = "active"
    def reload(self, data):
        def onErr():
            exc = format_exc()
            tk.SimpleDialog.askError(PluginManager.WINDOW, exc, "Plugin-Loader-Exception")
            TextColor.printStrf("§r" + exc)
            TextColor.printStrf("§ERRORCould not execute Plugin! (§c" + data["name"] + "§r)")
            data["console"] += "\n====================================\n" + exc
            self.console.setText(data["console"])
        if data["module"] is None:
            try:
                module = import_module(data["path"])
            except:
                onErr()
                return
        else:
            try:
                module = reload(data["module"])
            except:
                onErr()
                return
        pluginName = data["name"]

        instance = module.Plugin._INSTANCE
        #PluginManager.PLUGIN_DATA.remove(data)

        data.data = {
            "name":pluginName,  # name of the Plugin
            "version":module.VERSION if hasattr(module, "VERSION") else None,
            "description":module.DESCRIPTION if hasattr(module, "DESCRIPTION") else "Has no Description!",
            "path":"PyExplorer.src.plugins." + pluginName,
            "module":module,  # module instance from import
            "plugin":instance,  # plugin instance from class:
            "priority":instance.priority,
            "state":"disabled" if instance._disabled else "active",  # active, inactive, disabled, error
            "console":"",
        }
        instance._pluginName = pluginName
        instance._getStateHook = PluginManager._getState
        instance._window = PluginManager.WINDOW
        #data = PluginManager.PLUGIN_DATA[-1]
        PluginManager.PLUGIN_DATA_DICT[data["name"]] = data
        if data["state"] == "active":
            instance._run()
        nameLen = len(module.__name__)
        state = data["state"]
        if state == "active":
            instance._run()  # run the Plugin
            TextColor.printStrf("§INFO   -Plugin successfully reloaded!   (§c" + module.__name__ + "§g)" + "-" * (50 - nameLen + 2) + "§g-> §gENABLED")
        elif state == "disabled":
            TextColor.printStrf("§INFO   -Plugin successfully reloaded!   (§c" + module.__name__ + "§g)" + "-" * (50 - nameLen + 2) + "§g-> §rDISABLED")
        else:
            TextColor.printStrf("§INFO   -Plugin successfully reloaded!   (§c" + module.__name__ + "§g)" + "-" * (50 - nameLen))
        return data
    def close(self):
        self._onCloseEvent()
        self.destroy()
    def _onCloseEvent(self, e=""):
        self.waiting = False
        sleep(.2)
        PluginManagerGUI._OPEN = False
class PluginData:
    def __init__(self, name, version, desc, path, module, plugin, priority, state="active", console=""):
        self.data = {
        "name":name,       # name of the Plugin
        "version":version,
        "description":desc,
        "path":path,
        "module":module,   # module instance from import
        "plugin":plugin,   # plugin instance from class
        "priority":priority,
        "state":state,  # active, inactive, disabled, error
        "console":console,
    }
    def __getitem__(self, key):
        return self.data[key]
    def __setitem__(self, key, value):
        self.data[key] = value
    def __lt__(self, other):
        return self["priority"] < other["priority"]
    def getRealPath(self):
        return os.path.join(os.path.split(os.path.split(BASE_PATH)[0])[0], *self["path"].split("."))+".py"
class PluginManager:
    PLUGIN_DATA:[PluginData] = [] # in correct priority order!
    PLUGIN_DATA_DICT = {}         # to fast access from name
    WINDOW = None
    @staticmethod
    def _getState(name):
        return PluginManager.PLUGIN_DATA_DICT[name]["state"]
    @staticmethod
    def call(eventName, **kwargs):
        """

        @param eventName:
        @param kwargs:
        @return: False -> no cancel, True one or more cancels!
        """
        canc = []
        event = None
        for data in PluginManager.PLUGIN_DATA:
            if event is not None and event["cancelOther"]: break
            if not data["state"] == "active": continue
            try:
                event = data["plugin"]._call(eventName, **kwargs)
            except Exception as e:
                exc = format_exc()
                data["console"] += "\n"+exc
                TextColor.print(exc, "red")
                tk.SimpleDialog.askError(PluginManager.WINDOW, f"An error occurred while executing event '<{eventName}>' in Plugin '{data['name']}'.\nCheck the console in the PluginManager for more information.", "PluginManager gui")
                data["state"] = "error"
            if event is not None: canc.append(event["setCanceled"])
        return any(canc)
    @staticmethod
    def _getPlugins(path):
        for pluginName in os.listdir(path):
            if os.path.splitext(pluginName)[1] != ".py": continue
            pluginName = pluginName.replace(".py", "")
            if pluginName.startswith("__"): continue
            yield pluginName
    @staticmethod
    def _loadPluginFromName(pluginName):
        try:
            module = import_module("PyOverlay.src.plugins." + pluginName
                                   if not RUNNING_AS_COMPILED else
                                   pluginName)
            if hasattr(module, "Plugin") and module.Plugin._INSTANCE is not None:

                instance = module.Plugin._INSTANCE
                pl_data = PluginData(
                    name=pluginName,
                    version=module.VERSION if hasattr(module, "VERSION") else None,
                    desc=module.DESCRIPTION if hasattr(module, "DESCRIPTION") else "Has no Description!",
                    path="PyOverlay.src.plugins." + pluginName,
                    module=module,
                    plugin=instance,
                    priority=instance.priority,
                    state="disabled" if instance._disabled else "active",
                )
                PluginManager.PLUGIN_DATA.append(pl_data)
                PluginManager.PLUGIN_DATA_DICT[pluginName] = pl_data
                instance._pluginName = pluginName
                instance._getStateHook = PluginManager._getState
                instance._window = PluginManager.WINDOW
                if instance._disabledInDev and PluginManager.WINDOW.devMode:
                    pl_data["state"] = "disabled"
                #t.sleep(0.2)
                state = PluginManager.PLUGIN_DATA[-1]["state"]
                nameLen = len(module.__name__)
                if state == "active":
                    instance._run()  # run the Plugin
                    TextColor.printStrf(
                        "§INFO   -Plugin successfully registered! (§c" + module.__name__ + "§g)" + "-" * (
                                    50 - nameLen + 2) + "§g-> §gENABLED")
                elif state == "disabled":
                    TextColor.printStrf(
                        "§INFO   -Plugin successfully registered! (§c" + module.__name__ + "§g)" + "-" * (
                                    50 - nameLen + 2) + "§g-> §rDISABLED")
                else:
                    TextColor.printStrf(
                        "§INFO   -Plugin successfully registered! (§c" + module.__name__ + "§g)" + "-" * (50 - nameLen))
            else:
                pl_data = PluginData(
                    name=pluginName,
                    version=None,
                    desc="",
                    path="PyOverlay.src.plugins." + pluginName,
                    module=None,
                    plugin=None,
                    priority=1000,
                    state="error",
                    console="Could not register Plugin: Plugin class not available!"
                )
                PluginManager.PLUGIN_DATA.append(pl_data)
                PluginManager.PLUGIN_DATA_DICT[pluginName] = pl_data
                TextColor.printStrf(
                    "§ERROR§rCould not register Plugin: Plugin class not available! (§c" + module.__name__ + "§r)")

        except Exception as e:
            exc = format_exc()
            pl_data = PluginData(
                name=pluginName,
                version=None,
                desc="",
                path="PyOverlay.src.plugins." + pluginName,
                module=None,
                plugin=None,
                priority=1000,
                state="error",
                console=str(exc)
            )
            PluginManager.PLUGIN_DATA.append(pl_data)
            PluginManager.PLUGIN_DATA_DICT[pluginName] = pl_data
            TextColor.printStrf("§r" + exc)
            TextColor.printStrf("§ERRORCould not execute Plugin! (§c" + pluginName + "§r)")
            tk.SimpleDialog.askError(PluginManager.WINDOW, exc, "Plugin-Loader-Exception")
    @staticmethod
    def loadPlugins(loadingFrame):
        pluginNames = [i for i in PluginManager._getPlugins(os.path.join(BASE_PATH, "plugins"))]
        """
        master = tk.Dialog(window)
        master.setTopmost(True)
        master.setTitle("Plugin loader")
        master.setCloseable(False)
        master.setWindowSize(350, 100)
        """
        pg = tk.Progressbar(loadingFrame)
        pg.placeRelative(fixHeight=30, changeX=+15, changeWidth=-30, stickDown=True, changeY=-75)
        lb = tk.Label(loadingFrame, SG).setText(f"Loading Plugins... (0/{len(pluginNames)}) 0%").setFont(15)
        lb.placeRelative(fixHeight=25, changeX=+15, changeWidth=-30, stickDown=True, changeY=-175)
        lb2 = tk.Label(loadingFrame, SG).setText("-textEditorPlugin").setFont(15)
        lb2.placeRelative(fixHeight=25, changeX=+15, changeWidth=-30, stickDown=True, changeY=-125)
        MsgText.info(f"Loading plugins... ({len(pluginNames)})")
        for i, pluginName in enumerate(pluginNames):
            PluginManager._loadPluginFromName(pluginName)
            lb.setText(f"Loading Plugins... ({i}/{len(pluginNames)}) {round((i / len(pluginNames)) * 100, 1)}%")
            lb2.setText(f"Plugin: {pluginName}")
            pg.setPercentage((i / len(pluginNames)) * 100)
            PluginManager.WINDOW.update()
        pg.setPercentage(100)
        lb.setText(f"Finishing up... 100%")
        lb2.setText("Building gui...")
        #t.sleep(.5)
        PluginManager.PLUGIN_DATA.sort()
        PluginManager.PLUGIN_DATA.reverse()
    @staticmethod
    def openGUI(e=""):
        if not PluginManagerGUI._OPEN:
            gui = PluginManagerGUI(PluginManager.WINDOW)

