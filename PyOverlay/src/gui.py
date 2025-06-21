import os
from PyOverlay.src.pluginManager import PluginManager
from PyOverlay.src.constants import STYLE_GROUP as SG, LOAD_STYLE, OPEN_AT_START
from PyOverlay.src.settings import Settings
from PyOverlay.src.configLoader import Config
import tksimple as tk
from pyautogui import position, size
import threading as th
import time as t


class Overlay(tk.Toplevel):
    """
    Implementation of the overlay rendered on the screen.
    """
    OVERLAY_NAME = {}
    OVERLAYS = []
    def __init__(self, master=None, name="", x=100, y=25, visible=True, command=None, addStdLabel=True, devMode=False):
        if master is None: master = Window.WINDOW
        self.master = self
        self.name = name
        super().__init__(master, True)
        if name in Overlay.OVERLAY_NAME.keys(): raise Exception(f"Overlay name {name} exist already!")
        #overlay register
        Overlay.OVERLAY_NAME[name] = self
        Overlay.OVERLAYS.append(self)

        Window.WINDOW.overlayListBox.add(name) # add name to listbox

        if devMode:self.setBg("blue")
        self.setTopmost(True)
        if devMode: self.setTransparent("blue")

        self._windowSize = (x, y)
        self._screenSize = size()
        self._isVisible = visible
        self.setWindowSize(x, y)
        if addStdLabel: self._info = tk.Label(self).setBg("blue").setFg("black").setFont(15).placeRelative()
        self._updateFunction = command
        self._dragLabel = tk.Label(self).setBg("red")
        self._dragLabel.setText("-")
        self._dragLabel.setFont(15)
        self._dragLabel.bind(self._onDragEnter, tk.EventType.ENTER)
        self._dragLabel.bind(self._onDragLeave, tk.EventType.LEAVE)
        self._dragLabel.bind(self._onDrag, tk.EventType.MOTION_WITH_LEFT_CLICK)

        if devMode:self.overrideredirect()
        self.show()
    def update(self):
        """
        Updates current overlay.
        Get value from "command" func.
        
        @return: 
        """
        if self._updateFunction is not None and self._isVisible:
            value = self._updateFunction()
            self.setText(value)
    def setMoveAble(self, b):
        """
        Set Overlay moveable or not. 

        @param b: 
        @return: 
        """
        if b:
            self._dragLabel.placeRelative(fixWidth=10, fixHeight=10, stickRight=False)
        else:
            self._dragLabel.placeForget()
        self._dragLabel.lift()
    def setText(self, text:str):
        self._info.setText(text)
    def show(self):
        """
        Shows current Overlay.
        
        @return: 
        """
        self._isVisible = True
        super().show()
    def hide(self):
        """
        Hides current Overlay.
        
        @return: 
        """
        self._isVisible = False
        super().hide()
    def highlight(self):
        """
        Highlights current Overlay.

        @return:
        """
        self._info.setBg("yellow")
    def unHighlight(self):
        """
        Resets current Overlay highlighting.
        
        @return: 
        """
        self._info.setBg("blue")
    def _onDragEnter(self, e):
        self.setCursor(tk.Cursor.WIN_FOUR_ARROW)
    def _onDragLeave(self, e):
        self.setCursor(tk.Cursor.WIN_DEFAULT)
    def _onDrag(self, e):
        x, y = position()

        self._isMotioned = True
        windowSize = self._windowSize
        if x < 0: x=0
        if y+windowSize[1] > self._screenSize[1]:
            y = self._screenSize[1]-windowSize[1]
        print(x, y)
        self.setPositionOnScreen(x, y)
    @staticmethod
    def _updateOverlay():
        """
        Updates the current Overlay.

        @return:
        """
        for overlay in Overlay.OVERLAYS:
            overlay.update()
class ScreenMenuPage(tk.Frame):
    def __init__(self, _master):
        super().__init__(_master)
    def show(self):
        x = Config.SETTINGS_CONFIG.get("square_size", 10)
        self.placeRelative(changeHeight=-x, changeY=+x)
    def hide(self):
        self.placeForget()
class SettingsMenu:
    def __init__(self, _frame):
        self._alwaysTop = tk.Checkbutton(_frame, SG).setSelected()
        self._alwaysTop.setText("Always on top")
        self._alwaysTop.setTextOrientation()
        self._alwaysTop.onSelectEvent(self.update)
        self._alwaysTop.placeRelative(fixHeight=25, xOffsetRight=50)

        self._openPluginManager = tk.Button(_frame, SG)
        self._openPluginManager.setText("Open Plugin Manager")
        self._openPluginManager.setCommand(PluginManager.openGUI)
        self._openPluginManager.placeRelative(fixHeight=25, xOffsetRight=50, fixY=25)

        self._openAdvancedSettings = tk.Button(_frame, SG)
        self._openAdvancedSettings.setText("Open Advanced Settings")
        self._openAdvancedSettings.setCommand(Settings.openGUI)
        self._openAdvancedSettings.placeRelative(fixHeight=25, xOffsetRight=50, fixY=50)
    def update(self):
        alwtop = self._alwaysTop.getValue()
        Window.WINDOW.setAllwaysOnTop(alwtop)
class Window(tk.Tk):
    WINDOW = None
    def __init__(self, devMode=False):
        Window.WINDOW = self
        Settings.WINDOW = self
        self.devMode = devMode
        super().__init__()
        LOAD_STYLE()
        SG.add(self)
        self.setTopmost()
        self.overrideredirect()
        self.loadingFrame = tk.Frame(self, SG)
        self.loadingFrame.placeRelative()
        self.bind(self.exit, "<q>")

        self.setPositionOnScreen(0, 0)
        self._updateLoopRunning = True
        self._screenSize = size()
        self._windowSize = (350, 275)
        self._isMotioned = False
        self._isMinimized = (not Config.SETTINGS_CONFIG.get("is_menu_minimized_on_start", True) and not devMode)

        self.setWindowSize(*self._windowSize)

        self._dragLabel = tk.Label(self).setBg("red").setFont(20)
        self._dragLabel.setText("-")
        self._dragLabel.setFont(15)
        self._dragLabel.bind(self._onDragEnter, tk.EventType.ENTER)
        self._dragLabel.bind(self._onDragLeave, tk.EventType.LEAVE)
        self._dragLabel.bind(self._onDrag, tk.EventType.MOTION_WITH_LEFT_CLICK)
        self._dragLabel.bind(self._onDragClickRelease, tk.EventType.LEFT_CLICK_RELEASE)


        self.main = ScreenMenuPage(self)

        # Plugin Loading
        PluginManager.WINDOW = self
        PluginManager.loadPlugins(self.loadingFrame)

        self._menu = tk.Notebook(self.main)
        self._activePage = self.main
        #self._volume = self._menu.createNewTab("Volume", SG)
        #self._automation = self._menu.createNewTab("Macros", SG)
        PluginManager.call("onTabRegisterEvent") #  register other Tabs from Plugins
        self._overlay = self._menu.createNewTab("Overlay", SG)
        self._settings = self._menu.createNewTab("Settings", SG)
        self._menu.placeRelative()

        #self.volumeReg = VolumeRegulator(self._volume)
        #self.automation = Automation(self, self._automation)

        self.overlayListBox = tk.Listbox(self._overlay, SG).placeRelative(xOffsetRight=50)
        self.overlayListBox.onSelectEvent(self.overlayListBoxSelect)
        self._overlaySettings = tk.LabelFrame(self._overlay, SG).setText("Options").placeRelative(xOffsetLeft=50)
        self._overlay_hideW = tk.Checkbutton(self._overlaySettings, SG).setText("Hide all").setTextOrientation().placeRelative(fixHeight=25, changeWidth=-5).onSelectEvent(self.updateOverlayWidgets)
        self._overlay_moveW = tk.Checkbutton(self._overlaySettings, SG).setText("Move mode").setTextOrientation().placeRelative(fixHeight=25, fixY=25, changeWidth=-5).onSelectEvent(self.updateOverlayWidgets)
        self._overlay_hide = False
        self._overlay_move = False
        self.loadingFrame.lift()
        self._settingsMenu = SettingsMenu(self._settings)

        self.updateSquareSize()
        self._activePage.show()
        if not OPEN_AT_START and not devMode: self.minimize()
    def _init(self):
        """
        Running in parallel to mainloop.

        @return:
        """
        t.sleep(.1)
        self.updateDynamicWidgets()
        self.loadingFrame.placeForget()
        PluginManager.call("onEnable")
        self.updateMenuState()
        #th.Thread(target=self.updateLoop).start()
    def updateSquareSize(self):
        x = Config.SETTINGS_CONFIG.get("square_size", 10)
        self._dragLabel.placeRelative(fixWidth=x, fixHeight=x, stickRight=False)
        self._activePage.show()
    def exit(self):
        """
        Exits the application.

        @return:
        """
        self._updateLoopRunning = False
        PluginManager.call("onDisable")
        t.sleep(.2)
        self.destroy()
        os._exit(0)
    def updateLoop(self):
        while self._updateLoopRunning:
            self.update()
            t.sleep(.1)
            Overlay._updateOverlay()
    def updateOverlayWidgets(self):
        if self._overlay_hide != self._overlay_hideW.getValue():
            self._overlay_hide = self._overlay_hideW.getValue()
            if self._overlay_hide:
                for o in Overlay.OVERLAYS:
                    o.hide()
            else:
                for o in Overlay.OVERLAYS:
                    o.show()

        if self._overlay_move != self._overlay_moveW.getValue():
            self._overlay_move = self._overlay_moveW.getValue()
            if self._overlay_move:
                for o in Overlay.OVERLAYS:
                    o.setMoveAble(True)
            else:
                for o in Overlay.OVERLAYS:
                    o.unHighlight()
                    o.setMoveAble(False)
    def mainloop(self):
        th.Thread(target=self._init).start()
        super().mainloop()
    def hide(self):
        super().hide()
    def minimize(self):
        self._activePage.hide()
        self.updateSquareSize()
        x = Config.SETTINGS_CONFIG.get("square_size", 10)
        self.setWindowSize(x, x)
        PluginManager.call("onClose")
    def maximise(self):
        self.updateSquareSize()
        self.setWindowSize(*self._windowSize)
        self._activePage.show()
        PluginManager.call("onOpen")
    def overlayListBoxSelect(self):
        sel = self.overlayListBox.getSelectedItem()
        if sel is None and self._overlay_move: return
        for o in Overlay.OVERLAYS:
            o.unHighlight()
        overlay = Overlay.OVERLAY_NAME[sel]
        overlay.highlight()
    def updateMenuState(self):
        if self._isMinimized:
            self.minimize()
        else:
            self.maximise()
    def toggleMenuState(self):
        self._isMinimized = not self._isMinimized
    def _onDragClickRelease(self, e):
        if self._isMotioned:
            self._isMotioned = False
        else:
            self.toggleMenuState()
            self.updateMenuState()
    def _onDragEnter(self, e):
        self.setCursor(tk.Cursor.WIN_FOUR_ARROW)
    def _onDragLeave(self, e):
        self.setCursor(tk.Cursor.WIN_DEFAULT)
    def _onDrag(self, e):
        x, y = position()
        self._isMotioned = True
        if not Config.SETTINGS_CONFIG.get("is_menu_movable", True): return
        if self._isMinimized:
            windowSize = (10, 10)
        else:
            windowSize = self._windowSize
        if x < 0: x=0
        if y+windowSize[1] > self._screenSize[1]:
            y = self._screenSize[1]-windowSize[1]
        self.setPositionOnScreen(x, y)
