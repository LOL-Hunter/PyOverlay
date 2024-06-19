from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume, AudioSession
import pysettings.tk as tk
from PyOverlay.src.constants import STYLE_GROUP as SG
from PyOverlay.src.plugins import EventHandler, Plugin

class VolumeScale(tk.Scale):
    def __init__(self, master, index, session:AudioSession):
        super().__init__(master, SG, 100, 0, orient=tk.Orient.VERTICAL)
        self.session = session
        self.isActive = bool(session.State)
        self.name = session.Process.name().replace(".exe", "")
        self.volumeInterface = session._ctl.QueryInterface(ISimpleAudioVolume)
        self.value = self.getVolume()

        self.setSteps(.01)
        self.setValueVisible(False)
        self.onScroll(self.onScaleChange)
        self.setValue(self.value*100)
        self.bind(self.onMouseScroll, tk.EventType.WHEEL_MOTION)
        self.setSliderWidth(10)


        self.placeRelative(fixX=50*index, fixWidth=50, changeHeight=-50)

        self.value_lbl = tk.Label(master, SG)
        self.value_lbl.setText(str(int(round(self.value*100)))+"%")
        self.value_lbl.placeRelative(fixX=50*index, fixWidth=50, fixHeight=25, stickDown=True, changeY=-25)

        self.name_lbl = tk.Label(master)
        self.name_lbl.setText(self.name)
        self.name_lbl.setBg("red" if self.getMute() else "green")
        self.name_lbl.bind(self.onLabelClick, tk.EventType.LEFT_CLICK)
        self.name_lbl.setFont(8)
        self.name_lbl.placeRelative(fixX=50*index, fixWidth=50, fixHeight=25, stickDown=True)
    def onLabelClick(self, e):
        value = self.getMute()
        self.setMute(not value)
        self.name_lbl.setBg("red" if not value else "green")
    def onMouseScroll(self, e:tk.Event):
        if str(e.getScrollDelta()).startswith("-"):
            value = round((self.getValue()-2) / 100, 2)
            value = 0 if value < 0 else value
        else:
            value = round((self.getValue()+2) / 100, 2)
            value = 1 if value > 1 else value
        self.setValue(value*100)
        self.setVolume(value)
        self.value_lbl.setText(str(int(round(self.getValue(), 0))) + "%")
    def onScaleChange(self, e):
        value = round(self.getValue()/100, 2)
        self.setVolume(value)
        self.value_lbl.setText(str(int(round(self.getValue(), 0)))+"%")
    def getVolume(self) -> float:
        return self.volumeInterface.GetMasterVolume()
    def setVolume(self, value):
        self.volumeInterface.SetMasterVolume(value, None)
    def getMute(self) -> float:
        return self.volumeInterface.GetMute()
    def setMute(self, value):
        self.volumeInterface.SetMute(bool(value), None)
    def delete(self):
        self.destroy()
        self.value_lbl.destroy()
        self.name_lbl.destroy()

class VolumeRegulator(EventHandler):
    def __init__(self):
        self.active = self.getSessions()
    def onTabRegisterEvent(self):
        self.master = plugin.registerTab("Volume")
    def onEnable(self):
        self.activeScales = []

        self.refreshImg = tk.PILImage.loadImage(r".\images\icons\refresh.png")
        self.refreshImg.resizeToIcon()
        self.refreshImg.preRender()

        self.refresh = tk.Button(self.master, SG)
        self.refresh.setImage(self.refreshImg)
        self.refresh.setCommand(self.update)
        self.refresh.placeRelative(fixWidth=20, fixHeight=20, stickDown=True, stickRight=True)

        self.err_lbl = tk.Label(self.master, SG)
        self.err_lbl.setText("There is no active Audio session!")

        self.update()
    def onOpen(self):
        print("open")
        self.update()
    def update(self):
        self.err_lbl.placeForget()
        self.active = self.getSessions()
        for v in self.activeScales:
            v.delete()
        self.activeScales = []
        for i, sess in enumerate(self.active):
            scale = VolumeScale(self.master, i, sess)
            self.activeScales.append(scale)
        if not len(self.active):
            self.err_lbl.placeRelative(changeWidth=-20, changeHeight=-20)


    def getSessions(self)->[AudioSession]:
        return [sess for sess in AudioUtilities.GetAllSessions() if sess.Process is not None]


plugin = Plugin(priority=5)
plugin.register(VolumeRegulator)