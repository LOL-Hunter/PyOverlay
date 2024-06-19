from PyOverlay.src.plugins import EventHandler, Plugin
from PyOverlay.src.gui import Overlay




class TestOverlay(Overlay):
    def __init__(self, master):
        super().__init__(
            master=master,
            name="testLabel",
            x=300,
            y=130,
            command=self._run
        )

    def _run(self):
        return "Test String"


class TestPlugin(EventHandler):
    def onEnable(self):
        print("enable")
    def onTabRegisterEvent(self):
        self.tab = plugin.registerTab("TEST")
    def onDisable(self, e):
        """
        On Plugin Disable

        @param e:
        @return:
        """
        print("disapojsd")
        pass





plugin = Plugin(priority=0)
#plugin.registerOverlay(TestOverlay)
plugin.register(TestPlugin)
plugin.disable()