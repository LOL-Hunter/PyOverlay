from PyOverlay.src.plugins import EventHandler, Plugin

DESCRIPTION = """
This is a Test Description.
"""


class TestPlugin(EventHandler):
    def onEnable(self):
        """
        This is the on enable Event!
        Use this as __init__ and initialize your code here.
        """
    def onTabRegisterEvent(self):
        """
        Here can new Tabs be registered.
        """
        self.tab = plugin.registerTab("TEST")
    def onDisable(self, e):
        """
        On Plugin Disable

        @param e:
        @return:
        """
    def onOpen(self):
        """
        Get executed if the menu opens.
        """
    def onClose(self):
        """
        Get executed if the menu closes.
        """
    def onSettingsFrameConstruct(self, frame):
        """
        This method gets executed if the settings are loading.
        Remove this method if your plugin has no settings.
        Widgets can be placed on the frame.
        """
    def onSettingsCloseEvent(self, e):
        """
        Use this method to save your settings.
        """


plugin = Plugin(priority=0) # priority for event call.
plugin.register(TestPlugin) # register plugin
plugin.disable() # if this method is called the plugin is disabled.