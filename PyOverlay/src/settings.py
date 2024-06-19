from traceback import format_exc
from pysettings import tk
from PyOverlay.src.configLoader import Config
from PyOverlay.src.constants import STYLE_GROUP as SG
from PyOverlay.src.pluginManager import PluginManager, PluginData

class SettingsGUI(tk.Dialog):
    _OPEN = False
    def __init__(self, master):
        SettingsGUI._OPEN = True
        super().__init__(master, SG, topMost=False)
        self.window = master
        self.setTitle("Settings")
        self.setResizeable(False)
        self.setWindowSize(600, 400)
        self.setPositionOnScreen(350, 275)
        self.config = Config.SETTINGS_CONFIG
        self.menu = tk.Notebook(self)
        #Frame height: 375
        self.frame_general = self.menu.createNewTab("General", SG)
        self.frame_advanced = self.menu.createNewTab("Advanced", SG)
        self.frame_plugins = self.menu.createNewTab("Plugins", SG)

        self.menu.placeRelative()
        self.onCloseEvent(self.onCloseEvent_)
        self.bind(self.close, tk.EventType.ESC)

        self.create_General(self.frame_general)
        self.create_Advanced(self.frame_advanced)
        self.create_Plugins(self.frame_plugins)
        self.show()
    def create_General(self, frame):
        def update():
            Config.SETTINGS_CONFIG["is_menu_movable"] = isMenuMovable.getState()
            Config.SETTINGS_CONFIG["is_menu_minimized_on_start"] = isMenuMinimizedOnStart.getState()
            Config.SETTINGS_CONFIG["square_size"] = int(squareSize.getValue())


            Settings.WINDOW.updateSquareSize()

            Config.SETTINGS_CONFIG.save()

        squareOptions = tk.LabelFrame(frame, SG).setText("Square Options").place(0, 0, 200, 200)

        isMenuMovable = tk.Checkbutton(squareOptions, SG)
        isMenuMovable.setState(Config.SETTINGS_CONFIG.get("is_menu_movable", True))
        isMenuMovable.setText("is Menu Movable")
        isMenuMovable.onSelectEvent(update)
        isMenuMovable.placeRelative(fixHeight=25, changeWidth=-5)

        isMenuMinimizedOnStart = tk.Checkbutton(squareOptions, SG)
        isMenuMinimizedOnStart.setState(Config.SETTINGS_CONFIG.get("is_menu_minimized_on_start", True))
        isMenuMinimizedOnStart.setText("is Menu Minimized on Start")
        isMenuMinimizedOnStart.onSelectEvent(update)
        isMenuMinimizedOnStart.placeRelative(fixHeight=25, changeWidth=-5, fixY=25)

        squareSize = tk.Scale(squareOptions, SG, from_=10, to=50)
        squareSize.onScroll(update)
        squareSize.setText("Square Size")
        squareSize.setValue(Config.SETTINGS_CONFIG.get("square_size", 10))
        squareSize.placeRelative(fixHeight=75, changeWidth=-5, fixY=50)
    def create_Advanced(self, frame):
        pass
    def create_Plugins(self, frame):
        plSelect = tk.LabelFrame(frame, SG).setText("Plugins").place(0, 0, 150, 375)
        self.pluginList = tk.Listbox(plSelect, SG).placeRelative(changeWidth=-5, changeHeight=-50)
        self.pluginList.onSelectEvent(self.onPluginSelect)
        self.nameToData = {}
        for data in PluginManager.PLUGIN_DATA:
            self.pluginList.add(data["name"])
            self.nameToData[data["name"]] = data
        self.pluginList.setItemSelectedByIndex(0)

        def _openPMgr():
            cancel = self.close()
            if not cancel: PluginManager.openGUI()


        tk.Button(plSelect, SG).setText("Open Plugin Manager").place(0, 328, 145, 25).setCommand(_openPMgr)

        self.pluginSettings = tk.LabelFrame(frame, SG).setText("Plugin Settings").place(150, 0, 445, 375)
        # plugin frame size: 440 355
        self.activePluginFrame = None
        self.onPluginSelect()
    def onPluginSelect(self, e=""):
        sel = self.pluginList.getSelectedItem()
        if sel is not None:
            if self.activePluginFrame is not None:
                self.activePluginFrame.destroy()
                self.activePluginFrame = None

            data = self.nameToData[sel]
            blankFrame = tk.Frame(self.pluginSettings, SG)
            try:
                constructedFrame = data["plugin"]._constructPluginSettings(blankFrame)
            except:
                exc = format_exc()
                tk.SimpleDialog.askError(Settings.WINDOW, "The Settings Frame could not be built.\nCheck the error log on the Frame.", f"Plugin Settings Exception ({data['name']})")
                constructedFrame = tk.Frame(self.pluginSettings, SG)
                tk.Text(constructedFrame, SG, scrollAble=True).setText(exc).setWrapping(tk.Wrap.NONE).place(0, 0, 440, 355)


            self.activePluginFrame:tk.Frame = constructedFrame.placeRelative(changeHeight=-20, changeWidth=-5)
            if len(self.activePluginFrame._getAllChildWidgets()) == 0:
                tk.Label(self.activePluginFrame, SG).setText("This Plugin has no settings!").placeRelative()
    def close(self):
        cancel = self.onCloseEvent_("", True)
        if not cancel: self.destroy()
        return cancel
    def onCloseEvent_(self, e, force=False):
        cancel = PluginManager.call("onSettingsCloseEvent")
        if not force: e.setCanceled(cancel)
        SettingsGUI._OPEN = False
        return cancel


class Settings:
    WINDOW = None
    @staticmethod
    def openGUI():
        if not SettingsGUI._OPEN:
            gui = SettingsGUI(Settings.WINDOW)