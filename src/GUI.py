from Tkinter import *
from docutils.nodes import compound
from pygments.styles.paraiso_dark import BACKGROUND
import random
import time

class MyApp:
    def __init__(self, parent):
       
        self.myParent = parent
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()   
                
        #self.photo=PhotoImage(file="./Tileset/baum.gif")
        
        #self.L1 = Label(self.myContainer1,image=self.photo, text="za", compound=CENTER, fg="green", bg="white",font = "Helvetica 16 bold italic")       
        #self.L1.pack()     
        
        #self.L2 = Label(self.myContainer1,image=self.photo, text="zu", compound=CENTER, fg="green", bg="white",font = "Helvetica 16 bold italic")       
        #self.L2.pack()
        
        self.x=40
        self.y =40
        
        #self.L3 = Label(self.myContainer1,bg="green",height=self.y, width=self.x, text=str(self.x)+" x "+str(self.y))
        #self.L3.pack()
        
        self.p=PhotoImage()
        self.dimX=20
        self.dimY=20
        #self.L1 = Label(self.myContainer1,bg="red",relief='solid',image=self.p,height=self.y, compound='center',width=self.x, text='sex')
        #self.L1.pack(side=RIGHT)
        self.k=0
        self.map=[[0 for i in range(self.dimY)] for i in range(self.dimX)]
        
        for i in range(self.dimX):
            for j in range(self.dimY):
                self.map[i][j]=(Label(self.myContainer1,bg="red",relief='solid',image=self.p,height=self.y, compound='left',width=self.x,text=random.randint(1,6)))
                self.map[i][j].grid(row=self.dimY-j,column=i)          
                #self.tiles[self.i,j].grid(row=self.j,column=self.i)
                
        #self.L1['text']="green"
        #self.["background"]='green'
        #self.tiles[1].config(text = "sdf")
        #print len(self.tiles)
        #print self.tiles[1]
        self.moves=[[-1,0],[1,0],[0,1],[0,-1]]
        self.pos=[random.randint(0,self.dimX-1),random.randint(0,self.dimY-1)]                
        self.map[self.pos[0]][self.pos[1]].configure(bg="green")   
        
        print self.pos         
     
        for i in range(100):         
            self.myContainer1.after(i*400,self.RandomMove)  
            #self.myContainer1.after(200,self.RandomMove)
            
            #self.delay
            

    def RandomMove(self):
        
        self.map[self.pos[0]][self.pos[1]].configure(bg="red")
            
        self.move=random.choice(self.moves)            
        self.moveX=self.move[0]
        self.moveY=self.move[1]
            
        while self.moveX+self.pos[0]<0 or self.moveX+self.pos[0]>self.dimX-1 or self.moveY+self.pos[1]<0 or self.moveY+self.pos[1]>self.dimY-1:
            self.move=random.choice(self.moves)            
            self.moveX=self.move[0]
            self.moveY=self.move[1]
                
        self.map[self.pos[0]+self.moveX][self.pos[1]+self.moveY].configure(bg="green")
            
        self.pos=[self.pos[0]+self.moveX,self.pos[1]+self.moveY]
        
        #print self.pos            
        
         
                    

        #self.map[4][0].configure(bg="green")
        #self.map[4-1][0+1].configure(bg="green")
        

root = Tk()
myapp = MyApp(root)
root.mainloop()
