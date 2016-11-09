from Tkinter import *
from docutils.nodes import compound

class MyApp:
    def __init__(self, parent):
        
        self.myParent = parent
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()  
    
        
        self.photo=PhotoImage(file="./Tileset/baum.gif")
        
        self.L1 = Label(self.myContainer1,image=self.photo, text="za", compound=CENTER, fg="green", bg="white",font = "Helvetica 16 bold italic")       
        self.L1.pack()     
        
        self.L2 = Label(self.myContainer1,image=self.photo, text="zu", compound=CENTER, fg="green", bg="white",font = "Helvetica 16 bold italic")       
        self.L2.pack()
        
        self.x=30
        self.y =20
        
        self.L3 = Label(self.myContainer1,bg="green",height=self.y, width=self.x, text=str(self.x)+" x "+str(self.y))
        self.L3.pack()
        
        self.L4 = Label(self.myContainer1,bg="red",height=self.y, width=self.x, text=str(self.x)+" x "+str(self.y))
        self.L4.pack(side=RIGHT)
        
        


root = Tk()
myapp = MyApp(root)
root.mainloop()
