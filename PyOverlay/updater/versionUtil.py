from requests import get
from updater.integratedJsonConfig import JsonConfig
import os

URL = "https://raw.githubusercontent.com/LOL-Hunter/PyOverlay/main/version_manifest.json"
PATH = os.getcwd()

NEWEST_VERSION = None


def compareVersions(v1, v2):
    print(v1, v2)
    """
    is Version1 newer than Version2?

    @param v1:
    @param v2:
    @return:
    """

    v1List = v1.split(".")
    v2List = v2.split(".")
    if len(v1List) != len(v2List):
        return True
    for i, vers1, vers2 in zip(*enumerate(v1List), v2List):
        vers1 = int(vers1)
        vers2 = int(vers2)
        if vers1 > vers2: return True
    return False


def getVersionManifest():
    global NEWEST_VERSION
    if NEWEST_VERSION is None:
        content = get(URL).text
        NEWEST_VERSION = JsonConfig.fromString(content)["current_version"]
    return NEWEST_VERSION


def getCurrentVersion():
    js = JsonConfig.loadConfig(os.path.join(PATH, "version.json"))
    return js["version"]


def hasUpdates():
    thisVersion = getCurrentVersion()
    newestVersion = getVersionManifest()
    return compareVersions(newestVersion, thisVersion)

