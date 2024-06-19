from updater.versionUtil import hasUpdates, getVersionManifest
from updater.downloadUtil import download
from updater import integratedTk as tk
import os
from shutil import rmtree
from zipfile import ZipFile

URL = "https://raw.githubusercontent.com/LOL-Hunter/PyOverlay/main/PyOverlay.zip"

class GUI(tk.Tk):
    def __init__(self, vers):
        super().__init__()
        self.setTitle("PyOverlay-Updater")
        self.setWindowSize(250, 100)
        self.setResizeable(False)
        self.setCloseable(False)
        self.infoLabel = tk.Label(self)
        self.infoLabel2 = tk.Label(self)
        self.processBar = tk.Progressbar(self)
        self.infoLabel.setText(f"Downloading version {vers}...")
        self.infoLabel.placeRelative(fixHeight=25)
        self.processBar.placeRelative(fixHeight=25, fixY=25, centerX=True, fixWidth=200)
        self.infoLabel2.placeRelative(fixHeight=25, fixY=50)
        self.update()


    def updateOverlay(self, url):
        PATH = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Temp")

        if os.path.exists(os.path.join(PATH, "PyOverlay.zip")):
            os.remove(os.path.join(PATH, "PyOverlay.zip"))
        if os.path.exists(os.path.join(PATH, "PyOverlay")):
            rmtree(os.path.join(PATH, "PyOverlay"))


        for proc in download(url, PATH, "PyOverlay.zip"):
            self.update()
            self.processBar.setPercentage(proc)
            self.infoLabel2.setText(f"{round(proc, 2)}%")
        self.infoLabel2.clear()
        self.infoLabel.setText("Extracting PyOverlay...")

        with ZipFile(os.path.join(PATH, "PyOverlay.zip"), 'r') as zip_ref:
            zip_ref.extractall(os.path.join(PATH, "PyOverlay"))

        NEW_FILES = os.path.join()

        #for dirpath, dirnames, filenames in os.walk():







def runOverlay():
    from PyOverlay.src.main import Main
    Main(devMode=False)


if __name__ == '__main__':
    if hasUpdates():

        gui = GUI(getVersionManifest())
        gui.updateOverlay(URL)


        gui.mainloop()

    runOverlay()