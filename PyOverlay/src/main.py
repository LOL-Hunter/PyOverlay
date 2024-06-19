import os
os.chdir(os.path.split(__file__)[0])
from PyOverlay.src.gui import Window



class Main:
    def __init__(self, devMode=True):
        self.window = Window(devMode=devMode)

        self.window.mainloop()



if __name__ == '__main__':
    Main()