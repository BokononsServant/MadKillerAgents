
from Tkinter import *

class MyApp:
    def __init__(self, parent):
        self.myParent = parent  ### (7) remember my parent, the root
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()

        self.button1 = Button(self.myContainer1)
        self.button1.configure(text="OK", background= "green")
        self.button1.pack(side=LEFT)
        self.button1.bind("<Button-1>", self.button1Click) ### (1)

        for i in range(10):
            self.myParent.after(200,self.evt())
    
    
    def evt(self):
        self.button1Click("<Button-1>")
        

    def button1Click(self, event):    ### (3)
        if self.button1["background"] == "green": ### (4)
            self.button1["background"] = "yellow"
        else:
            self.button1["background"] = "green"




root = Tk()
myapp = MyApp(root)
root.mainloop()