import os
from pysettings.jsonConfig import AdvancedJsonConfig
"""
This script handles the Config file I/O.
"""
BASE_PATH = os.getcwd()
CONFIG_PATH = os.path.join(BASE_PATH, 'config')

class Config:
    AdvancedJsonConfig.setConfigFolderPath(CONFIG_PATH)

    SETTINGS_CONFIG = AdvancedJsonConfig("SettingsConfig")
    SETTINGS_CONFIG.setDefault({
        "is_menu_movable":True,
        "is_menu_minimized_on_start":True,
        "square_size":10,
    })
    SETTINGS_CONFIG.load("settings.json")
