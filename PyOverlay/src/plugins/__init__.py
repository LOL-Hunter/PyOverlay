import pysettings.tk as tk
from pysettings.text import MsgText, TextColor
from traceback import format_exc
from PyOverlay.src.pluginManager import PluginManager as _PluginManager
from PyOverlay.src.constants import STYLE_GROUP as SG
"""
Plugin API

"""

class _Exceptions:
    class RegisterError(Exception):
        pass
class Event:
    def __init__(self, d=None):
        data = {"setCanceled":False, "cancelOther":False, "frame":None}
        if isinstance(d, dict):
            self.data = {**data, **d}
        elif d is None:
            self.data = data
        elif isinstance(d, Event):
            self.data = d.data
    def __getitem__(self, item):
        return self.data[item]
    def __setitem__(self, key, value):
        self.data[key] = value
    def getPath(self):
        return self["path"]
    def setCanceled(self, b:bool):
        self["setCanceled"] = b
    def cancelOtherCalls(self, b):
        self["cancelOther"] = b
class _EventHandler:
    def __init__(self, plugin):
        self.plugin = plugin
    def _handler(self):
        handler = self.plugin._pluginClass
        if handler is None:
            return EventHandler()
        else:
            return handler
    def onEnable(self, kw):
        event = Event(kw)
        self._handler().onEnable()
        return event
    def onOpen(self, kw):
        event = Event(kw)
        self._handler().onOpen()
        return event
    def onClose(self, kw):
        event = Event(kw)
        self._handler().onClose()
        return event
    def onDisable(self, kw):
        event = Event(kw)
        self._handler().onDisable(event)
        return event
    def onSettingsFrameConstruct(self, kw):
        event = Event(kw)
        self._handler().onSettingsFrameConstruct(event["frame"])
        return event
    def onSettingsCloseEvent(self, kw):
        event = Event(kw)
        self._handler().onSettingsCloseEvent(event)
        return event
    def onTabRegisterEvent(self, kw):
        Plugin.CAN_REGISTER_TAB = 1
        self._handler().onTabRegisterEvent()
        del Plugin.CAN_REGISTER_TAB


class EventHandler:
    def onEnable(self):
        pass
    def onDisable(self, e):
        pass
    def onSettingsFrameConstruct(self, frame):
        pass
    def onSettingsCloseEvent(self, e):
        pass
    def onTabRegisterEvent(self):
        pass
    def onOpen(self):
        pass
    def onClose(self):
        pass

class _Command:
    def __init__(self, ins, target):
        self.ins = ins
        self.target = target
    def run(self, *args, **kwargs):
        if self.ins._getStateHook(self.ins._pluginName) == "active":
            self.target(*args, **kwargs)
class Plugin:
    _INSTANCE = None # temporary variable for Plugin instance
    def __init__(self, priority=0):
        self.priority = priority
        self.triggerEvent = self._call
        self._disabledInDev = False

        self._defaultBinds = {}

        self._commands = []
        self._frame = None
        self._handler = _EventHandler(self)
        self._disabled = False
        self._bindings = []

        self._pluginName = ""
        self._getStateHook = None
        self._window = None


        self._pluginClass = None
    def __repr__(self):
        return f"{self._pluginClass.__class__.__name__}(priority={self.priority})"
    def _call(self, eventName, **kwargs):
        if hasattr(self._handler, eventName):
            func = getattr(self._handler, eventName)
            return func(kwargs)
        else:
            MsgText.error("Could not trigger EventType: "+eventName)
    def call(self, eventName, **kwargs):
        _PluginManager.call(eventName, **kwargs)
    def _constructPluginSettings(self, frame):
        self._call("onSettingsFrameConstruct", frame=frame)
        return frame
    def _quit(self):
        pass
    def _run(self):
        for i in self._bindings:
            i.register(self._pluginName)
    def _getPluginClass(self):
        return self._pluginClass
    def update(self):
        self._window.update()
    def registerTab(self, name:str)->tk.NotebookTab:
        if hasattr(Plugin, "CAN_REGISTER_TAB"):
            return self._window._menu.createNewTab(name, SG)
        raise Exception("Cannot register Tab now! Use the 'onTabRegisterEvent' to register a new Tab.")
    def registerOverlay(self, ovly):
        ovly(self._window)
    def getWindow(self):
        if self._window is None:
            return "Tk" # to convert Toplevel to Tk
        return self._window
    def register(self, _class):
        try:
            self._pluginClass = _class()
        except:
            exc = format_exc()
            tk.SimpleDialog.askError(self._window, f"An error has occurred while running __init__ from plugin '{self._pluginName}':"+exc)
            TextColor.print(exc, "red")
        Plugin._INSTANCE = self
    def disable(self):
        self._disabled = True
    def disableInDevMode(self):
        """
        dont run in dev mode
        @return:
        """
        self._disabledInDev = True

    def isDevMode(self)->bool:
        return self._window.devMode
    def isOverlayOpen(self)->bool:
        return not self._window._isMinimized
