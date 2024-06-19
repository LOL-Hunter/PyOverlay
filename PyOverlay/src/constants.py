from pysettings import tk
from tkinter import ttk

class Color:
    COLOR_WHITE = tk.Color.rgb(255, 255, 255)
    COLOR_DARK = tk.Color.rgb(50, 50, 50)
    COLOR_GRAY = tk.Color.rgb(160, 160, 160)




OPEN_AT_START = False
# test


STYLE_GROUP = tk.WidgetGroup()
STYLE_GROUP.addCommand("setBg", Color.COLOR_DARK)
STYLE_GROUP.addCommand("setFg", Color.COLOR_WHITE, ignoreErrors=True)
STYLE_GROUP.addCommand("setActiveBg", Color.COLOR_GRAY, ignoreErrors=True)
STYLE_GROUP.addCommand("setSlotBgDefault", Color.COLOR_DARK, ignoreErrors=True)
STYLE_GROUP.addCommand("setSelectBackGroundColor", Color.COLOR_GRAY, ignoreErrors=True)
STYLE_GROUP.addCommand("setSelectColor", Color.COLOR_GRAY, ignoreErrors=True)


def LOAD_STYLE():
    style = ttk.Style()

    style.theme_create("yummy", parent="alt", settings={
        "TNotebook":{
            "configure":{
                "tabmargins":[2, 5, 2, 0]
            }
        },
        "TNotebook.Tab":{
            "configure":{
                "padding":[5, 1],
                "background":tk.Color.rgb(50, 50, 50),
                "foreground":tk.Color.rgb(255, 255, 255)
            }
        },
        "Treeview": {
            "configure": {
                "background": Color.COLOR_DARK,
                "foreground": Color.COLOR_WHITE,
                "fieldbackground": Color.COLOR_DARK
            },
            "map": {
                "background": [('selected', Color.COLOR_GRAY)]
            }
        },
        "Treeview.Heading": {
            "configure": {
                "background": Color.COLOR_DARK,
                "foreground": Color.COLOR_WHITE
            }
        },
        "TProgressbar": {
            "configure": {
                "background": "green",
                "troughcolor": Color.COLOR_DARK,
            }
        },
        "TCombobox": {
            "configure": {
                "background": Color.COLOR_DARK,
                "foreground": Color.COLOR_WHITE,
                "fieldbackground": Color.COLOR_DARK,
                "selectbackground": Color.COLOR_DARK,
                "selectcolor": Color.COLOR_DARK,
            }
        },
        "Vertical.TScrollbar": {
            "configure": {
                "background": Color.COLOR_DARK,
                "foreground": Color.COLOR_WHITE,
                "fieldbackground": Color.COLOR_DARK,
                "selectbackground": Color.COLOR_DARK,
                "selectcolor": Color.COLOR_DARK,
                "arrowsize": 17
            }
        }
    }
    )

    style.theme_use("yummy")