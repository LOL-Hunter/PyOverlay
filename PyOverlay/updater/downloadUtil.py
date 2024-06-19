from urllib.request import urlopen
from time import sleep

def download(url, _dir, name):
    u = urlopen(url)
    meta = u.info()
    size = int(meta.get("Content-Length"))
    print("Write to", _dir+"\\"+name)
    f = open(_dir+"\\"+name, 'wb')
    #meta = dict(u.askInfo())
    #file_size = int(meta["Content-Length"])
    file_size_dl = 0
    block_sz = 1024
    while True:
        sleep(.1)
        buffer = u.read(block_sz)
        if not buffer:
            break
        file_size_dl += len(buffer)
        f.write(buffer)
        yield file_size_dl * 100. / size
    f.close()