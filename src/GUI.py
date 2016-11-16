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
        self.myContainer2 =Frame(self.myContainer1)
        self.myContainer2.pack()
        
        self.button1 = Button(self.myContainer1, command=self.button1Click) ### (1)
        self.button1.configure(text="OK", background= "green")
        self.button1.pack(side=LEFT)
        self.button1.focus_force()                

        self.x=40
        self.y =40
        
        self.p=PhotoImage()
        self.dimX=20
        self.dimY=20

        self.k=0
        self.map=[[0 for i in range(self.dimY)] for i in range(self.dimX)]
        
        for i in range(self.dimX):
            for j in range(self.dimY):
                #self.map[i][j]=(Label(self.myContainer2,bg="red",relief='solid',image=self.p,height=self.y, compound='left',width=self.x,text=str(i)+" "+str(j)))
                self.map[i][j]=(Label(self.myContainer2,relief='solid',image=self.p,height=self.y, compound='left',width=self.x,text=" "))
                self.map[i][j].grid(row=self.dimY-j,column=i)          

        #self.moves=[[-1,0],[1,0],[0,1],[0,-1]]
        #self.pos=[random.randint(0,self.dimX-1),random.randint(0,self.dimY-1)]                
        #self.map[self.pos[0]][self.pos[1]].configure(bg="green")   
        
        #print self.pos         
        
        self.MapGeneration()

        
        
            
        
        #for i in range(100):         
            #self.myContainer2.after(i*400,self.RandomMove)  
            #self.myContainer1.after(200,self.RandomMove)
            
            #self.delay
            
    def MapGeneration(self):        
        
        prb6 = 10 # chance in % for 6
        prb5 = 80
        prb4 = 50
        prb3 = 50
        prb2 = 50
        
        #Pass 1: Assign 6s        
        
        for x in range(self.dimX):
            for y in range(self.dimY):
                if random.randint(1,100) <= prb6:
                    self.map[x][y].configure(text=6)
                    self.map[x][y].configure(bg="sienna4")
                    
        #Pass 2: Assign 5s       
              
        for x in range(self.dimX):
            for y in range(self.dimY):
                if self.map[x][y].cget("text")==" ":                  

                    if 6 in self.SurroundingTiles(x, y) and random.randint(1,100) <= prb5:
                            self.map[x][y].configure(text=5)
                            self.map[x][y].configure(bg="sienna3")              
              
        #pass 3: Assign 4s
        
        for x in range(self.dimX):
            for y in range(self.dimY):
                if self.map[x][y].cget("text")==" ":                  

                    if 5 in self.SurroundingTiles(x, y) and random.randint(1,100) <= prb4:
                            self.map[x][y].configure(text=4)
                            self.map[x][y].configure(bg="sienna2")  
                            
        #pass 4: Assign 3s
        
        for x in range(self.dimX):
            for y in range(self.dimY):
                if self.map[x][y].cget("text")==" ":                  

                    if 4 in self.SurroundingTiles(x, y) and random.randint(1,100) <= prb3:
                            self.map[x][y].configure(text=3)
                            self.map[x][y].configure(bg="sienna1")
        #pass 5: Assign 2s
        
        for x in range(self.dimX):
            for y in range(self.dimY):
                if self.map[x][y].cget("text")==" ":                  

                    if 3 in self.SurroundingTiles(x, y) and random.randint(1,100) <= prb2:
                            self.map[x][y].configure(text=2)
                            self.map[x][y].configure(bg="green3")
        #pass 6: Assign 1s
        
        for x in range(self.dimX):
            for y in range(self.dimY):
                if self.map[x][y].cget("text")==" ":             
                            self.map[x][y].configure(text=1)   
                            self.map[x][y].configure(bg="green2")
    
    
    

        
        
        
        
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

    def button1Click(self):  ### (3)
        print "button1Click event handler"
        if self.button1["background"] == "green":
            self.button1["background"] = "yellow"
        else:
            self.button1["background"] = "green"
            
    def SurroundingTiles(self, x,y):
        ### Returns a list with the tile Values of the surrounding Tiles
        ST=[]
        
        try:
            if x>1: #when Array-Index is negative, Python starts counting from behind
                ST.append(self.map[x-1][y].cget("text"))
        except:
            pass
        try:
            ST.append(self.map[x+1][y].cget("text"))
        except:
            pass
        try:
            ST.append(self.map[x][y+1].cget("text"))
        except:
            pass
        try:
            if y>1: #when Array-Index is negative, Python starts counting from behind
                ST.append(self.map[x][y-1].cget("text"))
        except:
            pass
        
        return ST



root = Tk()
myapp = MyApp(root)
root.mainloop()
