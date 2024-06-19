import os
from PyOverlay.src.constants import STYLE_GROUP as SG, Color
from PyOverlay.src.plugins import Plugin, EventHandler
from pysettings import tk, iterDict
from pysettings.jsonConfig import JsonConfig
from pyperclip import copy

# name : (clazz, enabled:bool)
REGISTER = {}

def register(name:str, enabled=True):
    def _wrapper(clazz):
        REGISTER[name] = (clazz, enabled)
        return clazz
    return _wrapper
class OneClickSelector(tk.ContextMenu):
    def __init__(self, optionList:list, loc=tk.Location2D(350, 275)):
        super().__init__(plugin.getWindow(), SG, eventType=None)
        self.loc = loc
        self.cmd = None
        for option in optionList:
            tk.Button(self).setText(option).setCommand(tk.CustomRunnable(self._selectOption, option))
        self.create()

    def _selectOption(self, opt):
        if self.cmd is None: return
        self.cmd(opt)

    def openSelector(self, cmd):
        self.open(self.loc)
        self.cmd = cmd
class Tool:
    def __init__(self, plugin):
        self.enabled = True
    def onCreateGUI(self):
        pass
    def onSelect(self):
        pass
###############
# Tools start #
###############

# add new Tools Here!

@register(name="Java Path Finder")
class TJavaPathFinder(Tool):
    def onSelect(self):
        def onSelect(opt):
            copy(opt)
        def parse(path):
            return [os.path.join(path, i, "bin") for i in os.listdir(path)]
        paths = []
        if os.path.exists(os.path.join("C:\Program Files", "Java")):
            paths += parse(os.path.join("C:\Program Files", "Java"))
        if os.path.exists(os.path.join("C:\Program Files (x86)", "Java")):
            paths += parse(os.path.join("C:\Program Files (x86)", "Java"))
        onc = OneClickSelector(paths)
        onc.openSelector(onSelect)


#############
# Tools end #
#############

class ToolPlugin(EventHandler):
    def onEnable(self):
        self.tools = {} # name:class Tool instances
        self.lf_available_tools = tk.LabelFrame(self.master, SG)

        self.availableTools = tk.Listbox(self.lf_available_tools, SG)
        self.availableTools.bind(self.onToolSelect, tk.EventType.DOUBBLE_LEFT)
        self.availableTools.bind(self.onToolSelect, tk.EventType.RETURN)
        self.availableTools.bindArrowKeys()
        self.availableTools._get()["activestyle"] = "none"  # remove underline on select
        self.availableTools.setSelectForeGroundColor(tk.Color.WHITE)
        self.availableTools.setSelectBackGroundColor(Color.COLOR_GRAY)

        for name, data in iterDict(REGISTER):
            clazz, enabled = data
            if not enabled: continue
            self.tools[name.replace(" ", "_")] = clazz(self)
            self.availableTools.add(name)

        self.lf_available_tools.setText(f"Available Tools [{self.availableTools.length()}]")
        self.availableTools.placeRelative(changeHeight=-20-25, changeWidth=-5, changeY=25)
        self.search_E = tk.Entry(self.lf_available_tools, SG)
        self.search_E.onUserInputEvent(self.onSearch)
        self.search_E.bind(self.onSearchRightClick, tk.EventType.RIGHT_CLICK)
        self.search_E.bind(self.onSearchRightClick, tk.EventType.ESC)
        self.search_E.placeRelative(fixHeight=25, changeWidth=-5)
        self.search_E.bind(self.arrowKeysEntry, tk.EventType.ARROW_UP, args=["up"])
        self.search_E.bind(self.arrowKeysEntry, tk.EventType.ARROW_DOWN, args=["down"])

        self.lf_available_tools.placeRelative(xOffsetRight=50)
    def onSearch(self, e):
        con = self.search_E.getText().lower()
        self.availableTools.clear()
        for tool_name, class_ in iterDict(self.tools):
            tool = tool_name.lower()
            if con in tool or con == "":
                self.availableTools.add(tool_name.replace("_", " "))
    def onSearchRightClick(self, e):
        self.search_E.clear()
        self.onSearch("")
    def onToolSelect(self, e):
        sel = self.availableTools.getSelectedItem()
        if sel is None: return
        sel = sel.replace(" ", "_")
        _class = self.tools[sel]
        _class.onSelect()
    def onTabRegisterEvent(self):
        self.master = plugin.registerTab("Tools")
    def arrowKeysEntry(self, e):
        pass
plugin = Plugin(priority=0)
plugin.register(ToolPlugin)