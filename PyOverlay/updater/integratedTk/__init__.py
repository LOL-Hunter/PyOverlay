import tkinter.simpledialog as simd
import tkinter.colorchooser as colorChooser
import tkinter.messagebox as msg
import tkinter.filedialog as fd
import tkinter.font as _font
import tkinter.ttk as ttk
import tkinter as _tk_
import threading as th
from typing import Union, Callable, Iterable
from datetime import date
from enum import Enum
from traceback import format_exc
import random as r
import string
import time as t
try:
    from ..geometry import Location2D, _map, Rect
    from ..text import MsgText, TextColor
except ImportError:
    from pysettings.geometry import Location2D, _map, Rect
    from pysettings.text import MsgText, TextColor
import os

## TEMP ##
from pysettings.text import TextColor

tk = None # cuz i'm sometimes dump lol
WIDGET_DELETE_DEBUG = False
#Draggable class

#TODO Cannot bind two same events!!!
#Check Entry Content: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/entry-validation.html
#System-Tray: https://www.tutorialspoint.com/how-to-create-a-system-tray-icon-of-a-tkinter-application
#icon zb askyesno
#ttk.Styles ???
#spinBox scrollable + onScrollEvent
#finish calendar
#key: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/key-names.html
#Scrollbar: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/scrollbar.html
#def clone(self): -> widget

#TEMPLATES
#-Keyboard
#statisc tamplate
"""
# Various canvas styles
PIESLICE='pieslice'
CHORD='chord'
ARC='arc'
FIRST='first'
LAST='last'
BUTT='butt'
PROJECTING='projecting'
ROUND='round'
BEVEL='bevel'
MITER='miter'

"""

"""


def cut_text():
        text.event_generate(("<<Cut>>"))
# define function to copy 
# the selected text
def copy_text():
        text.event_generate(("<<Copy>>"))
# define function to paste 
# the previously copied text
def paste_text():
        text.event_generate(("<<Paste>>"))


"""
# WIDGET GROUPS TO CHANGE SETTINGS FOR ALL
#Funcs from class Wm
"""
WM_ATTRIBUTES
-alpha double
how opaque the overall window is; note that changing between 1.0 and any other value may cause the window to flash (Tk changes the class of window used to implement the toplevel).
-fullscreen boolean
controls whether the window fills the whole screen, including taskbar
-disabled boolean
makes it impossible to interact with the window and redraws the focus
-toolwindow boolean
makes a window with a single close-button (which is smaller than usual) on the right of the title bar
-topmost boolean
makes sure the window always stays on top of all other windows
"""
class TKExceptions:
    class InvalidFileExtention(Exception):
        pass
    class PathNotExisits(Exception):
        pass
    class InvalidUsageException(Exception):
        pass
    class InvalidHeaderException(Exception):
        pass
    class InvalidWidgetTypeException(Exception):
        pass
    class EventExecutorException(Exception):
        pass
    class BindException(Exception):
        pass
class Symbol:
    DICE_1 = "\u2680"
    DICE_2 = "\u2681"
    DICE_3 = "\u2682"
    DICE_4 = "\u2683"
    DICE_5 = "\u2684"
    DICE_6 = "\u2685"
class FontType(Enum):
    ARIAL ="arial"
class Orient(Enum):
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"
class Style(Enum):
    FLAT = "flat"
    SOLID = "solid"
    RAISED = "raised"
    SUNKEN = "sunken"
    GROOVE = "groove"
    RIDGE = "ridge"
class Anchor(Enum):
    NW = UP_LEFT = "nw"
    NE = UP_RIGHT = "ne"
    SW = DOWN_LEFT = "sw"
    SE = DOWN_RIGHT = "se"
    CENTER = MIDDLE = "center"
    N = UP = "n"
    E = RIGHT = "e"
    S = DOWN = "s"
    W = LEFT = "w"
class Direction(Enum):
    LEFT = "left"
    RIGHT = "right"
    CENTER = "center"
    NONE = "none"
    TOP = "top"
    BOTTOM = "bottom"
class Color(Enum):
    DEFAULT = "#F0F0F0"
    WHITE = "white"
    BLACK = "black"
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
    CYAN = "cyan"
    YELLOW = "yellow"
    MAGENTA = "magenta"
    ORANGE = "#CB772F"
    @staticmethod
    def rgb(r, g, b):
        return '#%02x%02x%02x' % (r, g, b)
    @staticmethod
    def hex(hex:str):
        return hex
    @staticmethod
    def randomRGB():
        return Color.rgb(r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))
    @staticmethod
    def randomColor():
        return r.choice(list(Color))
class Wrap(Enum):
    NONE = "none"
    WORD = "word"
    CHAR = "char"
class Cursor(Enum):
    NONE = "none"
    WIN_DEFAULT = "arrow"
    WIN_TURN = "exchange"
    WIN_FOUR_ARROW = "fleur"
    WIN_TWO_ARROW_HORIZONTAL = "sb_h_double_arrow"
    WIN_TWO_ARROW_VERTICAL = "sb_v_double_arrow"
    WIN_TWO_ARROW_DIAGONAL = "size_nw_se"
    WIN_TWO_ARROW_DIAGONAL_INVERTED = "size_ne_sw"
    WIN_LOADING = "watch"
    WIN_CROSS = "tcross"
    WIN_CLICK_HAND = "hand2"
    WIN_MARK_TEXT = "xterm"

    SHAPE_CIRCLE = "circle"
    SHAPE_CROSS = "cross"
    SHAPE_DOTBOX = "dotbox"
    SHAPE_PLUS = "plus"

    CUSTOM_CLOCK = "clock"
    CUSTOM_HEART = "heart"
    CUSTOM_MAN = "man"
    CUSTOM_MOUSE = "mouse"
    CUSTOM_PIRATE = "pirate"
    CUSTOM_SHUTTLE = "shuttle"
    CUSTOM_SIZING = "sizing"
    CUSTOM_SPIDER = "spider"
    CUSTOM_SPRAYCAN = "spraycan"
    CUSTOM_STAR = "star"
    CUSTOM_TARGET = "target"
    CUSTOM_TRECK = "trek"
class Key(Enum):
    SHIFT = "<Shift>"
    RETURN = "<Return>"
    DOWN = "<Down>"
    RIGHT = "<Right>"
    LEFT = "<Left>"
    UP = "<Up>"
class Mouse(Enum):
    MOUSE_MOTION = "<Motion>"
    WHEEL_MOTION = "<MouseWheel>"

    LEFT_CLICK_RELEASE = "<ButtonRelease-1>"
    RIGHT_CLICK_RELEASE = "<ButtonRelease-2>"
    MIDDLE_CLICK_RELEASE = "<ButtonRelease-2>"

    LEFT_CLICK_PRESS = "<ButtonPress-1>"
    RIGHT_CLICK_PRESS = "<ButtonPress-2>"
    MIDDLE_CLICK_PRESS = "<ButtonPress-2>"

    LEFT_CLICK = "<Button-1>"
    RIGHT_CLICK = "<Button-3>"
    MIDDLE_CLICK = "<Button-2>"

    MOTION_WITH_LEFT_CLICK = "<B1-Motion>"
    MOTION_WITH_RIGHT_CLICK = "<B2-Motion>"
    MOTION_WITH_MIDDLE_CLICK = "<B3-Motion>"

    DOUBBLE_LEFT = "<Double-Button-1>"
    DOUBBLE_RIGHT = "<Double-Button-2>"
    DOUBBLE_MIDDLE = "<Double-Button-3>"

class FunctionKey(Enum):
    CONTROL = CTRL = "Control"
    ALT = "Alt"
class EventType(Enum):

    def __add__(self, other):
        this = self.value.replace("<", "").replace(">", "")
        other = (other.value if hasattr(other, "value") else other).replace("<", "").replace(">", "")
        return "<"+this+"-"+other+">"

    #Mouse
    MOUSE_MOTION = "<Motion>"
    WHEEL_MOTION = "<MouseWheel>"

    LEFT_CLICK = "<Button-1>"
    RIGHT_CLICK = "<Button-3>"
    MIDDLE_CLICK = "<Button-2>"

    LEFT_CLICK_RELEASE = "<ButtonRelease-1>"
    RIGHT_CLICK_RELEASE = "<ButtonRelease-2>"
    MIDDLE_CLICK_RELEASE = "<ButtonRelease-2>"

    LEFT_CLICK_PRESS = "<ButtonPress-1>"
    RIGHT_CLICK_PRESS = "<ButtonPress-2>"
    MIDDLE_CLICK_PRESS = "<ButtonPress-2>"


    DOUBBLE_LEFT = "<Double-Button-1>"
    DOUBBLE_RIGHT = "<Double-Button-2>"
    DOUBBLE_MIDDLE = "<Double-Button-3>"

    MOTION_WITH_LEFT_CLICK = "<B1-Motion>"
    MOTION_WITH_RIGHT_CLICK = "<B2-Motion>"
    MOTION_WITH_MIDDLE_CLICK = "<B3-Motion>"

    MOUSE_NEXT = "<Button-5>"
    MOUSE_PREV = "<Button-4>"
    #key Events
    KEY_UP = "<KeyRelease>"
    KEY_DOWN = "<KeyDown>"
    ESCAPE = ESC = "<Escape>"
    DELETE = "<Delete>"
    SPACE = "<space>"
    BACKSPACE = "<BackSpace>"

    STRG_LEFT = "<Control_L>"
    STRG_RIGHT = "<Control_R>"
    STRG_LEFT_UP = "<KeyRelease-Control_L>"
    STRG_RIGHT_UP = "<KeyRelease-Control_R>"
    STRG_LEFT_DOWN = "<KeyPress-Control_L>"
    STRG_RIGHT_DOWN = "<KeyPress-Control_R>"

    ALT_LEFT = "<Alt_L>"
    ALT_RIGHT = "<Alt_R>"
    ALT_LEFT_UP = "<KeyRelease-Alt_L>"
    ALT_RIGHT_UP = "<KeyRelease-Alt_R>"
    ALT_LEFT_DOWN = "<KeyPress-Alt_L>"
    ALT_RIGHT_DOWN = "<KeyPress-Alt_R>"

    SHIFT = "<Shift>"
    SHIFT_LEFT_UP = "<KeyRelease-Shift_L>"
    SHIFT_RIGHT_UP = "<KeyRelease-Shift_R>"
    SHIFT_LEFT_DOWN = "<KeyPress-Shift_L>"
    SHIFT_RIGHT_DOWN = "<KeyPress-Shift_R>"

    RETURN = "<Return>"
    RETURN_UP = "<KeyRelease-Return>"
    RETURN_DOWN = "<KeyPress-Return>"

    ARROW_DOWN = "<Down>"
    ARROW_RIGHT = "<Right>"
    ARROW_LEFT = "<Left>"
    ARROW_UP = "<Up>"

    #hotkeys
    CONTROL_S = "<Control-s>"
    CONTROL_C = "<Control-c>"
    CONTROL_V = "<Control-v>"
    CONTROL_Y = "<Control-y>"
    CONTROL_Z = "<Control-z>"
    CONTROL_X = "<Control-x>"

    F1 = "<F1>"
    F2 = "<F2>"
    F3 = "<F3>"
    F4 = "<F4>"
    F5 = "<F5>"


    #widget Events
    SIZE_CONFIUGURE = "<Configure>"
    DESTROY = "<Destroy>"
    ALL = ALL_KEYS = "<Key>"
    ENTER = "<Enter>"
    LEAVE = "<Leave>"
    LISTBOX_SELECT = "<<ListboxSelect>>"
    COMBOBOX_SELECT = "<<ComboboxSelected>>"
    #custom
    CUSTOM_RELATIVE_UPDATE = "[relative_update]" # [x, y, width, height]
    CUSTOM_RELATIVE_UPDATE_AFTER = "[relative_update_after]" # [x, y, width, height]

    @staticmethod
    def mouse(m):
        return m
    @staticmethod
    def key(k):
        return k
    @staticmethod
    def keyDown(k):
        return "<KeyPress-"+(k.value if hasattr(k, "value") else k)+">"
    @staticmethod
    def keyUp(k):
        return "<KeyRelease-"+(k.value if hasattr(k, "value") else k)+">"
    @staticmethod
    def customEvent(k):
        return k
    @staticmethod
    def hotKey(k1:FunctionKey, k2, k3=None):
        if k3 is not None and not isinstance(k2, FunctionKey): raise ValueError("if k3 is not None then k2 must be instance of 'FunctionKey'!")
        return "<"+(k1.value if hasattr(k1, "value") else k1)+"-"+(k2.value if hasattr(k2, "value") else k2)+("-"+(k3.value if hasattr(k3, "value") else k3) if k3 is not None else "")+">"

class Cmd:
    """
    Custom Runnable.

    """
    def __init__(self, command, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.command = command
    def __call__(self, *args, **kwargs):
        self.command(*self.args, **self.kwargs)

class PILImage:
    def __init__(self, image):
        import PIL.Image as Image
        self.copy = self.clone
        self._preRenderedImage = None
        self._pilImage = Image # cuz pil.image must exist in whole class!
        self._useOrg = False
        if isinstance(image, str):
            self._image = self._pilImage.open(image)
        elif isinstance(image, Image.Image):
            self._image = image
        else:
            raise TKExceptions.InvalidUsageException("Use 'Image.loadImage(<path>)' instead! Not:"+str(type(image)))
        self._original = self._image.copy()
    @staticmethod
    def loadImage(path):
        if os.path.exists(path):
            return PILImage(path)
        else:
            raise TKExceptions.PathNotExisits("This path does not Exists: "+str(path))
    @staticmethod
    def loadImageFromPIL(image):
        return PILImage(image)
    def clone(self, orginal=False):
        return PILImage(self._image.copy() if not orginal else self._original.copy())
    def toOriginal(self):
        self._image = self._original
        return self
    def resizeToIcon(self, useOriginal=True):
        #256x256
        if useOriginal:
            self._image = self._original.resize((16, 16))
        else:
            self._image = self._image.resize((16, 16))
        return self
    def resize(self, fac, useOriginal=True):
        if useOriginal:
            self._image = self._original.resize((int(round(self._original.width * fac, 0)), int(round(self._original.height * fac, 0))))
        else:
            self._image = self._image.resize((int(round(self._image.width * fac, 0)), int(round(self._image.height * fac, 0))))
        return self
    def resizeTo(self, x, y=None, useOriginal=True):
        if isinstance(x, Rect):
            x, y = x.getWidth(), x.getHeight()
        x = int(round(x, 0))
        y = int(round(y, 0))
        if useOriginal:
            self._image = self._original.resize((x, y))
        else:
            self._image = self._image.resize((x, y))
        return self
    def crop(self, loc:Location2D, loc2:Location2D, useOriginal=True):
        if useOriginal:
            self._image = self._original.crop((*loc.get(), *loc2.get()))
        else:
            self._image = self._image.crop((*loc.get(), *loc2.get()))
        return self
    def getWidth(self):
        return self._image.width
    def getHeight(self):
        return self._image.height
    def preRender(self):
        import PIL.ImageTk as imgTk
        self._preRenderedImage = imgTk.PhotoImage(self._image)
        return self
    def _get(self):
        if self._preRenderedImage is None:
            self.preRender()
            img = self._preRenderedImage
            self._preRenderedImage = None
            return img
        else:
            return self._preRenderedImage
    def _getPIL(self):
        return self._image
class TkImage:
    def __init__(self, image:_tk_.PhotoImage):
        if isinstance(image, _tk_.PhotoImage):
            self.image = image
        else:
            raise TKExceptions.InvalidUsageException("Use 'Image.loadImage(<path>)' instad! Not:" + str(type(image)))
    @staticmethod
    def loadImage(path):
        if os.path.exists(path):
            return TkImage(_tk_.PhotoImage(file=path))
        else:
            raise TKExceptions.PathNotExisits("This path does not Exists: " + str(path))
    def resize(self, f:int):
        self.image = self.image.subsample(f)
    def getWidth(self):
        return int(self.image["width"])
    def getHeight(self):
        return int(self.image["height"])
    def _get(self, o=None):
        return self.image

class Event:
    def __init__(self, dic=None, **kwargs):
        if dic is None:
            self.data = {"afterTriggered":None,
                         "setCanceled": False,
                         "widget": None,
                         "args":[],
                         "priority":0,
                         "tkArgs":None,
                         "func":None,
                         "value":None,
                         "eventType":None,
                         "defaultArgs":False,
                         "disableArgs":True,
                         "decryptValueFunc":None,
                         "forceReturn":None,
                         "handler":None,
                         "pos":None,
                         "setTkEventCanceled":False}
        else:
            self.data = dic.data

        for k, v in zip(kwargs.keys(), kwargs.items()):
            self.data[k] = v
    def __repr__(self):
        func = f"'{'' if not hasattr(self.data['func'], '__self__') else self.data['func'].__self__.__class__.__name__ + '.'}{self.data['func'] if not hasattr(self.data['func'], '__name__') else self.data['func'].__name__}'"
        return f"Event({{func: {func}, args:"+str(self["args"])+", priority:"+str(self["priority"])+", setCanceled:"+str(self["setCanceled"])+"})"
    def __call__(self):
        if self["handler"] is None:
            return
        return self["handler"]()
    def __getitem__(self, item):
        return self.data[item]
    def __setitem__(self, key, value):
        self.data[key] = value
    def __lt__(self, other):
        return self["priority"] < other["priority"]
    def getTkArgs(self):
        return self["tkArgs"]
    def setCanceled(self, b:bool=True):
        self["setCanceled"] = b
    def getWidget(self):
        return self["widget"]
    def getValue(self):
        return self["value"]
    def getPos(self)->Location2D:
        return self["pos"]
    def getScrollDelta(self):
        return self["tkArgs"].delta if hasattr(self["tkArgs"], "delta") else None
    def getArgs(self, i=None):
        if self["args"] is None: return None
        if type(i) is int: return self["args"][i]
        return self["args"]
    def getEventType(self):
        return self["eventType"]
    def getKey(self):
        return self.getTkArgs().keysym
    def isKey(self, k):
        k = k.value if hasattr(k, "value") else k
        k = k.replace("<", "").replace(">", "")
        if not hasattr(self.getTkArgs(), "keysym"): return False
        return k == self.getTkArgs().keysym
    def setTkEventCanceled(self, b:bool=True):
        self["setTkEventCanceled"] = b
    def info(self):
        print("This Event[type: "+self["eventType"]+"] was triggered by "+str(type(self["widget"]))+"! | Args:"+str(self["args"]))
class ScrollBarEvent(Event):
    pass
class _EventRegistry:
    def __init__(self, ins):
        if isinstance(ins, Widget) or isinstance(ins, Tk) or isinstance(ins, CanvasObject):
            self.data = {"event":{}, "widget":ins} # event : { type_ : ( <type:_EventHandler>, [<type:Event>, ...] ) }
        elif isinstance(ins, dict):
            self.data = ins
        elif isinstance(ins, _EventRegistry):
            self.data = ins.data
        else:
            raise TKExceptions.InvalidWidgetTypeException("ins must be " + str(self.__class__.__name__) + " instance not: " + str(ins.__class__.__name__))
    def __repr__(self):
        return str(self.__class__.__name__)+"("+str(self.data)+")"
    def __getitem__(self, item):
        return self.data[item]
    def __setitem__(self, key, value):
        self.data[key] = value
    def printAllBinds(self):
        print("Widget: "+self["widget"].__class__.__name__)
        for k, v in zip(self["event"].keys(), self["event"].values()):
            print("-EventType: "+k+":")
            for event in v[1]:
                print(" -bind to: "+event["func"].__name__)
    def rawCallable(self):
        return None
    def addEvent(self, event, type_):
        handler = None
        if type_ in self["event"].keys(): # add Event
            self["event"][type_][1].append(event)
            self["event"][type_][1].sort()
            self["event"][type_][1].reverse()
        else:                             # new event type
            handler = EventHandler(event)
            self["event"][type_] = (handler, [event])
        if EventHandler.DEBUG:
            print(self["event"][type_][0])
        return handler
    def getRegisteredEvents(self, type_):
        return self["event"][type_][1]
    def getCallables(self, type_)->Union[Event, list]:
        if type_ in self["event"].keys():
            return self["event"][type_][1]
        return []
    def getHandler(self, type_):
        if type_ in self["event"].keys():
            return self["event"][type_][0]
        return None
    def unregisterType(self, type_):
        if hasattr(type_, "value"):
            eventType = type_.value
        if type_ in self["event"].keys():
            _e = Event(self["event"][type_][0].event)
            _e.getWidget()._get().unbind(_e.getEventType())
            self["event"].pop(type_)
    def unregisterAll(self):
        for i in self["event"].values():
            _e = Event(i[0].event)
            try:
                _e.getWidget()._get().unbind(_e.getEventType())
            except:

                pass
        self["event"] = {}
class EventHandler:
    DEBUG = False
    #OLD:  _Events = {} #save in Individual instance! { <obj_id> : <type: _EventHandler> }
    def __init__(self, event):
        assert isinstance(event, Event), "Do not instance this class by yourself!"
        self.event = event
        #print(self.event.getWidget()["registry"], self.event.getWidget())
    def __repr__(self):
        return "EventHandler("+"{widgetType:\""+self.event["widget"].getType().__name__+"\", eventType:"+str(self.event["eventType"])+", ID:"+self.event["widget"]["id"]+"}) bind on: \n\t-"+"\n\t-".join([str(i) for i in self.event["widget"]["registry"].getRegisteredEvents(self.event["eventType"])])
    def __getitem__(self, item):
        return self.event[item]
    def __setitem__(self, key, value):
        self.event[key] = value
    def __call__(self, *args):
        def raiseError():
            exc = format_exc()
            info = f"""
# Could not call bound function!
# BindTo:    '{"" if not hasattr(event["func"], "__self__") else event["func"].__self__.__class__.__name__ + "."}{event["func"] if not hasattr(event["func"], "__name__") else event["func"].__name__}'
# Widget:    '{event["widget"].getType().__name__}'
# EventType: {event["eventType"]}
# priority:  {event["priority"]}
# args:      {event["args"]}
# value:     {event["value"]}"""
            _max = max([len(i) for i in info.splitlines()])
            _info = ""
            for i in info.splitlines():
                _info += i + " "*(_max-len(i)+1) + "#" + "\n"
            info = _info
            info = "\n" + "#" *(_max+2) + info + "#" *(_max+2)

            raise TKExceptions.EventExecutorException(info)
        args = args[0] if len(args) == 1 else list(args)
        event = None
        out = None
        cancTk = False
        for event in self.event["widget"]["registry"].getCallables(self.event["eventType"]): #TODO get only the output of the last called func. problem? maybe priorities
            func = event["func"]
            event["tkArgs"] = args
            if event["setTkEventCanceled"]: cancTk = True
            if event["decryptValueFunc"] is not None:
                event["value"] = event["decryptValueFunc"](args) #TODO event in 'decryptValueFunc'
                if event["value"] == "CANCEL":
                    return
            if not event["defaultArgs"]:
                if event["value"] is None:
                    if hasattr(args, "x") and hasattr(args, "y"):
                        event["pos"] = Location2D(args.x, args.y)
                args = event
            if ((not hasattr(func, "__code__")) or ("self" in func.__code__.co_varnames and func.__code__.co_argcount > 1) or ("self" not in func.__code__.co_varnames and func.__code__.co_argcount > 0)) and not event["disableArgs"]:

                try:
                    out = func(args)
                except:
                    raiseError()
            else:
                try:
                    out = func()
                except:
                    raiseError()
            if event["afterTriggered"] is not None: event["afterTriggered"](event, out)
        #print("AFTER CALLED", self.event.data)
        if event is None: return
        if event["forceReturn"] is None:
            if event["setTkEventCanceled"]:
                if cancTk: return "break"
                else: return out
            #if event["forceReturn"]:
            #    return event["forceReturn"]
            #else: return out
        else: return event["forceReturn"]
    @staticmethod
    def setEventDebug(b:bool):
        EventHandler.DEBUG = b
    @staticmethod
    def printAllBinds(widget):
        widget["registry"].printAllBinds()
    @staticmethod
    def _registerNewEvent(obj, func, eventType:Union[EventType, Key, Mouse], args: list, priority:int, decryptValueFunc=None, defaultArgs=False, disableArgs=False):
        """
        This is the intern Event-Register
        @param obj: the widget
        @param func: the target function to be bound
        @param eventType: the event type to trigger the event
        @param args: arguments which are transferred to the function
        @param decryptValueFunc: this function gets called before the binded func was called
        @param defaultArgs: this bool decides if the 'Event' instance or the mormal tkinter args are passed into the target function
        @param disableArgs: if this is True no arguments will be passed
        @return: None
        """
        if hasattr(eventType, "value"):
            eventType = eventType.value
        assert isinstance(func, Callable), eventType + " bound Func is not callable " + str(func) + " instead!"
        event = Event()
        event["defaultArgs"] = defaultArgs
        event["disableArgs"] = disableArgs
        event["widget"] = obj
        event["args"] = args
        event["func"] = func
        event["decryptValueFunc"] = decryptValueFunc
        event["eventType"] = eventType
        event["priority"] = priority
        handler = obj["registry"].addEvent(event, eventType)
        if handler is not None:
            try:
                obj._get().bind(eventType, handler)
            except:
                func = f"'{'' if not hasattr(func, '__self__') else func.__self__.__class__.__name__ + '.'}{func if not hasattr(func, '__name__') else func.__name__}'"
                raise TKExceptions.BindException(f"Could not bind event type '{eventType}' to func {func}!")
        event["handler"] = EventHandler(event)
        return event
    @staticmethod
    def _registerNewCommand(obj, func, args:Union[list, None], priority:int, decryptValueFunc=None, defaultArgs=False, disableArgs=False, onlyGetRunnable=False, cmd="command"):
        assert isinstance(func, Callable), "command binded Func is not callable " + str(type(func)) + " instead!"
        event = Event()
        event["defaultArgs"] = defaultArgs
        event["disableArgs"] = disableArgs
        event["widget"] = obj
        event["args"] = args
        event["func"] = func
        event["priority"] = priority
        event["decryptValueFunc"] = decryptValueFunc
        event["eventType"] = "cmd"
        handler = obj["registry"].addEvent(event, "cmd")
        if not onlyGetRunnable:
            if handler is not None:
                obj._get()[cmd] = handler
            event["handler"] = EventHandler(event)

        else:
            return handler
        return event
    @staticmethod
    def _registerNewValidateCommand(obj, func, args:list, priority:int, type_="all", decryptValueFunc=None, defaultArgs=False, disableArgs=False):
        assert isinstance(func, Callable), "vCommand binded Func is not callable " + str(type(func)) + " instead!"
        event = Event()
        event["defaultArgs"] = defaultArgs
        event["disableArgs"] = disableArgs
        event["widget"] = obj
        event["args"] = args
        event["func"] = func
        event["priority"] = priority
        event["decryptValueFunc"] = decryptValueFunc
        event["forceReturn"] = True
        event["eventType"] = "vcmd"
        handler = obj["registry"].addEvent(event, "vcmd")
        if handler is not None:
            obj["widget"]["validate"] = type_
            obj["widget"]["validatecommand"] = (obj["master"]._get().register(handler), '%P')
        event["handler"] = EventHandler(event)
    @staticmethod
    def _registerNewTracer(obj, var, func, args:list, priority:int, decryptValueFunc=None, defaultArgs=False, disableArgs=False):
        assert isinstance(func, Callable), "tracer bound Func is not callable " + str(type(func)) + " instead!"
        event = Event()
        event["defaultArgs"] = defaultArgs
        event["disableArgs"] = disableArgs
        event["widget"] = obj
        event["args"] = args
        event["func"] = func
        event["priority"] = priority
        event["decryptValueFunc"] = decryptValueFunc
        event["eventType"] = "trace"
        handler = obj["registry"].addEvent(event, "trace")
        if handler is not None:
            var.trace("w", handler)
        event["handler"] = EventHandler(event)
    @staticmethod
    def _getNewEventRunnable(obj, func, args, priority:int, decryptValueFunc=None, defaultArgs=False, disableArgs=False, after=None):
        assert isinstance(func, Callable), "Runnable bound Func is not callable " + str(type(func)) + " instead!"
        event = Event()
        event["defaultArgs"] = defaultArgs
        event["disableArgs"] = disableArgs
        event["widget"] = obj
        event["args"] = args
        event["func"] = func
        event["priority"] = priority
        event["decryptValueFunc"] = decryptValueFunc
        event["afterTriggered"] = after
        event["eventType"] = "runnable"
        handler = obj["registry"].addEvent(event, "runnable")
        if handler is not None:
            event["handler"] = handler
        else:
            event["handler"] = EventHandler(event)
        return event["handler"]
    @staticmethod
    def _registerNewCustomEvent(obj, func, eventType:Union[EventType, Key, Mouse], args, priority: int, decryptValueFunc=None, defaultArgs=False, disableArgs=False, after=None):
        assert isinstance(func, Callable), "CustomEvent bound Func is not callable " + str(type(func)) + " instead!"
        if hasattr(eventType, "value"):
            eventType = eventType.value
        event = Event()
        event["defaultArgs"] = defaultArgs
        event["disableArgs"] = disableArgs
        event["widget"] = obj
        event["args"] = args
        event["func"] = func
        event["priority"] = priority
        event["decryptValueFunc"] = decryptValueFunc
        event["afterTriggered"] = after
        event["eventType"] = eventType
        handler = obj["registry"].addEvent(event, eventType)
        eventType = eventType.value if hasattr(eventType, "value") else eventType
        event["handler"] = EventHandler(event)


        if eventType == "[relative_update]" or eventType == "[relative_update_after]":
            obj["placeRelData"]["handler"] = EventHandler(event)


        return handler
    @staticmethod
    def _registerNewTagBind(obj, id_, func, eventType: Union[EventType, Key, Mouse], args: list, priority:int, decryptValueFunc=None, defaultArgs=False, disableArgs=False):
        if hasattr(eventType, "value"):
            eventType = eventType.value
        assert isinstance(func, Callable), eventType + " boun Func is not callable " + str(func) + " instead!"
        event = Event()
        event["defaultArgs"] = defaultArgs
        event["disableArgs"] = disableArgs
        event["widget"] = obj
        event["args"] = args
        event["func"] = func
        event["priority"] = priority
        event["decryptValueFunc"] = decryptValueFunc
        event["eventType"] = eventType
        handler = obj["registry"].addEvent(event, eventType)
        if handler is not None:
            obj._get().tag_bind(id_, eventType, handler)
        event["handler"] = EventHandler(event)
class TaskScheduler:
    def __init__(self, _master, delay, func, repete=False, dynamic=False):
        if hasattr(_master, "_get"):
            self._id = None
            self._master = _master
            self._delay = delay
            self._func = func
            self._repete = repete
            self._dynamic = dynamic
        else:
            raise TKExceptions.InvalidWidgetTypeException("WidgetType must be any 'tkWidget' or 'Tk' not:"+str(type(_master)))
    def start(self):
        self._id = self._master._get().after(int(self._delay*1000), self)
        return self
    def __call__(self):
        f = t.time()
        self._func()
        if self._repete:
            self._id = self._master._get().after(self._delay*1000 if not self._dynamic else self._delay-(t.time()-f) if self._delay-(t.time()-f) > 0 else 0, self)

    def cancel(self):
        if self._id is not None: self._master._get().after_cancel(self._id)
class IntVar:
    def __init__(self, _master):
        self.index = -1
        self.command = None
        self._intvar = _tk_.IntVar(_master._get())
    def _add(self):
        self.index +=1
        return self.index
    def _get(self):
        return self._intvar
    def get(self):
        return self._intvar.get()
    def set(self, v:int):
        self._intvar.set(v)

class Window:
    def __init__(self, ins):
        self.loopInterval = 0
        self.ins = ins
        self.master = Tk()
    def setLoopInterval(self, sec):
        self.loopInterval = sec
    def mainloop(self):
        if hasattr(self.ins, "loop"): self.ins.onEnable()
        th.Thread(target=self._loop).start()
        self.master.mainloop()
    def onEnable(self):
        pass
    def loop(self):
        pass
    def _loop(self):
        while True:
            if hasattr(self.ins, "loop"):
                t.sleep(self.loopInterval)
                self.ins.loop()

class Tk:
    """
    The toplevel window class

    """
    def __init__(self, _master=None, group=None):
        if group is not None: group.add(self)
        self.setAllwaysOnTop = self.setTopmost
        self.title = self.setTitle
        self.quit = self.quitMainLoop
        self.withdraw = self.hide
        if _master is None:
            self.data = {"master": _tk_.Tk(), "registry":_EventRegistry(self), "isRunning":False, "destroyed":False, "hasMenu":False, "childWidgets":{},"oldWinSize":(-1, -1), "setSize":(),  "privateOldWinSize":(-1, -1), "id":"".join([str(r.randint(0,9)) for _ in range(15)]), "dynamicWidgets":{}, "closeRunnable":None, "title":""}

            #configure internal onCloseEvent
            self["master"].protocol("WM_DELETE_WINDOW", self._internalOnClose)

        elif isinstance(_master, dict):
            self.data = _master
        elif isinstance(_master, Tk):
            self.data = _master.data
        else:
            raise TKExceptions.InvalidWidgetTypeException("_master must be " + str(self.__class__.__name__) + " instance not: " + str(_master.__class__.__name__))
    def __str__(self):
        return str(self.__class__.__name__)+"("+str(self.data)+")"
    def __getitem__(self, item):
        try:return self.data[item]
        except KeyError as e: raise KeyError("Item '"+str(item)+"' is not in dict of class '"+self["master"].__class__.__name__+"'")
    def __setitem__(self, key, value):
        self.data[key] = value
    def __del__(self):
        print("__DELETE__", type(self))
    def getType(self):
        return type(self)
    def runTask(self, func):
        task = TaskScheduler(self, 0, func)
        task._id = self["master"].after(0, task)
        return task
    def runTaskAfter(self, func, time):
        task = TaskScheduler(self, time, func)
        task._id = self["master"].after(int(time * 1000), task)
        return task
    def runIdleLoop(self, func):
        task = TaskScheduler(self, 0, func, repete=True)
        task._id = self["master"].after(0, task)
        return task
    def runDelayLoop(self, func, delay):
        task = TaskScheduler(self, delay, func, repete=True)
        task._id = self["master"].after(0, task)
        return task
    def runDynamicDelayLoop(self, delay, func):
        task = TaskScheduler(self, delay, func, repete=True, dynamic=True)
        task._id = self["master"].after(0, task)
        return task
    def getWindowActive(self):
        return self["isRunning"]
    def throwErrorSound(self):
        self["master"].bell()
    def onWindowResize(self, func, args:list=None, priority:int=0, defaultArgs=False, disableArgs=False, filterEvent=True):
        EventHandler._registerNewEvent(self, func, EventType.key("<Configure>"), args, priority, decryptValueFunc=(self._decryptWindowResize if filterEvent else self._decryptNonFilteredWindowResize), defaultArgs=defaultArgs, disableArgs=disableArgs)
    def copyToClip(self, s):
        self["master"].clipboard_append(str(s))
        return self
    def clearClip(self):
        self["master"].clipboard_clear()
        return self
    def getClip(self):
        return self["master"].clipboard_get()
    def setFocus(self):
        self["master"].focus_set()
        return self
    def forceFocus(self):
        self["master"].focus_force()
        return self

    def hide(self):
        self["master"].withdraw()
    def show(self):
        self["master"].deiconify()
    def setIcon(self, icon:Union[TkImage, PILImage]):
        self["master"].iconphoto(True, icon._get())
        return self
    def sleep(self, s):
        temp = t.time()
        while True:
            if not self["destroyed"]: self.update()
            if t.time()-temp >= s:
                break
        return self
    def lift(self):
        self["master"].lift()
        return self
    def closeViaESC(self):
        """
        Destroys the window via pressing ESC-key.
        Only if the setCanceled in the 'onCloseEvent' is False!
        @return:
        """
        assert self["closeRunnable"] is not None, "Bind 'onCloseEvent' Event first!"
        self.bind(self["closeRunnable"], EventType.ESC)
        return self
    def destroyViaESC(self):
        """
        Destroys the window via pressing ESC-key.
        @return:
        """
        self.bind(self.destroy, EventType.ESC)
        return self
    #def bindToWidgetType(self, func, eventType:Union[EventType, Key, Mouse], event, args:list=None, defaultArgs=False, disableArgs=False):
        #_EventHandler.registerNewEvent(self, func, event.__name__, args, defaultArgs=defaultArgs, disableArgs=disableArgs, bindFunc="bind_class")
    def bind(self, func:Callable, event:Union[EventType, Key, Mouse, str], args:list=None, priority:int=0, defaultArgs=False, disableArgs=False):
        if event == "CANCEL": return
        if hasattr(event, "value"):
            event = event.value
        if event.startswith("["):
            EventHandler._registerNewCustomEvent(self, func, event, args, priority, defaultArgs=defaultArgs, disableArgs=disableArgs)
        else:
            EventHandler._registerNewEvent(self, func, event, args, priority, defaultArgs=defaultArgs, disableArgs=disableArgs)
    #def bindAll(self, func, event: Union[EventType, Key, Mouse], args: list=None, priority:int=0, defaultArgs=False, disableArgs=False):
        #EventHandler._registerNewEvent(self, func, event, args, priority, defaultArgs=defaultArgs, disableArgs=disableArgs, bindFunc="bind_all")
    def unbindEvent(self, event:Union[EventType, Key, Mouse]):
        self["registry"].unregisterType(event)
    def unbindAllEvents(self):
        self["registry"].unregisterAll()
    def getMousePosition(self):
        """
        Returns the current mouse position on the TK window.
        @return:
        """
        return Location2D(self["master"].winfo_pointerx() - self["master"].winfo_rootx(), self["master"].winfo_pointery() - self["master"].winfo_rooty())
        #return Location2D(self["master"].winfo_pointerx(), self["master"].winfo_pointery())
    def getWidgetFromTk(self, w):
        for widg in self._getAllChildWidgets(self):
            pass
    def getWidgetFromLocation(self, loc:Location2D):
        #for widget in self._getAllChildWidgets(self):
        #    if widget._get()
        #print(*loc.get())
        widget = self["master"].winfo_containing(*loc.get())
        return widget
    def setCursor(self, c:Cursor):
        self["master"]["cursor"] = c.value if hasattr(c, "value") else c
    def hideCursor(self, b=True):
        if b: self["master"]["cursor"] = "none"
    def clearAllWidgets(self):
        for i in self["master"].winfo_children():
            i.destroy()
    def centerWindowOnScreen(self):
        width, height = self.getWindowSize()
        if width == 1:
            if len(self["setSize"]) == 2:
                width, height = self["setSize"]
        else:
            raise TKExceptions.InvalidUsageException("Run the mainloop first or specify a window size manually to center the Window!")
        swidth , sheight = self.getScreenSize()
        nwidth = int(round((swidth/2-width/2), 0))
        nheight = int(round((sheight/2-height/2), 0))
        self.setPositionOnScreen(nwidth, nheight)
        return self
    def destroy(self):
        #print("destroy Tk!")
        try:
            self["destroyed"] = True
            WidgetGroup.removeFromAll(self)
            widgets = self["childWidgets"].copy().values()
            for w in widgets:
                w.destroy()
            self["master"].destroy()
            return True

        except Exception as e:
            if WIDGET_DELETE_DEBUG:
                print("FAIL!", e)
                TextColor.print(format_exc(), "red")
            return False
    def update(self):
        self["master"].update()
    def updateIdleTasks(self):
        self["master"].update_idletasks()
    def activeWidgets(self): #@TODO: FIX!
        for i in self["master"].winfo_children():
            yield i
    def setCloseable(self, b:bool):
        self["master"].protocol("WM_DELETE_WINDOW", b)
    def setTitle(self, title):
        self["title"] = title
        self["master"].title(title)
        return self
    def setTransparent(self, color):
        color = color.value if hasattr(color, "value") else color
        self["master"].wm_attributes("-transparentcolor", color)
        return self
    def disable(self, b=True):
        self["master"].wm_attributes("-disabled", b)
    def overrideredirect(self, b=True):
        self["master"].overrideredirect(b)
    def setTopmost(self, b=True):
        self["master"].wm_attributes("-topmost", b)
    def setResizeable(self, b:bool):
        self["master"].resizable(b, b)
        return self
    def setFullscreen(self, b:bool):
        self["master"].wm_attributes("-fullscreen", b)
    def setPositionOnScreen(self, x, y=None):
        if isinstance(x, Location2D):
            x, y = x.get()
        elif y is None:
            raise TypeError("y cannot be None!")
        if str(x).find("-") == -1: x = "+" + str(x)
        if str(y).find("-") == -1: y = "+" + str(y)
        self["master"].geometry(str(x) + str(y))
    def close(self):
        """
        Closes the window only if it was not prevented in the 'windowCloseEvent' with the setCanceled.

        @return:
        """
        if self["closeRunnable"] is None:
            self.destroy()
        else:
            self["closeRunnable"]()
    def onCloseEvent(self, func, args:list=None, priority:int=0, defaultArgs=False, disableArgs=False):
        """
        This Event is triggered if the user close the window or press Alt+F4.


        @param func:
        @param args:
        @param priority:
        @param defaultArgs:
        @param disableArgs:
        @return:
        """
        def after(e, out):
            if not e["setCanceled"]:
                self.destroy()
        self["closeRunnable"] = EventHandler._getNewEventRunnable(self, func, args, priority, defaultArgs=defaultArgs, disableArgs=disableArgs)
        return self["closeRunnable"]
    def setBg(self, col):
        self["master"]["bg"] = col.value if hasattr(col, "value") else col
    def getHeight(self):
        return self["master"].winfo_height()
    def getWidth(self):
        return self["master"].winfo_width()
    def getScreenSize(self):
        return self["master"].winfo_screenwidth(), self["master"].winfo_screenheight()
    def getWindowSize(self):
        return self["master"].winfo_width(), self["master"].winfo_height()
    def setWindowSize(self, x:int, y:int, minsize=False):
        self["setSize"] = (x, y)
        if minsize: self.setMinSize(x, y)
        self["master"].geometry(str(x) + "x" + str(y))
    def setMaxSize(self, x, y):
        self["master"].maxsize(x, y)
    def setMinSize(self, x, y):
        self["master"].minsize(x, y)
    def quitMainLoop(self):
        self["master"].quit()
    def mainloop(self):
        self._mainloop()
    def _mainloop(self):
        if self["destroyed"]: return
        self._finishLastTasks()
        self["isRunning"] = True
        self["master"].mainloop()
        self["isRunning"] = False
        self["destroyed"] = True
    def _updateDynamicSize(self, widget):
        if not widget["destroyed"] and "xOffset" in widget["placeRelData"]:# and widget["id"] in list(self["dynamicWidgets"].keys()):
            widget._get().place_forget()
            self._get().update_idletasks()
            data = widget["placeRelData"]
            x = _map(data["xOffset"] + data["xOffsetLeft"], 0, 100, 0, widget["master"].getWidth()) if data["fixX"] is None else data["fixX"]
            y = _map(data["yOffset"] + data["yOffsetUp"], 0, 100, 0, widget["master"].getHeight()) if data["fixY"] is None else data["fixY"]

            width = ((widget["master"].getWidth() - _map(data["xOffset"] + data["xOffsetRight"], 0, 100, 0, widget["master"].getWidth()) - x) - (widget.data["yScrollbar"]["thickness"] if "yScrollbar" in list(widget.data.keys()) and widget.data["yScrollbar"]["autoPlace"] else 0) if data["fixWidth"] is None else data["fixWidth"])
            height = ((widget["master"].getHeight() - _map(data["yOffset"] + data["yOffsetDown"], 0, 100, 0, widget["master"].getHeight()) - y) - (widget.data["xScrollbar"]["thickness"] if "xScrollbar" in list(widget.data.keys()) and widget.data["xScrollbar"]["autoPlace"] else 0) if data["fixHeight"] is None else data["fixHeight"])
            if data["stickRight"]:
                x = widget["master"].getWidth()-width
            if data["stickDown"]:
                y = widget["master"].getHeight()-height
            if data["centerX"]:
                x = int(round(widget["master"].getWidth()/2 - width/2, 0))
            if data["centerY"]:
                y = int(round(widget["master"].getHeight()/2 - height/2, 0))

            width += data["changeWidth"]
            height += data["changeHeight"]

            x += data["changeX"]
            y += data["changeY"]

            widget["widget"].place(x=x,
                                 y=y,
                                 width=width,
                                 height=height,
                                 anchor=Anchor.UP_LEFT.value)

            if data["handler"] is not None:
                handler = data["handler"]
                for event in widget["registry"].getCallables("[relative_update]"):
                    event["value"] = [x, y, width, height]
                handler()

            if "xScrollbar" in list(widget.data.keys()) and widget.data["xScrollbar"]["autoPlace"]:
                widget.data["xScrollbar"].place(x, y + height, width=width)

            if "yScrollbar" in list(widget.data.keys()) and widget.data["yScrollbar"]["autoPlace"]:
                widget.data["yScrollbar"].place(x + width, y, height=height)

            if data["handler"] is not None:
                handler = data["handler"]
                for event in widget["registry"].getCallables("[relative_update_after]"):
                    event["value"] = [x, y, width, height]
                handler()
            widget._get().update_idletasks()
            widget["placed"] = True
    def updateDynamicWidgets(self):
        for widget in list(self["dynamicWidgets"].values()):
            if not widget["destroyed"]: self._updateDynamicSize(widget)
    def _internalOnClose(self):
        """
        internal onClose Event.
        @return:
        """
        print("Internal Close")
        if self["closeRunnable"] is None:
            self.destroy()
        else:
            runnable = self["closeRunnable"]
            runnable()
            if not runnable.event["setCanceled"]:
                self.destroy()


    def _registerOnResize(self, widget):
        self["dynamicWidgets"][widget["id"]] = widget
    def _unregisterOnResize(self, widget):
        if list(self["dynamicWidgets"].keys()).__contains__(widget["id"]):
            del self["dynamicWidgets"][widget["id"]]
    def _decryptWindowResize(self, args):
        _size = self.getWindowSize()
        if self["oldWinSize"] == _size:
            return "CANCEL"
        else:
            self["oldWinSize"] = _size
            return _size
    def _decryptNonFilteredWindowResize(self, args):
        return self.getWindowSize()
    def _privateDecryptWindowResize(self, args):
        _size = self.getWindowSize()
        if self["privateOldWinSize"] == _size:
            return "CANCEL"
        else:
            self["privateOldWinSize"] = _size
            return _size
    def _finishLastTasks(self):
        EventHandler._registerNewEvent(self, self.updateDynamicWidgets, EventType.key("<Configure>"), args=[], priority=1, decryptValueFunc=self._privateDecryptWindowResize)
        self.updateDynamicWidgets()
    def clearChildWidgets(self):
        """
        Clears the child-widgets.

        @return:
        """
        self.data["childWidgets"].clear()

    def addChildWidgets(self, *args):
        """
        Adds/Overwrites all Child widgets from this widget with new ones.

        @param args:
        @return:
        """
        for w in args:
            self.data["childWidgets"][w["id"]] = w

    def unregisterChildWidget(self, w):
        """
        Unregisters specific Child widget from this Master.

        @param w:
        @return:
        """
        del self["childWidgets"][w["id"]]

    def getID(self)->str:
        return self["id"]
    @staticmethod
    def _getAllChildWidgets(widget):
        """
        @TODO REMOVED widget gets added to its child wigets many wrong
        @param widget:
        @return:
        """
        ch = [] # [widget]
        def point(_widget):
            for cw in _widget["childWidgets"].values():
                ch.append(cw)
                point(cw)
        point(widget)
        return ch
    @staticmethod
    def _getAllParentWidgets(widget):
        ch = []

        while True:
            if isinstance(widget, Tk):
                break
            widget = widget["master"]
            ch.append(widget)

        return ch
    @staticmethod #TODO FINISH UFF
    def _showParentChildTree(widget):
        print("==Hierarchy==")
        def point(_widget):
            for cw in _widget["childWidgets"].values():
                #print("".join([("| " if not isinstance(cw, _tk_.Tk) and not isinstance(cw["master"], _tk_.Tk) and not isinstance(cw["master"]["master"], _tk_.Tk) and any([index == (len(Tk._getAllParentWidgets(cw))-2)]) and list(cw["master"]["master"]["childWidgets"].values()).index(cw["master"]) != len(list(cw["master"]["master"]["childWidgets"].values()))-1 else "  ") for index in range(len(Tk._getAllParentWidgets(cw))-1)]) + ("└" if len(_widget["childWidgets"].values())-1 == list(_widget["childWidgets"].values()).index(cw) else "├")+"─"+cw.__class__.__name__)
                print("".join([("| " if not isinstance(cw, _tk_.Tk) and not isinstance(cw["master"], _tk_.Tk) and not isinstance(cw["master"]["master"], _tk_.Tk) and any([index == (len(Tk._getAllParentWidgets(cw))-2)]) and list(cw["master"]["master"]["childWidgets"].values()).index(cw["master"]) != len(list(cw["master"]["master"]["childWidgets"].values()))-1 else "  ") for index in range(len(Tk._getAllParentWidgets(cw))-1)]) + ("" if len(_widget["childWidgets"].values())-1 == list(_widget["childWidgets"].values()).index(cw) else "")+""+cw.__class__.__name__)
                point(cw)
        print(widget.__class__.__name__)
        point(widget)
    def _get(self):
        return self["master"]
class Toplevel(Tk):
    """
    Toplevel window.
    Pass 'Tk' for _master to Use 'Toplevel' as 'Tk-class'.
    This is useful if your application can run standalone (Tk) and can be imported to run as a Toplevel window above another application.
    """
    def __init__(self, _master, group=None, topMost=True):
        if isinstance(_master, Tk):
            self.data = {"master": _tk_.Toplevel(), "tkMaster":_master, "registry":_EventRegistry(self), "setSize":(), "isRunning":False, "destroyed":False, "hasMenu":False, "childWidgets":{},"oldWinSize":(-1, -1), "privateOldWinSize":(-1, -1), "id":"".join([str(r.randint(0,9)) for _ in range(15)]), "dynamicWidgets":{}, "title":"", "closeRunnable":None}
            EventHandler._registerNewEvent(self, self.updateDynamicWidgets, EventType.key("<Configure>"), args=[], priority=1, decryptValueFunc=self._privateDecryptWindowResize)
            # configure internal onCloseEvent
            self["master"].protocol("WM_DELETE_WINDOW", self._internalOnClose)
        elif isinstance(_master, str) and _master == "Tk":
            self.data = {"master":_tk_.Tk(), "tkMaster":_master, "registry":_EventRegistry(self), "setSize":(),"isRunning":False, "destroyed":False, "hasMenu":False, "childWidgets":{},"oldWinSize":(-1, -1), "privateOldWinSize":(-1, -1),"id":"".join([str(r.randint(0, 9)) for _ in range(15)]), "dynamicWidgets":{}, "title":"", "closeRunnable":None}
            EventHandler._registerNewEvent(self, self.updateDynamicWidgets, EventType.key("<Configure>"), args=[],priority=1, decryptValueFunc=self._privateDecryptWindowResize)
            # configure internal onCloseEvent
            self["master"].protocol("WM_DELETE_WINDOW", self._internalOnClose)
        elif isinstance(_master, Toplevel):
            self.data = _master.data
        else:
            raise TKExceptions.InvalidWidgetTypeException("_master must be " + str(self.__class__.__name__) + " or Tk instance not: " + str(_master.__class__.__name__))
        super().__init__(self.data, group)
        if topMost: self.setAllwaysOnTop()
    def setTitle(self, title):
        self["title"] = title
        self["master"].title(title)
        return self
    def mainloop(self):
        if isinstance(self["master"], _tk_.Tk):
            self["master"].mainloop()
class Dialog(Toplevel):
    def __init__(self, _master, group=None, topMost=True):
        super().__init__(_master, group, topMost)
        self.hide()
        self._get().transient()
        self._get().grab_set()
    def show(self):
        self._get().grab_set()
        self["master"].deiconify()
    def hide(self):
        self._get().grab_release()
        self["master"].withdraw()

class Widget:
    def __init__(self, ins, data, group):
        self._ins = self if ins is None else ins
        self.disable = self.setDisabled
        self.enable = self.setEnabled
        if list(data.keys()).__contains__("id"): self.data = data
        else:
            data["tkMaster"] = data["master"] if isinstance(data["master"], Tk) else data["master"]["tkMaster"]
            id = "".join([str(r.randint(0,9)) for _ in range(15)])
            self.data = {**data, **{"widgetProperties":{},"childWidgets":{}, "id":id, "placed":True, "destroyed":False, "placeRelData":{"handler":None}, "registry":_EventRegistry(self), "group":group}}
            self.data["master"]["childWidgets"][self["id"]] = self._ins
            if list(data.keys()).__contains__("init"):
                for key, value in zip(data["init"].keys(), data["init"].values()):
                    if key == "func": value()
                    else: self._setAttribute(name=key, value=value)
                del data["init"]
        if group is not None:
            group.add(self._ins)
    def __getitem__(self, item):
        try:return self.data[item]
        except KeyError as e: raise KeyError("Item '"+str(item)+"' is not in dict of class '"+self["widget"].__class__.__name__+"'")
    def __setitem__(self, key, value):
        self.data[key] = value
    def __str__(self):
        return str(self.__class__.__name__)+"("+str(self.data)+")"
    def __eq__(self, other):
        if not hasattr(other, "data"): return False
        return self.data == other.data
    def __del__(self):
        print("__DELETE__", type(self))
        if self["group"] is not None:
            self["group"].remove(self._ins)
    def setTextOrientation(self, ori:Anchor=Anchor.LEFT):
        self._setAttribute("anchor", ori.value if hasattr(ori, "value") else ori)
        return self
    def attachToolTip(self, text:str, atext:str="", waitBeforeShow=.5):
        return ToolTip(self, atext != "", waitBeforeShow=waitBeforeShow).setText(text).setAdditionalText(atext)
    def setOrientation(self, ori:Orient):
        self._setAttribute("orient", ori.value if hasattr(ori, "value") else ori)
        return self
    def _setId(self, id_:str): #@TODO: why? maby error with event??
        self["id"] = str(id_)
    def _addData(self, data:dict):
        self.data = {**self.data, **data}
    def unbind(self, event:Union[EventType, Key, Mouse]):
        self["registry"].unregisterType(event)
    def setStyle(self, style:Style):
        self._setAttribute("relief", style.value if hasattr(style, "value") else style)
        return self
    def setBorderWidth(self, bd:int):
        self._setAttribute("bd", bd)
        return self
    def getHeight(self):
        self.updateIdleTasks()
        return self["widget"].winfo_height()
    def getWidth(self):
        self.updateIdleTasks()
        return self["widget"].winfo_width()
    def generateEvent(self, event:Union[EventType, Key, Mouse, str]):
        event = event.value if hasattr(event, "value") else event
        if event.startswith("["):
            raise NotImplemented("Trigger custom Events is not implemented yet!")
        self["widget"].event_generate(event)
    def setCompound(self, dir_:Direction):
        dir_ = dir_.value if hasattr(dir_, "value") else dir_
        self._setAttribute("compound", dir_)
        return self
    def lift(self, widg=None):
        if widg is not None:
            self["widget"].lift(widg._get())
        else:
            self["widget"].lift()
    def bind(self, func:Callable, event:Union[EventType, Key, Mouse, str], args:list=None, priority:int=0, defaultArgs=False, disableArgs=False):
        if event == "CANCEL": return
        if hasattr(event, "value"):
            event = event.value
        if event.startswith("["):
            EventHandler._registerNewCustomEvent(self, func, event, args, priority, defaultArgs=defaultArgs, disableArgs=disableArgs)
        else:
            EventHandler._registerNewEvent(self._ins, func, event, args, priority, defaultArgs=defaultArgs, disableArgs=disableArgs)
        return self
    def canTakeFocusByTab(self, b:bool=False):
        self._setAttribute("takefocus", int(b))
        return self
    def setCursor(self, c:Cursor):
        self["widget"]["cursor"] = c.value if hasattr(c, "value") else c
        return self
    def isFocus(self):
        return self["widget"].focus_get() == self._get()
    def setFocus(self):
        self["widget"].focus_set()
        return self
    def getPosition(self)->Location2D:#?
        return Location2D(self["widget"].winfo_x(), self["widget"].winfo_y())
    def getPositionToMaster(self)->Location2D:
        return Location2D(self["widget"].winfo_vrootx(), self["widget"].winfo_vrooty())
    def setDisabled(self):
        self._setAttribute("state", _tk_.DISABLED)
        return self
    def setEnabled(self):
        self._setAttribute("state", _tk_.NORMAL)
        return self
    def update(self):
        self["widget"].update()
        return self
    def updateIdleTasks(self):
        self["widget"].update_idletasks()
        return self
    def updateRelativePlace(self):
        self["tkMaster"]._updateDynamicSize(self)
        return self
    def setFont(self, size:int=10, art=FontType.ARIAL, underline=False, bold=False, slant=False, overstrike=False):
        data = {'family': art.value if hasattr(art, "value") else art,
                'size': size,                            # size
                'weight': 'bold' if slant else 'normal', # fett
                'slant': 'italic' if bold else'roman',   # kusiv
                'underline': bool(underline),            # unterstrichen
                'overstrike': bool(overstrike)}          # durchgestrichen

        self._setAttribute("font", _font.Font(**data))
        return self
    def setText(self, text):
        self._setAttribute("text", str(text))
        return self
    def getText(self):
        return self["widget"]["text"]
    def setBg(self, col:Union[Color, str]):
        self._setAttribute("bg", col.value if hasattr(col, "value") else col)
        return self
    def setFg(self, col:Union[Color, str]):
        self._setAttribute("fg", col.value if hasattr(col, "value") else col)
        return self
    def setActiveBg(self, col:Color):
        self._setAttribute("activebackground", col.value if hasattr(col, "value") else col)
        return self
    def setActiveFg(self, col:Color):
        self._setAttribute("activeforeground", col.value if hasattr(col, "value") else col)
        return self
    def placeForget(self):
        try:
            self["widget"].place_forget()
            self["placed"] = False
        except: pass
        self["tkMaster"]._unregisterOnResize(self)
    def grid(self, row=0, column=0):
        assert not self["destroyed"], "The widget has been destroyed and can no longer be placed."
        self["widget"].grid(row=row, column=column)
        return self
    def _placeRelative(self, fixX, fixY, fixWidth, fixHeight, xOffset, yOffset, xOffsetLeft, xOffsetRight, yOffsetUp, yOffsetDown, stickRight, stickDown, centerY, centerX, changeX, changeY, changeWidth, changeHeight, nextTo, updateOnResize):
        assert 100 >= xOffset + xOffsetLeft >= 0 and 100 >= xOffset + xOffsetRight >= 0, "xOffset must be a int Value between 0 and 100!"
        assert 100 >= yOffset + yOffsetUp >= 0 and 100 >= yOffset + yOffsetDown >= 0, "yOffset must be a int Value between 0 and 100!"
        self.data["placeRelData"] = {"handler":self["placeRelData"]["handler"],
                                     "xOffset":xOffset,
                                     "xOffsetLeft":xOffsetLeft,
                                     "xOffsetRight":xOffsetRight,
                                     "yOffset":yOffset,
                                     "yOffsetUp":yOffsetUp,
                                     "yOffsetDown":yOffsetDown,
                                     "fixX":fixX,
                                     "fixY":fixY,
                                     "fixWidth":fixWidth,
                                     "fixHeight":fixHeight,
                                     "stickRight":stickRight,
                                     "stickDown":stickDown,
                                     "centerX":centerX,
                                     "centerY":centerY,
                                     "nextTo":nextTo,
                                     "changeX":changeX,
                                     "changeY":changeY,
                                     "changeWidth":changeWidth,
                                     "changeHeight":changeHeight}
        self["tkMaster"]._updateDynamicSize(self)
        if updateOnResize:
            self["tkMaster"]._registerOnResize(self)
        return self
    def placeRelative(self, fixX=None, fixY=None, fixWidth=None, fixHeight=None, xOffset=0, yOffset=0, xOffsetLeft=0, xOffsetRight=0, yOffsetUp=0, yOffsetDown=0, stickRight=False, stickDown=False, centerY=False, centerX=False, changeX=0, changeY=0, changeWidth=0, changeHeight=0, nextTo=None, updateOnResize=True):
        self._placeRelative(fixX, fixY, fixWidth, fixHeight, xOffset, yOffset, xOffsetLeft, xOffsetRight, yOffsetUp, yOffsetDown, stickRight, stickDown, centerY, centerX, changeX, changeY, changeWidth, changeHeight, nextTo, updateOnResize)
        return self
    def _place(self, x, y, width, height, anchor):
        assert not self["destroyed"], "The widget has been destroyed and can no longer be placed."
        if x is None: x = 0
        if y is None: y = 0
        if hasattr(anchor, "value"):
            anchor = anchor.value
        if isinstance(x, Location2D):
            x, y = x.get()
        if isinstance(x, Rect):
            width = x.getWidth()
            height = x.getHeight()
            x, y, = x.getLoc1().get()
        x = int(round(x, 0))
        y = int(round(y, 0))
        self._get().place_forget()
        self["widget"].place(x=x, y=y, width=width, height=height, anchor=anchor)
        self["placed"] = True
        return self
    def place(self, x=None, y=None, width=None, height=None, anchor:Anchor=Anchor.UP_LEFT):
        """
        To override!
        @param x:
        @param y:
        @param width:
        @param height:
        @param anchor:
        @return:
        """
        self._place(x, y, width, height, anchor)
        return self
    def _destroy(self):
        assert not self["destroyed"], f"Widget {self.getType()} {self.getID()} is already destroyed!"
        self["registry"].unregisterAll()
        self["tkMaster"]._unregisterOnResize(self)
        if WIDGET_DELETE_DEBUG: print(type(self["master"]), "->", type(self))
        del self["master"]["childWidgets"][self["id"]] # unregister as child widget from master

        WidgetGroup.removeFromAll(self)
        if not isinstance(self, ToolTip): # -> Ignore Widget is None
            if not self["destroyed"]: self["widget"].destroy()
        self["destroyed"] = True
        self["placed"] = False
        for w in self["childWidgets"].copy().values():
            self["tkMaster"]._unregisterOnResize(w)
            w.destroy()
    def destroy(self):
        self._destroy()
        return self
    def getType(self):
        return type(self._ins)
    def applyTkOption(self, **kwargs):
        for k, v in zip(kwargs.keys(), kwargs.values()):
            self._setAttribute(k, v)
        return self

    def clearChildWidgets(self):
        """
        Clears the child-widgets.

        @return:
        """
        self.data["childWidgets"].clear()

    def addChildWidgets(self, *args):
        """
        Adds/Overwrites all Child widgets from this widget with new ones.

        @param args:
        @return:
        """
        for w in args:
            self.data["childWidgets"][w["id"]] = w

    def unregisterChildWidget(self, w):
        """
        Unregisters specific Child widget from this Master.

        @param w:
        @return:
        """
        del self["childWidgets"][w["id"]]

    def getID(self)->str:
        return self["id"]
    def _decryptEvent(self, args):
        pass
    def _id(self):
        return self["id"]
    def _register(self, e):
        self["master"].register(e)
    def _setAttribute(self, name, value):
        if self.data["tkMaster"]["destroyed"]: return
        self["widgetProperties"][name] = value
        try:
            self["widget"][name] = value
        except Exception as e:
            valType = type(value)
            value = value[0:50]+"..." if len(str(value)) > 50 else value
            raise AttributeError("Could not set Attribute of Widget "+str(type(self._ins))+"!\n\tKEY: '"+str(name)+"'\n\tVALUE["+str(valType)+"]: '"+str(value)+"'\n"+str(self._ins)+" \n\tTKError: "+str(e))
    def _getAllChildWidgets(self):
        return list(self["childWidgets"].values())
    def _get(self):
        return self["widget"]
class _WidgetGroupMethod:
    def __init__(self, _ins, name):
        self._ins = _ins
        self._name = name
    def __call__(self, *args, **kwargs):
        if self._ins._priorityData is not None:
            """
            There is an execution with settings only used once!
            """
            data = self._ins._priorityData.copy()
            self._ins._priorityData = None
        else:
            data = self._ins._data.copy()

        for i, w in enumerate(self._ins._widgets):
            if data["changeOnlyForType"] is not None and not isinstance(w, data["changeOnlyForType"]): continue
            try:
                out = getattr(w, self._name)(*args, **kwargs)
            except Exception as e:
                if data["ignoreErrors"]: continue
                raise Exception(f"Error while execute '{self._name}' command on [{len(self._ins._widgets)}].\nType: {type(w)}, Error: {e}")
class WidgetGroup:
    _GROUPS = []
    def __init__(self, type_=None):
        self._widgets = []
        self._commandsOnRegister = []
        self._data = {
            "ignoreErrors":False,
            "changeOnlyForType":None,
        }
        self._priorityData = None
        for method in dir(type_ if isinstance(type_, Widget) else Widget):
            if method.startswith("__"): continue
            setattr(self, method, _WidgetGroupMethod(self, method))
        WidgetGroup._GROUPS.append(self)
    def add(self, w):
        for method in dir(type(w)):
            if method.startswith("__"): continue
            if hasattr(self, method): continue
            setattr(self, method, _WidgetGroupMethod(self, method))
        self._widgets.append(w)
        self.reRunRegisteredCommands(w)
        if WIDGET_DELETE_DEBUG: TextColor.print(f"+{len(self._widgets)} {type(w)}", "green")

    def remove(self, widg):
        if widg in self._widgets:
            self._widgets.remove(widg)
            if WIDGET_DELETE_DEBUG: TextColor.print(f"-{len(self._widgets)} {type(widg)}", "red")
    def addCommand(self, function_name:str, *args, ignoreErrors=False, onlyFor=None):
        """
        args -> any Function of any Widget to run on this Widget.
        Gets executed on if Widget is created with this Group.

        set Function_name '@custom' for Custom change.
        Pass function with one Argument (for widget) to args!

        @param function_name:
        @param args:
        @param ignoreErrors:
        @param onlyFor:
        @return:
        """
        self._commandsOnRegister.append([function_name, args, ignoreErrors, onlyFor])
    def reRunRegisteredCommands(self, _w=None, ignoreAll=False):
        def _run(w):
            for cmd, args, igErr, olyF in self._commandsOnRegister:
                if cmd is None and igErr: continue
                if olyF is not None and type(w) != olyF: continue
                if ignoreAll: igErr = True
                try:
                    if cmd == "@custom":
                        args[0](w)
                    else:
                        getattr(w, cmd)(*args)
                except Exception as e:
                    if igErr: continue
                    raise Exception(f"Error while execute '{cmd}' command on [{len(self._widgets)}].\nType: {type(w)}, Error: {e}")
        if _w is None:
            for w in self._widgets: _run(w)
        else:
            _run(_w)
    def clearCommands(self):
        self._commandsOnRegister.clear()
    def setIgnoreErrors(self, b:bool):
        self._data["ignoreErrors"] = bool(b)
        return self
    def runWithSettings(self, ignoreErrors=False, changeOnlyForType=None):
        self._priorityData = {
            "ignoreErrors":ignoreErrors,
            "changeOnlyForType":changeOnlyForType,
        }
        return self

    @staticmethod
    def removeFromAll(widg):
        for group in WidgetGroup._GROUPS:
            group.remove(widg)

class ToolTip(Widget):
    """
    create a tooltip for a given widget
    """
    def __init__(self, _master, pressShiftForMoreInfo=False, waitBeforeShow=.5, group=None):
        if isinstance(_master, dict):
            self.data = _master
        elif isinstance(_master, self.__class__):
            self.data = _master.data
        elif isinstance(_master, Tk) or isinstance(_master, Widget):
            self.data = {"master": _master,
                         "disableTip":False,
                         "widget":None,
                         "init": {},
                         "text":"",
                         "atext":"",
                         "wait":waitBeforeShow,
                         "wrapLength":180,
                         "task":None,
                         "tip":None,
                         "tipLabel":None}
            self["master"].bind(self._enter, "<Enter>")
            self["master"].bind(self._leave, "<Leave>")
            self["master"].bind(self._leave, "<ButtonPress>")
            if pressShiftForMoreInfo: self["master"]["tkMaster"].bind(self._more, "<KeyRelease-Shift_L>", args=["release"])
            if pressShiftForMoreInfo: self["master"]["tkMaster"].bind(self._more, "<KeyPress-Shift_L>", args=["press"])
        else:
            raise TKExceptions.InvalidWidgetTypeException("_master must be " + str(self.__class__.__name__) + ", Frame or Tk instance not: " + str(_master.__class__.__name__))
        super().__init__(self, self.data, group)
    def setDisabled(self):
        self["disableTip"] = True
    def setEnabled(self):
        self["disableTip"] = False
    def setText(self, text):
        self["text"] = text
        return self
    def setAdditionalText(self, text):
        self["atext"] = text
        return self
    def _more(self, e):
        mode = e.getArgs(0)
        if self["tip"]:
            text = self["text"] if mode == "release" else self["atext"]
            self["tipLabel"].destroy()
            self["tipLabel"] = Label(self["tip"]).applyTkOption(text=text, justify='left', background="#ffffff", relief='solid', borderwidth=1, wraplength = self["wrapLength"])
            self["tipLabel"]._get().pack(ipadx=1)
    def _enter(self, e):
        self._schedule()
    def _leave(self, e):
        self._unschedule()
        self._hidetip()
    def _schedule(self):
        self._unschedule()
        self["task"] = TaskScheduler(self["master"], self["wait"], self._show).start()
    def _unschedule(self):
        task = self["task"]
        self["task"] = None
        if task: task.cancel()
    def _show(self):
        if self["disableTip"]:
            return
        x, y, cx, cy = self["master"]._get().bbox("insert")
        x += self["master"]._get().winfo_rootx() + 25
        y += self["master"]._get().winfo_rooty() + 20
        self._hidetip()
        self["tip"] = Toplevel(self["master"]["tkMaster"])
        self["tip"].overrideredirect()
        self["tip"].setPositionOnScreen(x, y)
        self["tipLabel"] = Label(self["tip"], ).applyTkOption(text=self["text"], justify='left', background="#ffffff", relief='solid', borderwidth=1, wraplength = self["wrapLength"])
        self["tipLabel"]._get().pack(ipadx=1)
    def _hidetip(self):
        pin = self["tip"]
        self["tip"] = None
        if pin is not None:
            pin.destroy()
class PDFViewer(Widget):
    def __init__(self, _master, path, group=None):
        from tkPDFViewer import tkPDFViewer as pdf
        if isinstance(_master, dict):
            self.data = _master
        elif isinstance(_master, self.__class__):
            self.data = _master.data
        elif isinstance(_master, Tk) or isinstance(_master, NotebookTab) or isinstance(_master, Canvas) or isinstance(_master, Frame) or isinstance(_master, LabelFrame):
            viewer = pdf.ShowPdf()
            self.data = {"master": _master, "widget": viewer.pdf_view(_master._get(), 200, 200, path), "init": {}}
        else:
            raise TKExceptions.InvalidWidgetTypeException("_master must be " + str(self.__class__.__name__) + ", Frame or Tk instance not: " + str(_master.__class__.__name__))
        super().__init__(self, self.data, group)

class Calendar(Widget):
    def __init__(self, _master, group=None):
        import tkcalendar as cal
        if isinstance(_master, dict):
            self.data = _master
        elif isinstance(_master, self.__class__):
            self.data = _master.data
        elif isinstance(_master, Tk) or isinstance(_master, NotebookTab) or isinstance(_master, Canvas) or isinstance(_master, Frame) or isinstance(_master, LabelFrame):
            self.data = {"master": _master, "widget": cal.Calendar(_master._get()), "init": {}}
        else:
            raise TKExceptions.InvalidWidgetTypeException("_master must be " + str(self.__class__.__name__) + ", Frame or Tk instance not: " + str(_master.__class__.__name__))
        super().__init__(self, self.data, group)
    def setDate(self, d, m, y):
        self._setAttribute("day", d)
        self._setAttribute("month", m)
        self._setAttribute("year", y)
        return self
    def _decryptEvent(self, args):
        return self["widget"].get_date()
    def setMaxDate(self, d, m, y):
        d = int(d)
        m = int(m)
        y = int(y)
        self._setAttribute("maxdate", date(y, m, d))
        return self
    def setMinDate(self, d, m, y):
        d = int(d)
        m = int(m)
        y = int(y)
        self._setAttribute("mindate", date(y, m, d))
        return self
    def getValue(self):
        return self["widget"].get_date()
    def onCalendarSelectEvent(self, func, args:list = None, priority:int=0, defaultArgs=False, disableArgs=False):
        EventHandler._registerNewEvent(self, func, EventType.customEvent("<<CalendarSelected>>"), args, priority, decryptValueFunc=self._decryptEvent, defaultArgs=defaultArgs, disableArgs=disableArgs)
class DropdownCalendar(Widget):
    def __init__(self, _master, group=None):
        import tkcalendar as cal
        if isinstance(_master, dict):
            self.data = _master
        elif isinstance(_master, self.__class__):
            self.data = _master.data
        elif isinstance(_master, Tk) or isinstance(_master, NotebookTab) or isinstance(_master, Canvas) or isinstance(_master, Frame) or isinstance(_master, LabelFrame):
            self.data = {"master": _master, "widget": cal.DateEntry(_master._get()), "init": {}}
        else:
            raise TKExceptions.InvalidWidgetTypeException("_master must be " + str(self.__class__.__name__) + ", Frame or Tk instance not: " + str(_master.__class__.__name__))
        super().__init__(self, self.data, group)
    def setDate(self, d, m, y):
        self._setAttribute("day", d)
        self._setAttribute("month", m)
        self._setAttribute("year", y)
        return self
    def _decryptEvent(self, args):
        return self["widget"].get_date()
    def setMaxDate(self, d, m, y):
        self._setAttribute("maxdate", date(y, m, d))
        return self
    def setMinDate(self, d, m, y):
        self._setAttribute("mindate", date(y, m, d))
        return self
    def getValue(self):
        return self["widget"].get_date()
    def onCalendarSelectEvent(self, func, args:list = None, priority:int=0, defaultArgs=False, disableArgs=False):
        EventHandler._registerNewEvent(self, func, EventType.customEvent("<<DateEntrySelected>>"), args, priority, decryptValueFunc=self._decryptEvent, defaultArgs=defaultArgs, disableArgs=disableArgs)
class ScrollBar(Widget):
    def __init__(self, _master, autoPlace=True, group=None):
        if isinstance(_master, dict):
            self.data = _master
        elif isinstance(_master, self.__class__):
            self.data = _master.data
        elif isinstance(_master, Tk) or isinstance(_master, NotebookTab) or isinstance(_master, Canvas) or isinstance(_master, Frame) or isinstance(_master, LabelFrame):
            self.data = {"master": _master, "widget": ttk.Scrollbar(_master._get()), "autoPlace":autoPlace, "thickness":18, "init": {}}
        else:
            raise TKExceptions.InvalidWidgetTypeException("_master must be " + str(self.__class__.__name__) + ", Frame or Tk instance not: " + str(_master.__class__.__name__))
        super().__init__(self, self.data, group)
    def callEventOnScrollbarRelease(self):
        self._setAttribute("jump", 1)
    def callEventOnScroll(self):
        self._setAttribute("jump", 0)
    def onScrollEvent(self, func, args:list = None, priority:int=0, defaultArgs=False, disableArgs=False):
        EventHandler._registerNewCommand(self, func, args, priority, decryptValueFunc=self._decryptEvent, defaultArgs=defaultArgs, disableArgs=disableArgs)
    def _decryptEvent(self, args):
        return None
    def setWidth(self, w:int):
        raise NotImplemented()
        self["widget"]["width"] = w
        self["thickness"] = w-10
        return self
class Frame(Widget):
    def __init__(self, _master, group=None):
        if isinstance(_master, dict):
            self.data = _master
        elif isinstance(_master, Tk) or isinstance(_master, NotebookTab) or isinstance(_master, Canvas) or isinstance(_master, Frame) or isinstance(_master, LabelFrame):
            self.data = {"master": _master,  "widget": _tk_.Frame(_master._get())}
        else:
            raise TKExceptions.InvalidWidgetTypeException("_master must be "+str(self.__class__.__name__)+", Frame or Tk instance not: "+str(_master.__class__.__name__))
        super().__init__(self, self.data, group)
    def __destroy(self):
        assert self["placed"], "Widget is already destroyed!"
        for id, widg in zip(self["childWidgets"].keys(), self["childWidgets"].values()):
            #EventHandler.unregisterAllEventsFormID(widg["id"])
            self["tkMaster"]._unregisterOnResize(widg)
        del self["master"]["childWidgets"][self["id"]]
        self["registry"].unregisterAll()
        self["tkMaster"]._unregisterOnResize(self)
        WidgetGroup.removeFromAll(self)
        self["widget"].destroy()
        self["destroyed"] = False
        self["placed"] = False
        for w in self["childWidgets"].copy().values():
            w.destroy()
class LabelFrame(Widget):
    def __init__(self, _master, group=None):
        if isinstance(_master, dict):
            self.data = _master

        elif isinstance(_master, Tk) or isinstance(_master, NotebookTab) or isinstance(_master, Canvas) or isinstance(_master, Frame) or isinstance(_master, LabelFrame):
            self.data = {"master": _master,  "widget": _tk_.LabelFrame(_master._get())}
        else:
            raise TKExceptions.InvalidWidgetTypeException("_master must be "+str(self.__class__.__name__)+", Frame or Tk instance not: "+str(_master.__class__.__name__))
        super().__init__(self, self.data, group)

    def __destroy(self):
        print("test2<-----")
        assert self["placed"], f"Widget is already destroyed! (LabelFrame)"
        for id, widg in zip(self["childWidgets"].keys(), self["childWidgets"].values()):
            # EventHandler.unregisterAllEventsFormID(widg["id"])
            self["tkMaster"]._unregisterOnResize(widg)
        del self["master"]["childWidgets"][self["id"]]
        self["registry"].unregisterAll()
        self["tkMaster"]._unregisterOnResize(self)
        WidgetGroup.removeFromAll(self)
        self["widget"].destroy()
        self["destroyed"] = False
        self["placed"] = False

        for w in self["childWidgets"].copy().values():
            w.destroy()
class Label(Widget):
    def __init__(self, _master, group=None, **kwargs):
        if isinstance(_master, dict):
            self.data = _master
        elif isinstance(_master, self.__class__):
            self.data = _master.data
        elif isinstance(_master, Tk) or isinstance(_master, NotebookTab) or isinstance(_master, Canvas) or isinstance(_master, Frame) or isinstance(_master, LabelFrame):
            self.data = {"master":_master,  "widget":_tk_.Label(_master._get()), "init":kwargs}
        else:
            raise TKExceptions.InvalidWidgetTypeException("_master must be "+str(self.__class__.__name__)+" or Tk instance not: "+str(_master.__class__.__name__))
        super().__init__(self, self.data, group)
    def clear(self):
        self.setText("")
        return self
    def setImage(self, img:Union[TkImage, PILImage]):
        self["widget"]._image = img._get()
        self["widget"]["image"] = self["widget"]._image
        return self
    def clearImage(self):
        self["widget"]["image"] = ''
        return self
class Checkbutton(Widget):
    CHECKED = True
    UNCHECKED = False
    def __init__(self, _master, group=None, defaultState:bool=UNCHECKED, text:str=""):
        self.getValue = self.getState
        self.setValue = self.setState
        if isinstance(_master, dict):
            self.data = _master
        elif isinstance(_master, self.__class__):
            self.data = _master.data
        elif isinstance(_master, _SubMenu):
            self.data = {"master": _master._master,  "widget": _tk_.Checkbutton(_master._master._get()), "instanceOfMenu":True}
            _master._widgets.append(["checkbutton", self])
        elif isinstance(_master, Tk) or isinstance(_master, NotebookTab) or isinstance(_master, Canvas) or isinstance(_master, Frame) or isinstance(_master, LabelFrame):
            intVar = _tk_.IntVar(_master._get())
            intVar.set(defaultState)
            self.data = {"master":_master, "text":text, "widget":_tk_.Checkbutton(_master._get()), "intVar":intVar, "init":{"text":text, "variable":intVar}}
        else:
            raise TKExceptions.InvalidWidgetTypeException("_master must be "+str(self.__class__.__name__)+", Frame or Tk instance not: "+str(_master.__class__.__name__))
        super().__init__(self, self.data, group)
    def __bool__(self):
        return bool(self.getState())
    def onSelectEvent(self, func, args:list = None, priority:int=0, defaultArgs=False, disableArgs=False):
        EventHandler._registerNewCommand(self, func, args, priority, decryptValueFunc=self._decryptEvent, defaultArgs=defaultArgs, disableArgs=disableArgs)
        return self
    def _decryptEvent(self, e):
        return self.getState()
    def toggle(self):
        self.setState(not self.getState())
        return self
    def setSelected(self):
        self.setState(True)
        return self
    def setState(self, b:bool):
        self["intVar"].set(bool(b))
        return self
    def getState(self):
        return self["intVar"].get()
    def setSelectColor(self, c:Color):
        self._setAttribute("selectcolor", c.value if hasattr(c, "value") else c)
        return self
class Radiobutton:
    def __init__(self, _master, group=None):
        self.getValue = self.getState
        if isinstance(_master, dict):
            self.data = _master
        elif isinstance(_master, self.__class__):
            self.data = _master.data
        elif isinstance(_master, Tk) or isinstance(_master, NotebookTab) or isinstance(_master, Canvas) or isinstance(_master, Frame) or isinstance(_master, LabelFrame):
            intVar = IntVar(_master)
            self.data = {"master": _master,  "widgets":[], "intVar":intVar, "eventArgs":[], "group":group}
        else:
            raise TKExceptions.InvalidWidgetTypeException("_master must be "+str(self.__class__.__name__)+", Frame or Tk instance not: "+str(_master.__class__.__name__))

    def __getitem__(self, item):
        return self.data[item]


    def getState(self):
        return self.data["intVar"].get()
    def setState(self, i:int):
        self.data["widgets"][i].setSelected()
        return self


    def createNewRadioButton(self, group=None):
        rb =_RadioButton(self.data["master"], self.data["intVar"], (group if group is not None else self["group"]))
        self.data["widgets"].append(rb)
        for i in self.data["eventArgs"]:
            EventHandler._registerNewCommand(rb, i["func"], i["args"], i["priority"], decryptValueFunc=rb._decryptEvent, defaultArgs=i["defaultArgs"], disableArgs=i["disableArgs"])
        return rb
    def onSelectEvent(self, func, args:list=None, priority:int=0, defaultArgs=False, disableArgs=False):
        self.data["eventArgs"].append({"func":func, "args":args , "priority":priority, "defaultArgs":defaultArgs, "disableArgs":disableArgs})
        for btn in self.data["widgets"]:
            EventHandler._registerNewCommand(btn, func, args, priority, decryptValueFunc=btn._decryptEvent, defaultArgs=defaultArgs, disableArgs=disableArgs)
        return self
class _RadioButton(Widget):
    def __init__(self, _master, intVar, group):
        self.data = {"master": _master, "widget": _tk_.Radiobutton(_master._get()), "intvar": intVar, "init": {"variable": intVar._get(), "value": intVar._add()}}
        super().__init__(self, self.data, group)
    def setSelected(self):
        self["intvar"].set(self["widget"]["value"])
        return self
    def getValue(self):
        return self["intvar"].get()
    def setSelectColor(self, c:Color):
        self._setAttribute("selectcolor", c.value if hasattr(c, "value") else c)
        return self
    def flash(self):
        self["widget"].flash()
        #changes serveral times between selected and bg color
        return self
    def _decryptEvent(self, args):
        return self.getText()
class Button(Widget):
    def __init__(self, _master, group=None, text="", canBePressedByReturn=True, fireOnlyOnce=True, fireInterval:float=0.1, firstDelay:float=0.5):
        if isinstance(_master, dict):
            self.data = _master
        elif isinstance(_master, self.__class__):
            self.data = _master.data
        elif isinstance(_master, Tk) or isinstance(_master, NotebookTab) or isinstance(_master, Canvas) or isinstance(_master, Frame) or isinstance(_master, LabelFrame):
            self.data = {"master":_master, "widget":_tk_.Button(_master._get()), "canBePressedByReturn":canBePressedByReturn, "instanceOfMenu":False, "init":{"text":text}}
            if not fireOnlyOnce:
                self.data["init"]["repeatdelay"] = int(firstDelay * 1000)
                self.data["init"]["repeatinterval"] = int(fireInterval * 1000)
        elif isinstance(_master, _SubMenu) or isinstance(_master, ContextMenu):
            group = None # not possible!
            if isinstance(_master, ContextMenu): _master = _master["mainSubMenu"]
            self.data = {"master":_master._master, "widget":_tk_.Button(_master._master._get()), "instanceOfMenu":True}
            _master._widgets.append(["command", self])
        else:
            raise TKExceptions.InvalidWidgetTypeException("_master must be "+str(self.__class__.__name__)+", Frame or Tk instance not: "+str(_master.__class__))
        super().__init__(self, self.data, group)
    def triggerButtonPress(self, normalRelief=True):
        if normalRelief: self.setStyle(Style.SUNKEN)
        self.update()
        self["registry"].getHandler("cmd")()
        if normalRelief: self.setStyle(Style.RAISED)
        self.update()
    def setStyleOnHover(self, style:Style):
        self._setAttribute("overrelief", style.value if hasattr(style, "value") else style)
        return self
    def flash(self):
        self["widget"].flash()
        #changes serveral times between selected and bg color
        return self
    def setCommand(self, cmd:Callable, args:list=None, priority:int=0, disableArgs=False, defaultArgs=False):
        if cmd is None: return self
        runnable = EventHandler._registerNewCommand(self, cmd, args, priority, disableArgs=disableArgs, defaultArgs=defaultArgs, onlyGetRunnable=self["instanceOfMenu"])
        if self["instanceOfMenu"]:
            self["widgetProperties"]["command"] = runnable
        elif self["canBePressedByReturn"]:
            EventHandler._registerNewEvent(self, cmd, EventType.key(Key.RETURN), args, priority=1, disableArgs=disableArgs, defaultArgs=defaultArgs)
        return self
    def setImage(self, img:Union[TkImage, PILImage]):
        self["widget"]._image = img._get()
        self["widget"]["image"] = self["widget"]._image
        return self
class OnOffButton(Widget):
    def __init__(self, _master, group=None, text="", default=False, colorsActive=True, reliefActive=False):
        if isinstance(_master, dict):
            self.data = _master
        elif isinstance(_master, self.__class__):
            self.data = _master.data
        elif isinstance(_master, Tk) or isinstance(_master, NotebookTab) or isinstance(_master, Canvas) or isinstance(_master, Frame) or isinstance(_master, LabelFrame):
            self.data = {"master":_master,  "text":text, "widget":_tk_.Button(_master._get()), "value":default, "relief":reliefActive, "color":colorsActive, "onText":None, "offText":None, "init":{"text":text}}
            if default:
                if colorsActive: self.data["init"]["bg"] = Color.GREEN.value
                if reliefActive: self.data["init"]["relief"] = Style.SUNKEN.value
            else:
                if colorsActive: self.data["init"]["bg"] = Color.RED.value
                if reliefActive: self.data["init"]["relief"] = Style.SUNKEN.value
        else:
            raise TKExceptions.InvalidWidgetTypeException("_master must be "+str(self.__class__.__name__)+", Frame or Tk instance not: "+str(_master.__class__.__name__))
        super().__init__(self, self.data, group)
    def setValue(self, v):
        self["value"] = bool(v)
        self._update()
        return self
    def getValue(self):
        return self["value"]
    def setOn(self):
        self["value"] = True
        self._update()
        return self
    def setOnText(self, text:str):
        self["onText"] = str(text)
        self._update()
        return self
    def setOffText(self, text:str):
        self["offText"] = str(text)
        return self
    def _press(self, e):
        self["value"] = not self["value"]
        self._update()
        func = self["command"]
        func["value"] = self["value"]
        if func is not None:
            func()
    def setCommand(self, cmd, args:list=None, priority:int=0, disableArgs=False, defaultArgs=False):
        self["command"] = EventHandler._getNewEventRunnable(self, cmd, args, priority)
        EventHandler._registerNewCommand(self, self._press, args, priority)
        self._update()
        return self
    def _update(self):
        if self["value"]:
            if self["onText"] is not None: self.setText(self["onText"])
            if self["color"]: self.setBg(Color.GREEN)
            if self["relief"]: self.setStyle(Style.SUNKEN)
        else:
            if self["offText"] is not None: self.setText(self["offText"])
            if self["color"]: self.setBg(Color.RED)
            if self["relief"]: self.setStyle(Style.RAISED)
        return self["value"]
class Entry(Widget):
    def __init__(self, _master, group=None):
        self.getValue = self.getText
        self.setValue = self.setText
        if isinstance(_master, dict):
            self.data = _master
        elif isinstance(_master, self.__class__):
            self.data = _master.data
        elif isinstance(_master, Tk) or isinstance(_master, NotebookTab) or isinstance(_master, Canvas) or isinstance(_master, Frame) or isinstance(_master, LabelFrame):
            self.data = {"master":_master,  "widget":_tk_.Entry(_master._get())}
        else:
            raise TKExceptions.InvalidWidgetTypeException("_master must be "+str(self.__class__.__name__)+", Frame or Tk instance not: "+str(_master.__class__.__name__))
        super().__init__(self, self.data, group)
    def attachHorizontalScrollBar(self, sc:ScrollBar):
        self["xScrollbar"] = sc
        sc["widget"]["orient"] = _tk_.HORIZONTAL
        sc["widget"]["command"] = self._scrollHandler
        self["widget"]["xscrollcommand"] = sc["widget"].set
    def setCursorBlinkDelay(self, d:float):
        self._setAttribute("insertofftime",  int(d * 1000))
        self._setAttribute("insertontime", int(d * 1000))
        return self
    def setCursorColor(self, c: Color):
        self._setAttribute("insertbackground", c.value if hasattr(c, "value") else c)
        return self
    def setCursorThickness(self, i: int):
        self._setAttribute("insertwidth", i)
        return self
    def setSelectForeGroundColor(self, c:Color):
        self._setAttribute("selectforeground", c.value if hasattr(c, "value") else c)
    def setSelectBackGroundColor(self, c:Color):
        self._setAttribute("selectbackground", c.value if hasattr(c, "value") else c)
    def onUserInputEvent(self, func, args:list=None, priority:int=0, defaultArgs=False, disableArgs=False):
        EventHandler._registerNewEvent(self, func, EventType.KEY_UP, args, priority, decryptValueFunc=self._decryptEvent, defaultArgs=defaultArgs, disableArgs=disableArgs)
        #_EventHandler.registerNewValidateCommand(self, func, [], "all", decryptValueFunc=self._decryptEvent, defaultArgs=defaultArgs, disableArgs=disableArgs)
        return self
    def hideCharactersWith(self, i:str="*"):
        self._setAttribute("show", str(i))
        return self
    def clear(self):
        self["widget"].delete(0, _tk_.END)
        return self
    def setText(self, text):
        self.clear()
        self["widget"].insert(0, str(text))
        return self
    def addText(self, text, index="end"):
        self["widget"].insert(index, str(text))
        return self
    def getText(self)->str:
        return self["widget"].get()
    def _decryptEvent(self, args):
        return args
    def _scrollHandler(self, *l):
        op, howMany = l[0], l[1]
        if op == 'scroll':
            units = l[2]
            self["widget"].xview_scroll(howMany, units)
        elif op == 'moveto':
            self["widget"].xview_moveto(howMany)
class TextEntry(LabelFrame):
    def __init__(self, _master, group=None, text=""):
        super().__init__(_master, group)

        if isinstance(_master, Tk) or isinstance(_master, NotebookTab) or isinstance(_master, Canvas) or isinstance(_master, Frame) or isinstance(_master, LabelFrame):
            data = {"value":"", "label":Label(self, group), "entry":Entry(self, group)}
            data["label"].setText(text)
            self._addData(data)
        else:
            raise TKExceptions.InvalidWidgetTypeException("_master must be "+str(self.__class__.__name__)+", Frame or Tk instance not: "+str(_master.__class__.__name__))

    def bind(self, func:callable, event: Union[EventType, Key, Mouse, str], args:list=None, priority:int=0, defaultArgs=False, disableArgs=False):
        if event == "CANCEL": return
        EventHandler._registerNewEvent(self, func, event, args, priority, defaultArgs=defaultArgs, disableArgs=disableArgs)
        return self
    def updatePlace(self):
        self.data["label"]._get().grid(row=0, column=0)
        self.data["entry"]._get().grid(row=0, column=1, sticky=Anchor.RIGHT.value)
    def getValue(self):
        return self.getEntry().getValue()
    def setValue(self, v):
        self.getEntry().clear()
        self.getEntry().setValue(str(v))
        return self
    def setText(self, text):
        self.getLabel().setText(text)
        return self
    def getEntry(self):
        return Entry(self["entry"])
    def getLabel(self):
        return Label(self["label"])
    def clear(self):
        self.getEntry().clear()
        return self
    def setDisabled(self):
        self.getEntry().setDisabled()
    def setEnabled(self):
        self.getEntry().setEnabled()
    def place(self, x=0, y=0, width=None, height=25, anchor=Anchor.UP_LEFT, entryStartX=None):
        offset = 5
        self._place(x, y, 200, height, anchor)
        self.data["label"].place(0, 0)
        labelWidth = self.data["label"].getWidth()
        if entryStartX is not None: labelWidth = entryStartX
        if width is None:
            width = labelWidth+100
            entryWidth = 100
        else:
            entryWidth = width - labelWidth
        self.data["label"].place(0, 0, labelWidth, height-offset)
        self.data["entry"].place(labelWidth, 0, entryWidth-offset, height-offset)
        self._place(x, y, width, height, anchor)
        return self
    def placeRelative(self, fixX=None, fixY=None, fixWidth=None, fixHeight=None, xOffset=0, yOffset=0, xOffsetLeft=0, xOffsetRight=0, yOffsetUp=0, yOffsetDown=0, stickRight=False, stickDown=False, centerY=False, centerX=False, changeX=0, changeY=0, changeWidth=0, changeHeight=0, nextTo=None, updateOnResize=True):
        raise NotImplemented("Text Entry: place relative is currently not implemented!")
        #return self

    def _get(self):
        return self["widget"]
class TextDropdownMenu(Widget):
    def __init__(self, _master, group=None, text=""):
        if isinstance(_master, dict):
            self.data = _master
        elif isinstance(_master, self.__class__):
            self.data = _master.data
        elif isinstance(_master, Tk) or isinstance(_master, NotebookTab) or isinstance(_master, Canvas) or isinstance(_master, Frame) or isinstance(_master, LabelFrame):
            widg = LabelFrame(_master)
            self.data = {"master":_master,  "widget":widg, "value":"", "dropdownMenu":DropdownMenu(widg), "label":Label(widg)}
            self.data["widget"]._get().grid(padx=10, pady=10)
            self.data["label"].setText(text)
            self.data["label"]._get().grid(row=0, column=0)
            self.data["dropdownMenu"]._get().grid(row=0, column=1)
        else:
            raise TKExceptions.InvalidWidgetTypeException("_master must be "+str(self.__class__.__name__)+", Frame or Tk instance not: "+str(_master.__class__.__name__))
        super().__init__(self, self.data, group)
    def bind(self, func, event: Union[EventType, Key, Mouse], args:list=None, priority:int=0, defaultArgs=False, disableArgs=False):
        if event == "CANCEL": return
        EventHandler._registerNewEvent(self, func, event, args, priority, defaultArgs=defaultArgs, disableArgs=disableArgs)
        return self
    def getValue(self):
        return self.getDropdownMenu().getValue()
    def setValue(self, v):
        self.getDropdownMenu().setValue(str(v))
    def getLabel(self):
        return Label(self["label"])
    def getDropdownMenu(self):
        return DropdownMenu(self["dropdownMenu"])
    def setDisabled(self):
        self.getDropdownMenu().setDisabled()
    def setEnabled(self):
        self.getDropdownMenu().setEnabled()
    def _get(self):
        return self["widget"]._get()
class Listbox(Widget):
    SINGLE = "single"
    MULTIPLE = "multiple"
    def __init__(self, _master, group=None, mode=SINGLE):
        if isinstance(_master, dict):
            self.data = _master
        elif isinstance(_master, self.__class__):
            self.data = _master.data
        elif isinstance(_master, Tk) or isinstance(_master, NotebookTab) or isinstance(_master, Canvas) or isinstance(_master, Frame) or isinstance(_master, LabelFrame):
            self.data = {"master":_master,  "widget":_tk_.Listbox(_master._get()), "selectionMode":mode, "init":{"selectmode":mode}, "default_color":Color.DEFAULT}
        else:
            raise TKExceptions.InvalidWidgetTypeException("_master must be "+str(self.__class__.__name__)+", Frame or Tk instance not: "+str(_master.__class__.__name__))
        super().__init__(self, self.data, group)
    def bindArrowKeys(self, widget=None, ifNoSelectionSelect0=True):
        def _up(e):
            if self["placed"]:
                selected = self.getSelectedIndex()
                if selected is None or selected == 0:
                    selected = -1
                    self.clearSelection()
                    if ifNoSelectionSelect0: self.setItemSelectedByIndex(0)
                else:
                    if selected > 0:
                        selected -= 1
                        self.setItemSelectedByIndex(selected)

                self.see(selected)
                self["widget"].event_generate("<<ListboxSelect>>")
        def _down(e):
            if self["placed"]:
                selected = self.getSelectedIndex()
                if selected is None:
                    selected = 0
                    if ifNoSelectionSelect0: self.setItemSelectedByIndex(0)
                else:
                    if selected < self.length():
                        selected += 1
                        self.setItemSelectedByIndex(selected)

                self.see(selected)
                self["widget"].event_generate("<<ListboxSelect>>")
        if widget is None: widget = self
        EventHandler._registerNewEvent(widget, _down, EventType.ARROW_DOWN, [], 0)
        EventHandler._registerNewEvent(widget, _up, EventType.ARROW_UP, [], 0)
    def see(self, index):
        self["widget"].see(index)
        return self
    def setSelectForeGroundColor(self, c: Color):
        self._setAttribute("selectforeground", c.value if hasattr(c, "value") else c)
    def setSelectBackGroundColor(self, c: Color):
        self._setAttribute("selectbackground", c.value if hasattr(c, "value") else c)
    def attachVerticalScrollBar(self, sc:ScrollBar):
        self["yScrollbar"] = sc
        sc["widget"]["orient"] = _tk_.VERTICAL
        sc["widget"]["command"] = self["widget"].yview
        self["widget"]["yscrollcommand"] = sc["widget"].set
        return self
    def clearSelection(self):
        self["widget"].selection_clear(0, "end")
    def setMultipleSelect(self):
        self._setAttribute("selectmode", "multiple")
        return self
    def setSingleSelect(self):
        self._setAttribute("selectmode", "single")
        return self
    def add(self, entry:str, index = "end", color:Union[Color, str]=None):
        self["widget"].insert(index, str(entry))

        color = color if color is not None else self["default_color"]

        if len(self.getAllSlots()) != 0:
            self.setSlotBg((self.length()-1 if index=="end" else index), color)
        return self
    def addAll(self, entry:[str], index="end", color:Union[Color, str]=None):
        color = color if color is not None else self["default_color"]
        if entry is None: return self
        if color == Color.WHITE:
            self["widget"].insert(index, *entry)

        else:
            for i in entry:
                self["widget"].insert(index, str(i))
                if len(self.getAllSlots()) != 0:
                    self.setSlotBg(self.length()-1, color)
                self.updateIdleTasks()
        return self
    def length(self):
        return self["widget"].size()
    def clear(self):
        self["widget"].delete(0, _tk_.END)
        return self
    def setSlotBgDefault(self, color:Color=Color.WHITE):
        """
        Sets the default color of new added Items.


        @param color:
        @return:
        """
        self["default_color"] = color.value if hasattr(color, "value") else color
        return self
    def setSlotBgAll(self, color:Color=Color.WHITE):
        for i in self.getAllSlotIndexes():
            self.setSlotBg(i, color)
        return self
    def setItemSelectedByIndex(self, index, clearFirst=True):
        if clearFirst: self["widget"].selection_clear(0, "end")
        self["widget"].select_set(index)
        #self["widget"].activate(index)
        return self
    def setItemSelectedByName(self, name, clearFirst=True):
        if clearFirst: self["widget"].selection_clear(0, "end")
        if name in self.getAllSlots():
            self.setItemSelectedByIndex(self.getAllSlots().index(name))
        return self
    def deleteItemByIndex(self, index):
        self["widget"].delete(index)
        return self
    def deleteItemByName(self, name):
        self.deleteItemByIndex(self.getAllSlots().index(name))
    def getIndexByName(self, item):
        return self.getAllSlots().index(item)
    def getNameByIndex(self, index):
        return self.getAllSlots()[index]
    def getSelectedIndex(self):
        if self["selectionMode"] == Listbox.SINGLE:
            if len(self["widget"].curselection()) == 0: return None
            return int(self["widget"].curselection()[0])
        else:
            return [int(i) for i in self["widget"].curselection()]
    def getSelectedItem(self):
        index = self.getSelectedIndex()
        if index is None: return None
        if type(index) == int:
            return self.getNameByIndex(index)
        else:
            return [self.getNameByIndex(i) for i in index]
    def setSlotBg(self, index, col:Color=Color.WHITE):
        self["widget"].itemconfig(index, bg=col.value if hasattr(col, "value") else col)
        return self
    def getAllSlotIndexes(self):
        return [i for i in range(self.length())]
    def getAllSlots(self):
        return [self["widget"].get(i) for i in range(self.length())]
    def onSelectEvent(self, func, args:list=None, priority:int=0, defaultArgs=False, disableArgs=False):
        EventHandler._registerNewEvent(self, func, EventType.LISTBOX_SELECT, args, priority, defaultArgs=defaultArgs, disableArgs=disableArgs, decryptValueFunc=self._decryptEvent)
    def _decryptEvent(self, args):
        try:
            w = args.widget
            if self["selectionMode"] == Listbox.SINGLE:
                return w.get(int(w.curselection()[0]))
            else:
                return [w.get(int(i)) for i in w.curselection()]
        except:
            return "CANCEL"
class Scale(Widget):
    def __init__(self, _master, from_=0, to=100, group=None, orient:Orient=Orient.HORIZONTAL):
        self.setResolution = self.setSteps
        if isinstance(_master, dict):
            self.data = _master
        elif isinstance(_master, self.__class__):
            self.data = _master.data
        elif isinstance(_master, Tk) or isinstance(_master, NotebookTab) or isinstance(_master, Canvas) or isinstance(_master, Frame) or isinstance(_master, LabelFrame):
            doubbleVar = _tk_.DoubleVar(_master._get())
            self.data = {"master":_master,  "widget":_tk_.Scale(_master._get()), "var":doubbleVar, "init":{"variable":doubbleVar, "from_":from_, "to":to, "orient":orient.value if hasattr(orient, "value") else orient}}
        else:
            raise TKExceptions.InvalidWidgetTypeException("_master must be "+str(self.__class__.__name__)+", Frame or Tk instance not: "+str(_master.__class__.__name__))
        super().__init__(self, self.data, group)
    def getValue(self):
        return self["var"].get()
    def setValue(self, v):
        self["var"].set(v)
        return self
    def getSlideLocation(self, value=None):
        if value is None: value = self.getValue()
        return Location2D(self["widget"].coords(value))
    def setIntervalIndicators(self, i:float=-1):
        self._setAttribute("tickinterval", i)
        return self
    def setSliderBg(self, color:Color):
        self._setAttribute("troughcolor", color.value if hasattr(color, "value") else color)
        return self
    def setText(self, text):
        self._setAttribute("label", str(text))
    def setValueVisible(self, b:bool=True):
        self._setAttribute("showvalue", b)
        return self
    def setSliderWidth(self, i:int=30):
        self._setAttribute("sliderlength", i)
        return self
    def setStyle(self, style:Style=Style.RAISED):
        self._setAttribute("sliderrelief", style.value if hasattr(style, "value") else style)
    def setSteps(self, s:Union[int, float]=1):
        self._setAttribute("resolution", s)
        return self
    def onScroll(self, func, args:list=None, priority:int=0):
        EventHandler._registerNewCommand(self, func, args, priority, decryptValueFunc=self._decryptValue)
        return self
    def _decryptValue(self, a=None):
        return self.getValue()
class Progressbar(Widget):
    def __init__(self, _master, group=None, values:int=100):
        if isinstance(_master, dict):
            self.data = _master
        elif isinstance(_master, self.__class__):
            self.data = _master.data
        elif isinstance(_master, Tk) or isinstance(_master, NotebookTab) or isinstance(_master, Canvas) or isinstance(_master, Frame) or isinstance(_master, LabelFrame):
            self.data = {"master":_master,  "widget":ttk.Progressbar(_master._get()), "values":values, "value":0}
        else:
            raise TKExceptions.InvalidWidgetTypeException("_master must be "+str(self.__class__.__name__)+", Frame or Tk instance not: "+str(_master.__class__.__name__))
        super().__init__(self, self.data, group)
    def setNormalMode(self):
        self["widget"].stop()
        self._setAttribute("mode", "determinate")
        return self
    def setAutomaticMode(self, delay=0.01):
        self._setAttribute("mode", "indeterminate")
        self["widget"].start(int(delay*1000))
        return self
    def iter(self, reset=True):
        if reset:
            v = self["values"]
            self.reset()
        else:
            v = self["values"] - self["value"]
        for i in range(v):
            self.addValue()
            yield i
    def setOrient(self, o:Orient):
        self._setAttribute("orient", o.value if hasattr(o, "value") else o)
        return self
    def setValues(self, val):
        self["values"] = int(val)
    def update(self):
        self._setAttribute("value", int((self["value"] / self["values"]) * 100))
        self["widget"].update()
    def addValue(self, v=1):
        if self["values"] >= self["value"]+v:
            self["value"] += v
            self._setAttribute("value", int((self["value"] / self["values"]) * 100))
    def isFull(self):
        return self["values"] <= self["value"]
    def reset(self):
        """
        Sets the bar progress to 0.

        @return:
        """
        self._setAttribute("value", 0)
        self["value"] = 0
    def setValue(self, v):
        if self["values"] >= v:
            self["value"] = v
            self._setAttribute("value", int((self["value"] / self["values"]) * 100))
    def setPercentage(self, p):
        if str(p).startswith("0."):
            p *= 100
        self._setAttribute("value", p)
        self["value"] = p / 100 * self["values"]
class _ScrolledText(_tk_.Text):
    """
    Pivate implenetation of tkinter.scrolledtext.ScrolledText

    use ttk.Scrollbar

    """
    def __init__(self, master=None, **kw):
        self.frame = _tk_.Frame(master)
        self.vbar = ttk.Scrollbar(self.frame)
        self.vbar.pack(side=_tk_.RIGHT, fill=_tk_.Y)

        kw.update({'yscrollcommand': self.vbar.set})
        _tk_.Text.__init__(self, self.frame, **kw)
        self.pack(side=_tk_.LEFT, fill=_tk_.BOTH, expand=True)
        self.vbar['command'] = self.yview

        # Copy geometry methods of self.frame without overriding Text
        # methods -- hack!
        text_meths = vars(Text).keys()
        methods = vars(_tk_.Pack).keys() | vars(_tk_.Grid).keys() | vars(_tk_.Place).keys()
        methods = methods.difference(text_meths)

        for m in methods:
            if m[0] != '_' and m != 'config' and m != 'configure':
                setattr(self, m, getattr(self.frame, m))

    def __str__(self):
        return str(self.frame)
class Text(Widget):
    def __init__(self, _master, group=None, readOnly=False, forceScroll=False, scrollAble=False):
        self.getContent = self.getText
        if isinstance(_master, dict):
            self.data = _master
        elif isinstance(_master, self.__class__):
            self.data = _master.data
        elif isinstance(_master, Tk) or isinstance(_master, NotebookTab) or isinstance(_master, Canvas) or isinstance(_master, Frame) or isinstance(_master, LabelFrame):
            self.data = {"master": _master,  "widget": _ScrolledText(_master._get()) if scrollAble else _tk_.Text(_master._get()), "forceScroll":forceScroll, "tagCounter":0, "scrollable":scrollAble, "init":{"state":"disabled" if readOnly else "normal"}}
        else:
            raise TKExceptions.InvalidWidgetTypeException("_master must be "+str(self.__class__.__name__)+", Frame or Tk instance not: "+str(_master.__class__.__name__))
        super().__init__(self, self.data, group)
    def addLine(self, text, color="black"):
        if not text.endswith("\n"): text = text+"\n"
        self.addText(text, color)
        return self
    def addLineWithTimeStamp(self, text, color="black"):
        if not text.endswith("\n"): text = text+"\n"
        self.addText(t.strftime("[%H:%M:%S]: ")+text, color)
        return self
    def addStrf(self, text):
        """
        §D: DEFAULT
        §W: WHITE
        §B: BLACK

        §r: RED
        §g: GREEN
        §b: BLUE
        §c: CYAN
        §y: YELLOW
        §m: MAGENTA

        §rgb(r, g, b)

        @param text:
        @return:
        """

        colors = {'D':Color.DEFAULT,
                  'W':Color.WHITE,
                  'B':Color.BLACK,
                  'r':Color.RED,
                  'g':Color.GREEN,
                  'b':Color.BLUE,
                  'c':Color.CYAN,
                  'y':Color.YELLOW,
                  'm':Color.MAGENTA,
                  'o':Color.ORANGE}

        """
        Copying ... items from §bBilder§B to §bDesktop
                               | 24    | 29  | 33
        """

        _text = text
        print(text)
        for i in ['§D', '§W', '§B', '§r', '§g', '§b', '§c', '§y', '§m', '§o']:
            _text = _text.replace(i, "")
        content = self.getText()
        self.addText(_text)  # text without colorsmarkers
        line = _line = content.count("\n")  # 1
        firstMarkerChar = len(content.split("\n")[-1]) + len(text.split("§")[0])  # TODO prüfen wenn text nicht mit tag beginnt
        for i, textSection in enumerate(text.split("§")[1:]):
            firstMarker = str(line) + "." + str(firstMarkerChar)
            line += textSection.count("\n")
            if _line != line:  # clear fist marker at line change
                firstMarkerChar = 0
                _line = line
            if textSection.count("\n") > 0:  # section -> mehrere zeilen
                _textSectionLastLength = len(textSection.split("\n")[-1])  # section enthält keine Farbe
            else:
                _textSectionLastLength = len(textSection.split("\n")[-1]) - 1  # section nur 1 zeile (dann farbe entfernen)
            secondMarker = str(line) + "." + str(firstMarkerChar + _textSectionLastLength)
            if textSection[0] in colors.keys():  # check if tag is a valid color
                _id = "".join([r.choice(string.ascii_lowercase) for _ in range(30)])
                self["widget"].tag_add(_id, firstMarker, secondMarker)
                self["widget"].tag_config(_id, foreground=colors[textSection[0]].value)
            else:
                print(f"'{textSection}' has no valid color tag.")
            firstMarkerChar = int(secondMarker.split(".")[1])  # += len(textSection.split("\n")[-1])-1


    def setText(self, text):
        self.clear()
        self.addText(text)
        return self


    def addText(self, text, color="black"):
        color = color.value if hasattr(color, "value") else color
        disableAfterWrite=False
        #if text.endswith("\n"):
            #text = text[0:-1]
        self["tagCounter"]+=1
        if self["widgetProperties"]["state"] == "disabled":
            self.setEnabled()
            disableAfterWrite = True
        self["widget"].insert("end", str(text)) # changed: removed /n
        if color != "black":
            self["widget"].tag_add(str(self["tagCounter"]), str(self["tagCounter"])+".0", "end")
            self["widget"].tag_config(str(self["tagCounter"]), foreground=color)
        if self["forceScroll"]:
            self["widget"].see("end")
        self["tagCounter"]+=text.count("\n")
        if disableAfterWrite:
            self.setDisabled()
        return self
    def addTextFromFile(self, path, clearFirst=True):
        if os.path.exists(path):
            if clearFirst: self.clear()
            file = open(path, "r")
            for line in file:
                self.addText(line)
            file.close()
        else:
            TKExceptions.PathNotExisits("Cannot pull content from this file: "+path)
    def getText(self)->str:
        return self["widget"].get(0.0, "end")
    def scrollDown(self):
        self["widget"].see("end")
        return self
    def clear(self):
        disableAfterWrite = False
        if self["widgetProperties"]["state"] == "disabled":
            self.setEnabled()
            disableAfterWrite = True
        self["widget"].delete(0.0, _tk_.END)
        for i in self["widget"].tag_names():
            self["widget"].tag_delete(i)
        self["tagCounter"] = 0
        if disableAfterWrite:
            self.setDisabled()
        return self
    def getSelectedText(self):
        try:
            return self["widget"].get("sel.first", "sel.last")
        except _tk_.TclError:
            return None
    def onUserInputEvent(self, func, args:list=None, priority:int=0, defaultArgs=False, disableArgs=False):
        EventHandler._registerNewEvent(self, func, EventType.KEY_UP, args, priority, decryptValueFunc=self._decryptEvent, defaultArgs=defaultArgs, disableArgs=disableArgs)
        #_EventHandler.registerNewValidateCommand(self, func, [], "all", decryptValueFunc=self._decryptEvent, defaultArgs=defaultArgs, disableArgs=disableArgs)
    def setSelectForeGroundColor(self, c:Color):
        self._setAttribute("selectforeground", c.value if hasattr(c, "value") else c)
    def setSelectBackGroundColor(self, c:Color):
        self._setAttribute("selectbackground", c.value if hasattr(c, "value") else c)
    def setCursorColor(self, c:Color):
        self._setAttribute("insertbackground", c.value if hasattr(c, "value") else c)
        return self
    def setCursorThickness(self, i:int):
        self._setAttribute("insertwidth", i)
        return self
    def setCursorBlinkDelay(self, d:float):
        self._setAttribute("insertofftime",  int(d * 1000))
        self._setAttribute("insertontime", int(d * 1000))
        return self
    def setUndo(self, b:bool, maxUndo=-1):
        self._setAttribute("undo", int(b))
        self._setAttribute("maxundo", maxUndo)
        return self
    def setWrapping(self, w:Wrap):
        self._setAttribute("wrap", w.value if hasattr(w, "value") else w)
        return self
    def _decryptEvent(self, args):
        return self.getText()
class _SubFolder:
    def __init__(self, parent, data):
        self._parent = parent
        self.data = data
    def __getitem__(self, item):
        return self.data[item]
    def __setitem__(self, key, value):
        self.data[key] = value
    def addEntry(self, *args, index="end"):
        if isinstance(args[0], tuple) or isinstance(args[0], list):
            args = args[0]
        if len(self["headers"]) == 0:
            raise TKExceptions.InvalidHeaderException("Set Tree Headers first!")
        if len(self["headers"]) != len(list(args)):
            raise TKExceptions.InvalidHeaderException("Length of headers must be the same as args of addEntry!")
        self["widget"].insert(parent=self._parent, index=index, text=args[0], values=args[1:])
    def createFolder(self, *args, index="end"):
        if isinstance(args[0], tuple) or isinstance(args[0], list):
            args = args[0]
        if len(self["headers"]) == 0:
            raise TKExceptions.InvalidHeaderException("Set Tree Headers first!")
        if len(self["headers"]) != len(list(args)):
            raise TKExceptions.InvalidHeaderException("Length of headers must be the same as args of addEntry!")
        parent = self["widget"].insert(parent=self._parent, index=index, text=args[0], values=args[1:])
        return _SubFolder(parent, self.data)
class TreeViewElement:
    def __init__(self, tv, _id=None):
        if isinstance(tv, TreeView):
            self.data = {"master":tv, "id":_id}
        elif isinstance(tv, TreeViewElement):
            self.data = tv.data
        else:
            raise TKExceptions.InvalidWidgetTypeException("_master must be TreeViewElement instance not: " + str(tv.__class__.__name__))

    #def __lt__(self, other):
        #return 1 < other.score
    def setFont(self):
        pass
    def setImage(self):
        pass
    def setFg(self):
        pass
    def getIndex(self):
        pass
    def getKeys(self):
        pass
    def getValues(self):
        pass
class TreeView(Widget):
    """TODO
    tag_configure:
        font, image, foreground


    """
    def __init__(self, _master, group=None):
        if isinstance(_master, dict):
            self.data = _master
        elif isinstance(_master, self.__class__):
            self.data = _master.data
        elif isinstance(_master, Tk) or isinstance(_master, NotebookTab) or isinstance(_master, Canvas) or isinstance(_master, Frame) or isinstance(_master, LabelFrame):
            self.data = {"master": _master,  "widget":ttk.Treeview(_master._get()), "headers":[], "elements":[]}
        else:
            raise TKExceptions.InvalidWidgetTypeException("_master must be "+str(self.__class__.__name__)+", Frame or Tk instance not: "+str(_master.__class__.__name__))
        super().__init__(self, self.data, group)
    def onDoubleSelectEvent(self, func, args:list=None, priority:int=0, defaultArgs=False, disableArgs=False):
        EventHandler._registerNewEvent(self, func, Mouse.DOUBBLE_LEFT, args, priority, defaultArgs=defaultArgs, disableArgs=disableArgs, decryptValueFunc=self._decryptEvent)
    def onSingleSelectEvent(self, func, args:list=None, priority:int=0, defaultArgs=False, disableArgs=False):
        EventHandler._registerNewEvent(self, func, Mouse.LEFT_CLICK_RELEASE, args, priority, defaultArgs=defaultArgs, disableArgs=disableArgs, decryptValueFunc=self.__decryptEvent)
    def onArrowKeySelectEvent(self, func, args:list=None, priority:int=0, defaultArgs=False, disableArgs=False, bindToOtherWidget=None):
        widget = self
        if bindToOtherWidget is not None:
            widget = bindToOtherWidget

        EventHandler._registerNewEvent(widget, func, EventType.KEY_UP + EventType.ARROW_UP, args, priority, defaultArgs=defaultArgs, disableArgs=disableArgs, decryptValueFunc=self.__decryptEvent)
        EventHandler._registerNewEvent(widget, func, EventType.KEY_UP + EventType.ARROW_DOWN, args, priority, defaultArgs=defaultArgs, disableArgs=disableArgs, decryptValueFunc=self.__decryptEvent)
    def attachVerticalScrollBar(self, sc: ScrollBar):
        self["yScrollbar"] = sc
        sc["widget"]["orient"] = _tk_.VERTICAL
        sc["widget"]["command"] = self["widget"].yview
        self["widget"]["yscrollcommand"] = sc["widget"].set
        return self
    def _decryptEvent(self, args):
        ids = self["widget"].selection()
        if len(ids) == 0: return None
        #if id_ == "": return None
        items = []
        for id_ in ids:
            item = self["widget"].item(id_)
            a = {self["headers"][0]:item["text"]}
            for i, h in enumerate(self["headers"][1:]): a[h] = item["values"][i]
            items.append(a)
        return items
    def __decryptEvent(self, args):
        self["tkMaster"].updateIdleTasks()

        ids = self["widget"].selection()

        if len(ids) == 0: return None
        #if id_ == "": return None
        items = []
        for id_ in ids:
            item = self["widget"].item(id_)
            a = {self["headers"][0]:item["text"]}
            for i, h in enumerate(self["headers"][1:]): a[h] = item["values"][i]
            items.append(a)
        return items
    def _getDataFromId(self, id_):
        item = self["widget"].item(id_)
        a = {self["headers"][0]:item["text"]}
        for i, h in enumerate(self["headers"][1:]): a[h] = item["values"][i]
        return a
    def getSelectedItems(self)->list:
        return self._decryptEvent(None)
    def clear(self):
        if self.length() == 0: return self
        self["widget"].delete(*self["widget"].get_children())
        self["elements"] = []
        return self
    def setTableHeaders(self, *args):
        if isinstance(args[0], tuple) or isinstance(args[0], list):
            args = args[0]
        self["headers"] = [str(i) for i in args]
        self._setAttribute("columns", self["headers"][1:])
        self["widget"].column("#0", stretch=False)
        self["widget"].heading("#0", text=self["headers"][0], anchor="w")
        for i in self["headers"][1:]:
            self["widget"].column(i, stretch=False)
            self["widget"].heading(i, text=i, anchor="w")
    def addEntry(self, *args, index="end", image=None):
        if isinstance(image, TkImage) or isinstance(image, PILImage):
            image = image._get()
        if isinstance(args[0], tuple) or isinstance(args[0], list):
            args = args[0]
        if len(self["headers"]) == 0:
            raise TKExceptions.InvalidHeaderException("Set Tree Headers first!")
        if len(self["headers"]) != len(list(args)):
            raise TKExceptions.InvalidHeaderException("Length of headers must be the same as args of addEntry!")
        if image is not None: _id = self["widget"].insert(parent="", index=index, text=args[0], values=args[1:], image=image)
        else: _id = self["widget"].insert(parent="", index=index, text=args[0], values=args[1:])
        entry = TreeViewElement(self, _id)
        self["elements"].append(entry)
        return self
    def createFolder(self, *args, index="end"):
        if isinstance(args[0], tuple) or isinstance(args[0], list):
            args = args[0]
        if len(self["headers"]) == 0:
            raise TKExceptions.InvalidHeaderException("Set Tree Headers first!")
        if len(self["headers"]) != len(list(args)):
            raise TKExceptions.InvalidHeaderException("Length of headers must be the same as args of addEntry!")
        parent = self["widget"].insert(parent="", index=index, text=args[0], values=args[1:])
        return _SubFolder(parent, self.data)
    def setNoSelectMode(self):
        self._setAttribute("selectmode", "none")
        return self
    def setMultipleSelect(self):
        self._setAttribute("selectmode", "extended")
        return self
    def setSingleSelect(self):
        self._setAttribute("selectmode", "browse")
        return self
    def clearSelection(self):
        for item in self["widget"].selection():
            self["widget"].selection_remove(item)
        return self
    def see(self, index):
        self["widget"].see(self._getIds()[index])
        return self
    #TODO add length from subFolders!
    def length(self):
        return len(self._getIds())
    #TODO test after resorting items -> _getIds correct?
    def setItemSelectedByIndex(self, index:int, clearFirst=True):
        assert index < len(self._getIds()), "index is too large: \n\tListbox_length: "+str(len(self._getIds()))+"\n\tIndex: "+str(index)
        if clearFirst: self["widget"].selection_set(self._getIds()[index])
        else: self["widget"].selection_add(self._getIds()[index])
        return self
    """
    def setItemSelectedByName(self, name, clearFirst=True):
        if clearFirst: self["widget"].selection_clear(0, "end")
        if name in self.getAllSlots():
            self.setItemSelectedByIndex(self.getAllSlots().index(name))
        return self
    """
    def getSize(self):
        return len(self._getIds())
    def deleteItemByIndex(self, index):
        self["widget"].delete(self._getIds()[index])
        return self
    def getIndexByName(self, item):
        return self.getAllSlots().index(item)
    def getDataByIndex(self, index)->dict:
        return self._getDataFromId(self._getIds()[index])
    def getSelectedIndex(self):
        if self["widgetProperties"]["selectmode"] == "browse":
            if len(self["widget"].curselection()) == 0: return -1
            return self._getIds().index(self["widget"].selection()[0])
        else:
            ids = self._getIds()
            return [ids.index(i) for i in self["widget"].selection()]
    def getAllSlotIndexes(self):
        return [i for i in range(self.length())]
    def getAllSlots(self):
        return [self["widget"].item(i) for i in self._getIds()]
    def _getIds(self):
        return self["widget"].get_children()
class SpinBox(Widget):
    def __init__(self, _master, group=None, optionList:list=(), readOnly=True):
        if isinstance(_master, dict):
            self.data = _master
        elif isinstance(_master, self.__class__):
            self.data = _master.data
        elif isinstance(_master, Tk) or isinstance(_master, NotebookTab) or isinstance(_master, Canvas) or isinstance(_master, Frame):
            self.data = {"master": _master,  "widget": _tk_.Spinbox(_master._get()), "readonly":readOnly, "init":{"state":"readonly" if readOnly else "normal", "values":list(optionList)}}
        else:
            raise TKExceptions.InvalidWidgetTypeException("_master must be " + str(self.__class__.__name__) + ", Frame or Tk instance not: " + str(_master.__class__.__name__))
        super().__init__(self, self.data, group)
    def onButtonClick(self, func, args:list=None, priority:int=0, defaultArgs=False, disableArgs=False):
        EventHandler._registerNewCommand(self, func, args, priority, defaultArgs=defaultArgs, disableArgs=disableArgs, decryptValueFunc=self._decryptEvent)
    def onUserInputEvent(self, func, args:list=None, priority:int=0, defaultArgs=False, disableArgs=False):
        EventHandler._registerNewEvent(self, func, EventType.KEY_UP, args, priority, decryptValueFunc=self._decryptEvent, defaultArgs=defaultArgs, disableArgs=disableArgs)
    def setValue(self, v, clearFirst=True):
        disableAfterWrite = False
        if self["readonly"]:
            disableAfterWrite = True
            self.setEnabled()
        if clearFirst: self.clear()
        self["widget"].insert(0, str(v))
        if disableAfterWrite:
            self._setAttribute("state", "readonly")
        return self
    def getValue(self)->str:
        return self["widget"].get()
    def setOptionList(self, l:list):
        disableAfterWrite = False
        if self["readonly"]:
            disableAfterWrite = True
            self.setEnabled()
        self._setAttribute("values", l)
        if disableAfterWrite:
            self._setAttribute("state", "readonly")
    def clear(self):
        self["widget"].delete(0, "end")
    def setButtonStyle(self, style:Style):
        self._setAttribute("buttondownrelief", style.value if hasattr(style, "value") else style) #wtf
        self._setAttribute("buttonup", style.value if hasattr(style, "value") else style)
        return self
    def setButtonBackground(self, color:Color):
        self._setAttribute("buttonbackground", color.value if hasattr(color, "value") else color)
        return self
    def setButtonCursor(self, cursor:Cursor):
        self._setAttribute("buttoncursor", cursor.value if hasattr(cursor, "value") else cursor)
        return self
    def setCursorColor(self, c:Color):
        self._setAttribute("insertbackground", c.value if hasattr(c, "value") else c)
        return self
    def setCursorThickness(self, i:int):
        self._setAttribute("insertwidth", i)
        return self
    def setCursorBlinkDelay(self, d:float):
        self._setAttribute("insertofftime",  int(d * 1000))
        self._setAttribute("insertontime", int(d * 1000))
        return self
    def _decryptEvent(self, args):
        return self.getValue()
class DropdownMenu(Widget):
    def __init__(self, _master, group=None, optionList:list=(), readonly=True):
        if isinstance(_master, dict):
            self.data = _master
        elif isinstance(_master, self.__class__):
            self.data = _master.data
        elif isinstance(_master, Tk) or isinstance(_master, NotebookTab) or isinstance(_master, Canvas) or isinstance(_master, Frame) or isinstance(_master, LabelFrame):
            stringVar = _tk_.StringVar()
            self.data = {"master": _master,  "widget":ttk.Combobox(_master._get(), textvariable=stringVar), "values":optionList, "stringVar":stringVar, "readonly":readonly, "init":{"state":"readonly" if readonly else "normal", "values":list(optionList)}}
            self.style= ttk.Style()
            #self.style.theme_use("clam")

        else:
            raise TKExceptions.InvalidWidgetTypeException("_master must be "+str(self.__class__.__name__)+", Frame or Tk instance not: "+str(_master.__class__.__name__))
        super().__init__(self, self.data, group)
    def setReadOnly(self, b=True):
        self["readonly"] = b
        self._setAttribute("state", "readonly")
        return self
    def setEnabled(self, e=False):
        if self["readonly"] and not e:
            self._setAttribute("state", "readonly")
        else:
            self._setAttribute("state", "normal")
        return self
    def onSelectEvent(self, func, args:list=None, priority:int=0, defaultArgs=False, disableArgs=False):
        EventHandler._registerNewEvent(self, func, EventType.COMBOBOX_SELECT, args, priority, defaultArgs=defaultArgs, disableArgs=disableArgs, decryptValueFunc=self._decryptEvent)
        return self
    def onDropdownExpand(self, func, args:list=None, priority:int=0, defaultArgs=False, disableArgs=False):
        EventHandler._registerNewCommand(self, func, args, priority, defaultArgs=defaultArgs, disableArgs=disableArgs, cmd="postcommand")
        return self
    def onUserInputEvent(self, func, args:list=None, priority:int=0, defaultArgs=False, disableArgs=False):
        EventHandler._registerNewValidateCommand(self, func, args, priority, "all", decryptValueFunc=self._decryptEvent2, defaultArgs=defaultArgs, disableArgs=disableArgs)
        return self
    def setValueByIndex(self, i:int):
        disableAfterWrite = False
        if self["readonly"]:
            disableAfterWrite = True
            self.setEnabled(True)
        self["widget"].current(i)
        if disableAfterWrite:
            self._setAttribute("state", "readonly")
        return self
    def clear(self):
        disableAfterWrite = False
        if self["readonly"]:
            disableAfterWrite = True
            self.setEnabled(True)
        self["widget"].delete(0, "end")
        if disableAfterWrite:
            self._setAttribute("state", "readonly")
        return self
    def setText(self, text):
        self.setValue(text)
        return self
    def setValue(self, text, clearFirst=True):
        disableAfterWrite = False
        if self["readonly"]:
            disableAfterWrite = True
            self.setEnabled(True)
        if clearFirst: self["widget"].delete(0, "end")
        self["widget"].insert(0, str(text))
        if disableAfterWrite:
            self._setAttribute("state", "readonly")
        return self
    def getValue(self):
        return self["widget"].get()
    def setOptionList(self, l:Iterable):
        self["values"] = list(l)
        disableAfterWrite = False
        if self["readonly"]:
            disableAfterWrite = True
            self.setEnabled(True)
        self._setAttribute("values", l)
        if disableAfterWrite:
            self._setAttribute("state", "readonly")
        return self
    def addOption(self, i:str):
        self["values"].append(i)
        self.setOptionList(self["values"])
        return self
    def setBg(self, col:Union[Color, str]):
        disableAfterWrite = False
        if self["readonly"]:
            disableAfterWrite = True
            self.setEnabled(True)
        self.style.map("TCombobox", fieldbackground="red")#(col.value if hasattr(col, "value") else col)
        if disableAfterWrite:
            self._setAttribute("state", "readonly")
        return self
    def _decryptEvent(self, args):
        return self["widget"].get()
    def _decryptEvent2(self, args):
        return args
class Separator(Widget):
    def __init__(self, _master, group=None):
        if isinstance(_master, dict):
            self.data = _master
        elif isinstance(_master, self.__class__):
            self.data = _master.data
        elif isinstance(_master, Tk) or isinstance(_master, NotebookTab) or isinstance(_master, Canvas) or isinstance(_master, Frame) or isinstance(_master, LabelFrame):
            self.data = {"master": _master,  "widget":ttk.Separator(_master._get())}
        else:
            raise TKExceptions.InvalidWidgetTypeException("_master must be "+str(self.__class__.__name__)+", Frame or Tk instance not: "+str(_master.__class__.__name__))
        super().__init__(self, self.data, group)
class TaskBar(Widget):
    def __init__(self, _master, group=None):
        if isinstance(_master, dict):
            self.data = _master
        elif isinstance(_master, self.__class__):
            self.data = _master.data
        elif isinstance(_master, Tk) or isinstance(_master, NotebookTab) or isinstance(_master, Frame) or isinstance(_master, LabelFrame):
            if _master["hasMenu"]: raise RuntimeError("You cannot apply two Menus to the Window!") #@TODO Runtime ???
            _master["hasMenu"] = True
            self.data = {"master": _master,  "widget": _tk_.Menu(_master._get(), tearoff=False), "subMenu":[], "group":group}
            _master._get().config(menu=self.data["widget"])
        else:
            raise TKExceptions.InvalidWidgetTypeException("_master must be "+str(self.__class__.__name__)+", Frame or Tk instance not: "+str(_master.__class__.__name__))
        super().__init__(self, self.data, group)
    def createSubMenu(self, name:str):
        m = _SubMenu(self["master"], self["widget"], self.data, name, self["group"])
        #_SubMenu._SUB_MENUS.append(m)
        self["subMenu"].append(m)
        self["widget"].add("cascade", label=name, menu=m._menu)
        return m
    def place(self, x=0, y=0, width=None, height=None, anchor=Anchor.UP_LEFT):
        pass
    def grid(self, row=0, column=0):
        pass
    def create(self):
        for i in self["subMenu"]: i.create()
class _SubMenu:
    _SUB_MENUS = []
    def __init__(self, master, menu, data, name, group):
        self._id = "".join([str(r.randint(0,9)) for _ in range(15)])
        self._widgets = [] #[["command", <type: Button>], ["cascade", <type: Button>, <type: SubMenu>]]
        self.data = data
        self._name = name
        self._group = group
        self.data["created"] = False
        self._master = master
        self._masterMenu = menu
        self._menu = _tk_.Menu(menu, tearoff=False)
        if group is not None:
            # dummy widget for Group
            self._wid = Widget(None, {"master":self._master, "widget":self._menu}, group)




    def clear(self):
        """
        for i in self._widgets:
            if i[1] is not None and "text" in i[1]["widgetProperties"].keys():
                try:
                    self._menu.delete(i[1]["widgetProperties"]["text"])
                except:
                    pass
                    """
        for i in range(len(self._widgets)+1):
            try:
                self._menu.delete(0)
            except Exception as e:
                print(e)
        self._widgets = []
    def createSubMenu(self, button:Button, group):
        m = _SubMenu(self._master, self._menu, self.data, (button["widgetProperties"]["text"] if "text" in button["widgetProperties"].keys() else ""), group)
        self._widgets.append(["cascade", button, m])
        return m
    def addSeparator(self):
        self._widgets.append(["separator", None])
    def create(self): #@TODO fix if menus are created after mainloop
        #if self.data["created"]: return#@TODO FIX self.data["create"] is True
        for widget in self._widgets:
            if widget[1] is not None:
                data = widget[1]["widgetProperties"].copy()
                if data.keys().__contains__("text"): data["label"] = data["text"]
                if widget[0] == "cascade": data["menu"] = widget[2]._menu if hasattr(widget[2], "_menu") else widget[2]
                self._menu.add(widget[0], **{k:v for k, v in zip(data.keys(), data.values()) if ['accelerator', 'activebackground', 'activeforeground', 'background', 'bitmap', 'columnbreak', 'command', 'compound', 'font', 'fg', 'bg', 'hidemargin', 'image', 'label', 'menu', 'offvalue', 'onvalue', 'selectcolor', 'selectimage', 'state', 'underline', 'value', 'variable'].__contains__(k)})
                if widget[0] == "cascade" and hasattr(widget[2], "create"):
                    widget[2].create()
            else:
                #print(type(widget[0]), widget)
                self._menu.add(widget[0], {})
        self.data["created"] = True
class ContextMenu(Widget):
    def __init__(self, _master, group=None, closable=True, eventType:Union[EventType, Key, Mouse, None]=EventType.key(Mouse.RIGHT_CLICK)):
        if isinstance(_master, dict):
            self.data = _master
        elif isinstance(_master, self.__class__):
            self.data = _master.data
        elif hasattr(_master, "_get"):
            self.data = {"master": _master,  "widget": _tk_.Menu(_master._get(), tearoff=0), "subMenu":[], "closable":closable, "eventType":eventType, "group":group}
            if eventType is not None: EventHandler._registerNewEvent(_master, self.open, eventType, [], 1, decryptValueFunc=self._decryptEvent, defaultArgs=False, disableArgs=False)
            self.data["mainSubMenu"] = self._createSubMenu()
        else:
            raise TKExceptions.InvalidWidgetTypeException("_master must be "+str(self.__class__.__name__)+", Frame or Tk instance not: "+str(_master.__class__.__name__))
        super().__init__(self, self.data, group)

    def _createSubMenu(self):
        m = _SubMenu(self["master"], self["widget"], self.data, "", self["group"])
        m._menu = self["widget"]
        self["subMenu"].append(m)
        return m
    def addSeparator(self):
        self["mainSubMenu"]._widgets.append(["separator", None])
    def createSubMenu(self, button:Button)->_SubMenu:
        return self["mainSubMenu"].createSubMenu(button, self["group"])
    def bindToWidget(self, widg):
        EventHandler._registerNewEvent(widg, self.open, self["eventType"], [], 1, decryptValueFunc=self._decryptEvent, defaultArgs=False, disableArgs=False)
    def open(self, loc:Location2D):
        if isinstance(loc, Event):
            loc = Location2D(loc.getValue())
        loc.toInt()
        try:
            self["widget"].tk_popup(loc.getX(), loc.getY())
        except Exception as e:
            print(e)
        finally:
            if not self["closable"]:#fuer Fabi :^)
                self["widget"].grab_release()
        return self
    def _decryptEvent(self, e):
        if isinstance(e, Event):
            e = e.getTkArgs()
        # why -> Error
        return Location2D(e.x_root, e.y_root)
    def place(self, x=0, y=0, width=None, height=None, anchor=Anchor.UP_LEFT):
        pass
    def grid(self, row=0, column=0):
        pass
    def create(self):
        for i in self["subMenu"]:
            i.create()
class NotebookTab(Widget):
    def __init__(self, _master, notebook=None, name=None, group=None):
        self.setTabName = self.setText
        if isinstance(_master, dict):
            self.data = _master
        elif isinstance(_master, self.__class__):
            self.data = _master.data
        elif isinstance(_master, Tk) or isinstance(_master, NotebookTab) or isinstance(_master, Canvas) or isinstance(_master, Frame) or isinstance(_master, LabelFrame):
            self.data = {"master": notebook, "widget": _tk_.Frame(notebook._get()), "tabWidget": notebook, "tabId": None, "name":name}
            notebook._get().add(self.data["widget"], text=name)
            self.data["tabId"] = self.getNumberOfTabs()-1
        else:
            raise TKExceptions.InvalidWidgetTypeException("_master must be " + str(self.__class__.__name__) + ", Frame or Tk instance not: " + str(_master.__class__.__name__))
        super().__init__(self, self.data, group)
    def getTabIndex(self):
        return self["tabId"]
    def getTabName(self):
        return self["tabWidget"]._get().tab(self["tabId"], "text")
    def setText(self, text):
        self["tabWidget"]._get().tab(self["tabId"], text=text)
        return self
    def setSelected(self):
        self["tabWidget"]._get().select(self["tabId"])
        return self
    def getNumberOfTabs(self):
        return self["tabWidget"]._get().index("end")
    def __destroy(self):

        if not self["placed"]:
            print("!! ALREADY destroyd tab name" + self["name"])
            raise
            return
        #assert self["placed"], f"Widget is already destroyed! {self['name']} {self}"
        print("destroy tab name"+self["name"])
        for id, widg in zip(self["childWidgets"].keys(), self["childWidgets"].values()):
            # EventHandler.unregisterAllEventsFormID(widg["id"])
            self["tkMaster"]._unregisterOnResize(widg)
        del self["master"]["childWidgets"][self["id"]]
        self["registry"].unregisterAll()
        self["tkMaster"]._unregisterOnResize(self)
        WidgetGroup.removeFromAll(self)
        self["widget"].destroy()
        self["destroyed"] = False
        self["placed"] = False
        for w in self["childWidgets"].copy().values():
            w.destroy()
class Notebook(Widget):
    _INITIALIZED = False
    _STYLE = None
    def __init__(self, _master, group=None, closable=False):
        if not self._INITIALIZED and closable:
            Notebook._STYLE = self._initializeCustomStyle()
            Notebook._INITIALIZED = True
        if isinstance(_master, dict):
            self.data = _master
        elif isinstance(_master, self.__class__):
            self.data = _master.data
        elif isinstance(_master, Tk) or isinstance(_master, NotebookTab) or isinstance(_master, Canvas) or isinstance(_master, Frame) or isinstance(_master, LabelFrame):
            self.data = {"master":_master,  "widget":ttk.Notebook(_master._get()), "tabIndexList":[], "runnable":None, "group":group, "init":{"func":self._init, "style":"CustomNotebook" if closable else ""}}
            if closable:
                self._get().bind("<ButtonPress-1>", self._on_close_press, True)
                self._get().bind("<ButtonRelease-1>", self._on_close_release)
                self._active = None
                self._name = ""
        else:
            raise TKExceptions.InvalidWidgetTypeException("_master must be "+str(self.__class__.__name__)+", Frame or Tk instance not: "+str(_master.__class__.__name__))
        super().__init__(self, self.data, group)
    def _init(self):
        self.onTabSelectEvent(self._updateTab)
    def onTabSelectEvent(self, func, args:list=None, priority:int=0, disableArgs=False, defaultArgs=False):
        EventHandler._registerNewEvent(self, func, EventType.customEvent("<<NotebookTabChanged>>"), args, priority, decryptValueFunc=self._decryptEvent, disableArgs=disableArgs, defaultArgs=defaultArgs)
    def setCtrlTabEnabled(self):
        self["widget"].enable_traversal()
        return self
    def getSelectedTabIndex(self):
        return self["widget"].index("current")
    def getSelectedTabName(self):
        return self["widget"].tab(self.getSelectedTabIndex(), "text")
    def createNewTab(self, name, group=None)->NotebookTab:
        nbt = NotebookTab(self["master"], self, name)
        self["tabIndexList"].append(nbt)
        if group is None: group = self["group"]
        if group is not None: group.add(nbt)
        self.addChildWidgets(nbt)
        return nbt
    def _decryptEvent(self, args):
        return self.getSelectedTabIndex()
    def _initializeCustomStyle(self):
        style = ttk.Style()
        self.images = (
            _tk_.PhotoImage("img_close",
                          data="R0lGODlhCAAIAMIBAAAAADs7O4+Pj9nZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQgd2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU5kEJADs="),
            _tk_.PhotoImage("img_closeactive",
                          data="R0lGODlhCAAIAMIEAAAAAP/SAP/bNNnZ2cbGxsbGxsbGxsbGxiH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU5kEJADs="),
            _tk_.PhotoImage("img_closepressed",
                          data="R0lGODlhCAAIAMIEAAAAAOUqKv9mZtnZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQgd2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU5kEJADs=")
        )

        style.element_create("close", "image", "img_close",
                             ("active", "pressed", "!disabled", "img_closepressed"),
                             ("active", "!disabled", "img_closeactive"),
                             border=8, sticky='')
        style.layout("CustomNotebook", [("CustomNotebook.client", {"sticky": "nswe"})])
        style.layout("CustomNotebook.Tab", [
            ("CustomNotebook.tab", {
                "sticky": "nswe",
                "children": [
                    ("CustomNotebook.padding", {
                        "side": "top",
                        "sticky": "nswe",
                        "children": [
                            ("CustomNotebook.focus", {
                                "side": "top",
                                "sticky": "nswe",
                                "children": [
                                    ("CustomNotebook.label", {"side": "left", "sticky": ''}),
                                    ("CustomNotebook.close", {"side": "left", "sticky": ''}),
                                ]
                            })
                        ]
                    })
                ]
            })
        ])
        return style
    def getStyle(self):
        return Notebook._STYLE
    def onCloseEvent(self, func, args:list=None, priority:int=0, defaultArgs=False, disableArgs=False, getIdInsteadOfName=True):
        runnable = EventHandler._getNewEventRunnable(self, func, args, priority, decryptValueFunc=self._decryptValueID if getIdInsteadOfName else self._decryptValueNAME, defaultArgs=defaultArgs, disableArgs=disableArgs)
        self["runnable"] = runnable
    def _decryptValueID(self, e):
        return self._active
    def _decryptValueNAME(self, e):
        return self._name
    def _on_close_press(self, event):
        """Called when the button is pressed over the close button"""
        element = self["widget"].identify(event.x, event.y)
        if "close" in element:
            index = self["widget"].index("@%d,%d" % (event.x, event.y))
            self["widget"].state(['pressed'])
            self._active = index
            return "break"
    def _deleteIndex(self, index):
        tab = self["tabIndexList"][index]
        shift = False
        for i, itab in enumerate(self["tabIndexList"]):
            if itab == tab:
                shift = True
            if shift: itab["tabId"] = i-1
        self["tabIndexList"].pop(index)
    def _on_close_release(self, event):
        def _call(runnable):
            runnable()
            return runnable.event

        """Called when the button is released"""
        if not self["widget"].instate(['pressed']):
            return
        element = self["widget"].identify(event.x, event.y)
        if "close" not in element:
            # user moved the mouse off of the close button
            return
        index = self["widget"].index("@%d,%d" % (event.x, event.y))
        self._name = self["widget"].tab(index, "text")
        _event = _call(self["runnable"])
        if self._active == index and (self["runnable"] is None or (self["runnable"] is not None and not _event["setCanceled"])):
            if self["destroyed"]: return
            self["widget"].forget(index)
            self._deleteIndex(index)
            self["widget"].event_generate("<<NotebookTabClosed>>")
        if self["destroyed"]: return
        self["widget"].state(["!pressed"])
        self._active = None
        self._updateTab(self.getSelectedTabIndex())
    def _updateTab(self, e):
        if len(self["tabIndexList"]) == 0: return
        """
        
        
        @param e: event or int -> tab index
        @return: 
        """
        for widget in Tk._getAllChildWidgets(self["tabIndexList"][e.getValue() if hasattr(e, "getValue") else e]):
            if widget["id"] in list(self["tkMaster"]["dynamicWidgets"].keys()):
                self["tkMaster"]._updateDynamicSize(widget)
    def __destroy(self):
        """
        Don't need.
        tab deletion is handeld by child widget of Notebook


        @return:
        """
        print("DESTROY TABS")
        super().destroy()
        for tab in self["tabIndexList"]:  # destroy all tabs
            tab.destroy()

class CustomStyle:
    def __init__(self, master, widget):
        self.data = {"master":master, "widget":widget}

        pass
    def getType(self):
        return self.data["widget"]._get().winfo_class()

#finish
class Canvas(Widget):
    def __init__(self, _master, group=None):
        if isinstance(_master, dict):
            self.data = _master
        elif isinstance(_master, self.__class__):
            self.data = _master.data
        elif isinstance(_master, Tk) or isinstance(_master, NotebookTab) or isinstance(_master, Canvas) or isinstance(_master, Frame) or isinstance(_master, LabelFrame):
            self.data = {"master": _master, "widget": _tk_.Canvas(_master._get()), "canObjs":{}}
        else:
            raise TKExceptions.InvalidWidgetTypeException("_master must be "+str(self.__class__.__name__)+", Frame or Tk instance not: "+str(_master.__class__.__name__))
        super().__init__(self, self.data, group)
    def clear(self):
        for i in list(self["canObjs"].values()).copy():
            i.destroy()
class CanvasObject:
    def __init__(self, _ins, data, group):
        if group is not None:
            group.add(_ins)
        self._ins = _ins
        self.data = data
        self.draw = self.render
        if not list(self.data.keys()).__contains__("id"):
            self.data["loc1"] = None
            self.data["loc2"] = None
            self.data["width"] = None
            self.data["height"] = None
            self.data["id"] = "".join([str(r.randint(0,9)) for _ in range(15)])
            self.data["master"]["canObjs"][self._ins["id"]] = self._ins
            self.data["registry"] = _EventRegistry(self)
    def __getitem__(self, item):
        return self.data[item]
    def __setitem__(self, key, value):
        self.data[key] = value
    def getType(self):
        return type(self._ins)
    def bind(self, func, event: Union[EventType, Key, Mouse], args:list=None, priority:int=0, defaultArgs=False, disableArgs=False):
        if event == "CANCEL": return
        assert self["objID"] is not None, "Render canvasObj before binding!"
        EventHandler._registerNewTagBind(self, self["objID"], func, event, args, priority, defaultArgs=defaultArgs, disableArgs=disableArgs)
    def render(self, updatePos=False):
        assert self["loc1"] is not None, "Location must be defined use .setLocation()!"
        assert self["loc2"] is not None or (self["width"] is not None and self["height"] is not None), "Location2 or width and height must be defined!"
        if updatePos and self["objID"] is not None:
            self["master"]._get().coords(
                self["objID"],
                ((self["loc1"].getX(), self["loc1"].getY(), self["loc1"].getX() + self["width"], self["loc1"].getY() + self["height"])
                 if self["loc2"] is None else
                 (self["loc1"].getX(), self["loc1"].getY(), self["loc2"].getX(), self["loc2"].getY()))
            )

        else:
            self.destroy()
            if self["loc2"] is None:
                self["objID"] = self["master"]._get()._create(self["type"], args=(self["loc1"].getX(), self["loc1"].getY(), self["loc1"].getX()+self["width"], self["loc1"].getY()+self["height"]), kw=self["data"])
            else:
                self["objID"] = self["master"]._get()._create(self["type"], args=(self["loc1"].getX(), self["loc1"].getY(), self["loc2"].getX(), self["loc2"].getY()), kw=self["data"])
            self.data["master"]["canObjs"][self._ins["id"]] = self._ins
        return self
    def setLocation(self, loc:Location2D):
        self["loc1"] = loc.clone()
        return self
    def setSecondLoc(self, loc:Location2D):
        self["loc2"] = loc.clone()
        return self
    def setWidth(self, w:int):
        self["width"] = int(w)
        return self
    def setHeight(self, l:int):
        self["height"] = int(l)
        return self
    def setBg(self, col: Union[Color, str]):
        self["data"]["fill"] = col.value if hasattr(col, "value") else col
        return self
    def setOutlineThickness(self, i:int):
        self["data"]["width"] = i
        return self
    def setOutlineColor(self, col: Union[Color, str]):
        self["data"]["outline"] = col.value if hasattr(col, "value") else col
        return self
    def setAnchor(self, anchor):
        self["data"]["anchor"] = anchor.value if hasattr(anchor, "value") else anchor
    def clone(self):
        data = self.data.copy()
        data["objID"] = None
        return self._ins.__class__(data)
    def destroy(self):
        if self.data["objID"] is not None and self._ins["id"] in self["master"]["canObjs"]:
            #self["registry"].unregisterAll()
            self["master"]["canObjs"].pop(self._ins["id"])
            self["master"]._get().delete(self["objID"])
            self["objID"] = None
    def _get(self):
        return self.data["master"]._get()
class CanvasImage(CanvasObject):
    def __init__(self, _master=None, group=None):
        if isinstance(_master, dict):
            self.data = _master
        elif isinstance(_master, self.__class__):
            self.data = _master.data
        elif isinstance(_master, Canvas):
            self.data = {"master": _master, "objID":None, "widget":None, "type":"image", "image":None, "data":{"anchor":"nw"}}
        else:
            raise TKExceptions.InvalidWidgetTypeException("_master must be " + str(self.__class__.__name__) + " instance or Canvas not: " + str(_master.__class__.__name__))
        super().__init__(self, self.data, group)

    def setImage(self, i:Union[TkImage, PILImage]):
        self["data"]["image"] = i._get()
        return self
    def render(self):
        self.destroy()
        self["objID"] = self["master"]._get()._create(self["type"], (self["loc1"].getX(), self["loc1"].getY()), self["data"])
        self.data["master"]["canObjs"][self["id"]] = self
        return self
class CanvasRect(CanvasObject):
    def __init__(self, _master=None, group=None):
        if isinstance(_master, dict):
            self.data = _master
        elif isinstance(_master, self.__class__):
            self.data = _master.data
        elif isinstance(_master, Canvas):
            self.data = {"master": _master, "objID":None, "widget":None, "type":"rectangle", "data":{}}
        else:
            raise TKExceptions.InvalidWidgetTypeException("_master must be " + str(self.__class__.__name__) + " instance or Canvas not: " + str(_master.__class__.__name__))
        super().__init__(self, self.data, group)
class CanvasCircle(CanvasObject):
    def __init__(self, _master=None, group=None):
        if isinstance(_master, dict):
            self.data = _master
        elif isinstance(_master, self.__class__):
            self.data = _master.data
        elif isinstance(_master, Canvas):
            self.data = {"master": _master, "objID":None, "widget":None, "type":"oval", "data":{}}
        else:
            raise TKExceptions.InvalidWidgetTypeException("_master must be " + str(self.__class__.__name__) + " instance or Canvas not: " + str(_master.__class__.__name__))
        super().__init__(self, self.data, group)
    def placeCenterWithRadius(self, loc:Location2D, r:int):
        loc = loc.clone()
        self.setLocation(loc.change(x=-r, y=-r))
        self.setWidth(r*2)
        self.setHeight(r*2)
        return self
class CanvasLine(CanvasObject):
    def __init__(self, _master=None, group=None):
        if isinstance(_master, dict):
            self.data = _master
        elif isinstance(_master, self.__class__):
            self.data = _master.data
        elif isinstance(_master, Canvas):
            self.data = {"master": _master, "objID":None, "widget":None, "type":"line", "data":{}}
        else:
            raise TKExceptions.InvalidWidgetTypeException("_master must be " + str(self.__class__.__name__) + " instance or Canvas not: " + str(_master.__class__.__name__))
        super().__init__(self, self.data, group)
    def placeByDegree(self, loc:Location2D, d:int, length:int):
        import math
        x = loc.getX()+math.cos(math.radians(d)) * length
        y = loc.getY()+math.sin(math.radians(d)) * length
        self.setLocation(loc)
        self.setSecondLoc(Location2D(x, y))
        return self
class CanvasText(CanvasObject):
    def __init__(self, _master=None, group=None):
        if isinstance(_master, dict):
            self.data = _master
        elif isinstance(_master, self.__class__):
            self.data = _master.data
        elif isinstance(_master, Canvas):
            self.data = {"master": _master, "objID":None, "widget":None, "type":"text", "data":{}}
        else:
            raise TKExceptions.InvalidWidgetTypeException("_master must be " + str(self.__class__.__name__) + " instance or Canvas not: " + str(_master.__class__.__name__))
        super().__init__(self, self.data, group)
    def setText(self, text):
        self["data"]["text"] = str(text)
        return self
    def setFont(self, size, art=FontType.ARIAL):
        self["data"]["font"] = (art.value if hasattr(art, "value") else art, size)
        return self
    def render(self):
        if "loc2" not in list(self.data.keys()):
            self["objID"] = self["master"]._get()._create(self["type"], args=(self["loc1"].getX(), self["loc1"].getY()), kw=self["data"])
        else:
            self["objID"] = self["master"]._get()._create(self["type"], args=(self["loc1"].getX(), self["loc1"].getY()), kw=self["data"])
        return self
    def setTextAngle(self, a):
        self["data"]["angle"] = int(a)
        return self

class FileDialog:
    @staticmethod
    def openFile(master=None, title=None, initialpath=None, types=None):
        if types is None:
            types = []
        return FileDialog._dialog(fd.askopenfilename, master=master, title=title, initialpath=initialpath, types=types)
    @staticmethod
    def openDirectory(master=None, title=None, initialpath=None):
        return FileDialog._dialog(fd.askdirectory, master=master, title=title, initialpath=initialpath)
    @staticmethod
    def saveFile(master=None, title=None, initialpath=None, types=None):
        if types is None:
            types = []
        return FileDialog._dialog(fd.asksaveasfilename, master=master, title=title, initialpath=initialpath, types=types)
    @staticmethod
    def _dialog(func, master=None, title=None, initialpath=None, types=None):
        if types is None:
            types = []
        destroy=False
        _types = (("", "",), ("", "",))
        if type(types) == list:
            for i in types:
                if str(i).startswith("."):
                    _types += (("", "*"+str(i),),)
                elif str(i).startswith("*."):
                    _types += (("", str(i),),)
                else:
                    raise TKExceptions.InvalidFileExtention(str(i)+" is not a valid Extention! Use .<ext>!")
        data = {"title":str(title),
                "initialdir":initialpath}
        if func != fd.askdirectory: data["filetypes"] = _types
        if initialpath is not None and os.path.split(initialpath)[1]!="" and False:# Disabled
            data["initialfile"] = os.path.split(initialpath)[1]
        if master is None:
            destroy = True
            master = Tk()
            master.hide()
            data["parent"] = master._get()

        #data["filetypes"] = (('', ''), ('', ''), ('', '*.jpg'), ('', '*.png'), ('', '*.jpeg'), ('', '*.ppm'), ('', '*.gif'))

        path = func(**data)
        if destroy: master.destroy()
        if path == "" or path is None:
            return None
        return path
class SimpleDialog:
    @staticmethod
    def askYesNo(master, message="", title=""):
        return SimpleDialog._dialog(msg.askyesno, master, message=message, title=title)
    @staticmethod
    def askYesNoCancel(master, message="", title=""):
        """
        yes    -> True
        no     -> False
        cancel -> None
        @param master:
        @param message:
        @param title:
        @return:
        """
        return SimpleDialog._dialog(msg.askyesnocancel, master, message=message, title=title)
    @staticmethod
    def askOkayCancel(master, message="", title=""):
        """

        @rtype: object
        @param master:
        @param message:
        @param title:
        @return: True or False
        """
        return SimpleDialog._dialog(msg.askokcancel, master, message=message, title=title)
    @staticmethod
    def askRetryCancel(master, message="", title=""):
        return SimpleDialog._dialog(msg.askretrycancel, master, message=message, title=title)
    @staticmethod
    def askInfo(master, message="", title=""):
        return SimpleDialog._dialog(msg.showinfo, master, message=message, title=title)
    @staticmethod
    def askError(master, message="", title=""):
        return SimpleDialog._dialog(msg.showerror, master, message=message, title=title)
    @staticmethod
    def askWarning(master, message="", title=""):
        return SimpleDialog._dialog(msg.showwarning, master, message=message, title=title)
    @staticmethod
    def askString(master, message="", title="", initialValue="", hideWith=None):
        return SimpleDialog._dialog(simd.askstring, master, prompt=message, title=title, show=hideWith, initialvalue=initialValue)
    @staticmethod
    def askInteger(master, message="", title="", initialValue=""):
        return SimpleDialog._dialog(simd.askinteger, master, prompt=message, title=title)
    @staticmethod
    def askFloat(master, message="", title="", initialValue=""):
        return SimpleDialog._dialog(simd.askfloat, master, prompt=message, title=title)
    @staticmethod
    def askUsernamePassword(master, title="", initialUname="", initialPassw="", unameString="Username:", passwString="Password:", hidePassword=True, default=None, group=None):
        _return = None
        _masterNone = False

        def cancel(e):
            nonlocal _return
            _return = "None"
        def select(e):
            nonlocal _return
            un = unE.getValue()
            pw = pwE.getValue()
            _return = [un, pw]

        def onClose():
            nonlocal _return
            _return = "None"

        if master is None:
            _masterNone = True
            master = Tk()
            master.hide()
        dialog = Dialog(master, group=group)
        dialog.setTitle(title)
        dialog.setResizeable(False)
        dialog.setWindowSize(200, 125)
        dialog.onCloseEvent(onClose)
        dialog.bind(select, EventType.RETURN)
        dialog.bind(cancel, EventType.ESC)

        unL = Label(dialog, group=group).placeRelative(fixY=0, fixHeight=25, centerX=True, fixWidth=100).setText(unameString)
        unE = Entry(dialog, group=group).placeRelative(fixY=25, fixHeight=25, centerX=True, fixWidth=100).setValue(initialUname)
        pwL = Label(dialog, group=group).placeRelative(fixY=50, fixHeight=25, centerX=True, fixWidth=100).setText(passwString)
        pwE = Entry(dialog, group=group).placeRelative(fixY=75, fixHeight=25, centerX=True, fixWidth=100).setValue(initialPassw)
        if hidePassword: pwE.hideCharactersWith("*")

        cancB = Button(dialog, group=group).setCommand(cancel).placeRelative(fixY=100, fixHeight=25, xOffsetLeft=50).setText("Cancel")
        okB = Button(dialog, group=group).setCommand(select).placeRelative(fixY=100, fixHeight=25, xOffsetRight=50).setText("OK")

        dialog.show()
        while True:
            master.update()
            t.sleep(.1)
            if _return == "None":
                if _masterNone: master.destroy()
                dialog.destroy()
                return None if default is None else default
            elif isinstance(_return, list):
                if _masterNone: master.destroy()
                dialog.destroy()
                return _return
    @staticmethod
    def chooseFromList(master, title="", values=None, chooseOnlyOne=True, topMost=True, forceToChoose=True)->str|list:
        _return = None
        _masterNone = False

        def cancel(e):
            nonlocal _return
            _return = "None"
        def select(e):
            nonlocal _return
            sel = list_.getSelectedItem()
            if sel is None:
                if forceToChoose:
                    SimpleDialog.askError(dialog, "Please choose at least one!")
                else:
                    _return = "None"
            else:
                _return = [sel] if not isinstance(sel, list) else sel
        def onClose():
            nonlocal _return
            if not forceToChoose:
                _return = "None"

        if master is None:
            _masterNone = True
            master = Tk()
            master.hide()

        dialog = Dialog(master)
        dialog.onCloseEvent(onClose)
        if forceToChoose:
            dialog.setCloseable(False)
        dialog.setWindowSize(200, 200)
        dialog.setResizeable(False)
        dialog.setTitle(title)
        list_ = Listbox(dialog, mode="single" if chooseOnlyOne else "multiple")
        list_.addAll(values)
        list_.placeRelative(changeHeight=-30)
        list_.bind(select, EventType.DOUBBLE_LEFT)

        Button(dialog).setText("Select").placeRelative(stickDown=True, fixHeight=30, xOffsetRight=50).setCommand(select)
        canc = Button(dialog).setText("Cancel").placeRelative(stickDown=True, stickRight=True, fixHeight=30, xOffsetRight=50).setCommand(cancel)
        if forceToChoose: canc.disable()
        dialog.show()
        while True:
            master.update()
            t.sleep(.1)
            if _return == "None":
                if _masterNone: master.destroy()
                dialog.destroy()
                return None
            elif isinstance(_return, list):
                if _masterNone: master.destroy()
                dialog.destroy()
                return _return
    @staticmethod
    def _dialog(d, master, **kwargs):
        if isinstance(master, Tk):
            if kwargs["title"] == "":
                kwargs["title"] = master["title"]
            return d(parent=master._get(), **kwargs)
        else:
            mas = Tk()
            mas.hide()
            anw = d(parent=mas._get(), **kwargs)
            mas.destroy()
            return anw
class ColorChooser:
    def __init__(self, c):
        self._c = c
    def getCanceled(self):
        return self._c == (None, None)
    def getHex(self):
        return self._c[1]
    def getRGB(self):
        return self._c[0]
    def __str__(self):
        return self.getRGB()
    @staticmethod
    def askColor(master=None, initialcolor=None, title=""):
        if isinstance(master, Tk):
            if initialcolor == "": initialcolor = None
            return ColorChooser(colorChooser.askcolor(initialcolor=initialcolor.value if hasattr(initialcolor, "value") else initialcolor, parent=master._get(), title=str(title)))
        else:
            mas = Tk()
            mas.hide()
            anw = ColorChooser(colorChooser.askcolor(initialcolor=initialcolor.value if hasattr(initialcolor, "value") else master, parent=mas._get(), title=title))
            mas.destroy()
            return anw

Combobox = DropdownMenu
Menu = TaskBar

if __name__ == '__main__':
    a = SimpleDialog.askUsernamePassword(None, title="passwordDialog", initialUname="raspberry")

    print(a, type(a))