from pysettings.tk import _tk_, ttk
import pysettings.tk as tk

class DataVirtualizer(tk.Widget):
    def __init__(self, _master, autoRender=True):
        if isinstance(_master, dict):
            self.data = _master
        elif isinstance(_master, tk.Tk) or isinstance(_master, tk.Frame) or isinstance(_master, tk.LabelFrame):
            self.data = {"master": _master, "widget": tk._tk_.LabelFrame(_master._get())}
            self._canvas = tk.Canvas(master)
            self._scX = tk.Scale(master, orient=tk.Orient.HORIZONTAL, from_=1, to=1000).setValue(100).setBg(tk.Color.rgb(150, 150, 150)).onScroll(self._update)
            self._scY = tk.Scale(master, orient=tk.Orient.VERTICAL, from_=1, to=1000).setValue(100).setBg(tk.Color.rgb(150, 150, 150)).onScroll(self._update)
            self._isPoints = tk.Checkbutton(master, text="ShowPoints").setSelected().setBg(tk.Color.rgb(150, 150, 150)).onSelectEvent(self._update, args=["render"])
            self._autoRender = tk.Checkbutton(master, text="AutoRender").setValue(autoRender).setBg(tk.Color.rgb(150, 150, 150)).onSelectEvent(self._update)
            self._renderBtn = tk.Button(master, text="Render").setCommand(self._update, args=["render",])
            self.__isPoints = True
            self._maxValuesX = 100
            self._maxValuesY = 100
            self._dotWidth = 4
            self._drawedValues = 0
            self._lastPoint = tk.Location2D(0, 0)
            self._values = [0]
        else:
            raise tk.TKExceptions.InvalidWidgetTypeException("_master must be " + str(self.__class__.__name__) + ", Frame or Tk instance not: " + str(_master.__class__.__name__))
        super().__init__(self, self.data)
    def reset(self):
        self._lastPoint = tk.Location2D(0, self._canvas.getHeight()-10)
        self._canvas.clear()
        self._drawedValues = 0
        self._values = [0]
        return self
    def _update(self, e):
        if self._autoRender.getValue() or (e == "render" or (hasattr(e, "getArgs") and e.getArgs() is not None and e.getArgs()[0] == "render")):
            self._maxValuesX = self._scX.getValue()
            self._maxValuesY = self._scY.getValue()
            self.__isPoints = self._isPoints.getValue()
            _values = self._values.copy()
            self.reset()
            for value in _values[1:]:
                self.addValues(value)
    def addValues(self, args):
        assert self["alive"], "Widget must be placed before drawing values!"
        self._drawedValues += 1
        if ((self._canvas.getWidth()-10)/self._maxValuesX)*self._drawedValues < self._canvas.getWidth():
            pointLoc = tk.Location2D((((self._canvas.getWidth()-10)/self._maxValuesX)*self._drawedValues), self._canvas.getHeight()-tk._map(args, 0, self._maxValuesY, 10, self._canvas.getHeight()-10))
            if self.__isPoints:
                circ = tk.CanvasCircle(self._canvas).setLocation(pointLoc.clone().change(x=-int(self._dotWidth/2), y=-int(self._dotWidth/2))).setWidth(self._dotWidth).setHeight(self._dotWidth).setBg("black")
                circ.render()
            line = tk.CanvasLine(self._canvas).setLocation(self._lastPoint).setSecondLoc(pointLoc)
            line.render()
            self._lastPoint = pointLoc
            if args > max(self._values):
                #resize
                pass
        self._values.append(args)
    def place(self, x=0, y=0, width=200, height=200, anchor:tk.Anchor=tk.Anchor.UP_LEFT):
        assert not self["destroyed"], "The widget has been destroyed and can no longer be placed."
        if hasattr(anchor, "value"):
            anchor = anchor.value
        self.placeForget()
        if isinstance(x, tk.Location2D):
            x, y = x.get()
        x = int(round(x, 0))
        y = int(round(y, 0))
        self._canvas.place(0, 0, width-width*.1, height-height*.1)
        self._lastPoint = tk.Location2D(0, self._canvas.getHeight()-10)
        self._scX.place(0, height-height*.1,  width-width*.1, height*.1)
        self._scY.place(width-width*.1, 0, width*.1, height-height*.1)
        self._isPoints.place(width-width*.1, height-height*.1, width*.1)
        self._autoRender.place(width - width * .1, height - height * .1 + 25, width*.1)
        self._renderBtn.place(width - width * .1, height - height * .1 + 50, width*.1)
        self["widget"].place(x=x, y=y, width=width, height=height, anchor=anchor)
        self["alive"] = True
        return self
class TestWidget(tk.Widget):
    def __init__(self, _master):
        if isinstance(_master, dict):
            self.data = _master
        elif isinstance(_master, tk.Tk) or isinstance(_master, tk.Frame) or isinstance(_master, tk.LabelFrame):
            self.data = {"master": _master, "widget": tk._tk_.LabelFrame(_master._get())}
        else:
            raise tk.TKExceptions.InvalidWidgetTypeException("_master must be " + str(self.__class__.__name__) + ", Frame or Tk instance not: " + str(_master.__class__.__name__))
        super().__init__(self, self.data)
    def loadStyle(self):
        style = ttk.Style()
        self.images = (
            _tk_.PhotoImage("img_close",
                            data="R0lGODlhCAAIAMIBAAAAADs7O4+Pj9nZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQgd2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU5kEJADs="),
            _tk_.PhotoImage("img_closeactive",
                            data="R0lGODlhCAAIAMIEAAAAAP/SAP/bNNnZ2cbGxsbGxsbGxsbGxiH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU5kEJADs="),
            _tk_.PhotoImage("img_closepressed",
                            data="R0lGODlhCAAIAMIEAAAAAOUqKv9mZtnZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQgd2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU5kEJADs=")
        )

        style.element_create(
            "close", "image", "img_close",
            ("active", "pressed", "!disabled", "img_closepressed"),
            ("active", "!disabled", "img_closeactive"),
            border=8,
            sticky=''
                             )
        style.layout("CustomNotebook", [("CustomNotebook.client", {"sticky": "nswe"})])
        style.layout("CustomNotebook.Tab", [
            ("CustomNotebook.tab", {
                "sticky": "nswe",
                "children": [
                    ("CustomNotebook.padding", {
                        "side": "top",
                        "sticky": "nswe",
                        "children": [
                            ("CustomNotebook.focus", {
                                "side": "top",
                                "sticky": "nswe",
                                "children": [
                                    ("CustomNotebook.label", {"side": "left", "sticky": ''}),
                                    ("CustomNotebook.close", {"side": "left", "sticky": ''}),
                                ]
                            })
                        ]
                    })
                ]
            })
        ])
class CompleterEntry(tk.Entry):
    def __init__(self, _master):
        if isinstance(_master, dict):
            self.data = _master
        elif isinstance(_master, tk.Tk) or isinstance(_master, tk.Frame) or isinstance(_master, tk.LabelFrame):
            data = {"master":_master, "widget":_tk_.Entry(_master._get())}
            super().__init__(_master)
            self._addData(data)

            self._listBox = tk.Listbox(_master)
            self._listBox.onSelectEvent(self._setEntryText)
            self._rect = None


        else:
            raise tk.TKExceptions.InvalidWidgetTypeException("_master must be " + str(self.__class__.__name__) + ", Frame or Tk instance not: " + str(_master.__class__.__name__))

    def _up(self, e):
        pass
    def _down(self, e):
        pass


    def _setEntryText(self, e):
        self.addText(e.getValue())

    def _updateMenu(self, e, out):
        if out is None or self._rect is None or out == []:
            self._listBox.placeForget()
            return
        self._listBox.place(self._rect)
        self._listBox.clear()
        self._listBox.addAll(out)


    def _decryptEvent(self, args):
        return args

    def onUserInputEvent(self, func, args:list=None, priority:int=0, defaultArgs=False, disableArgs=False):
        event = tk.EventHandler._registerNewEvent(self, func, tk.EventType.KEY_UP, args, priority, decryptValueFunc=self._decryptEvent, defaultArgs=defaultArgs, disableArgs=disableArgs)
        event["afterTriggered"] = self._updateMenu

    def place(self, x=None, y=None, width=None, height=None, anchor:tk.Anchor=tk.Anchor.UP_LEFT):
        assert not self["destroyed"], "The widget has been destroyed and can no longer be placed."
        if x is None: x = 0
        if y is None: y = 0
        if hasattr(anchor, "value"):
            anchor = anchor.value
        if isinstance(x, tk.Location2D):
            x, y = x.get()
        if isinstance(x, tk.Rect):
            width = x.getWidth()
            height = x.getHeight()
            x, y, = x.getLoc1().get()
        x = int(round(x, 0))
        y = int(round(y, 0))
        self.placeForget()
        self._rect = tk.Rect.fromLocWidthHeight(tk.Location2D(x, y + height), width, 200)
        self["widget"].place(x=x, y=y, width=width, height=height, anchor=anchor)
        self["alive"] = True
        return self
if __name__ == "__main__":
    import os
    master = tk.Tk()



    def onComplete(e):

        val = ce.getValue()
        if val == "":
            return os.popen("fsutil fsinfo drives").read().replace("\n", "").strip(" ").split(" ")[1:]
        if not val.startswith("C:\\"):
            ce.setValue("C:\\")
        print("splitted Val", os.path.split(val)[0])
        if not os.path.exists(os.path.split(val)[0]):
            print("path does not exist: ", val)
            return []
        a = []
        for i in os.listdir(os.path.split(val)[0]):
            c = os.path.split(val)[0] + "\\" + i
            print(c, val)
            if c.startswith(val):
                a.append(i)
        print(a)
        return a


    master.setWindowSize(500, 500)


    ce = CompleterEntry(master)

    ce.onUserInputEvent(onComplete)


    ce.place(0, 0, 250, 20)


    master.mainloop()

