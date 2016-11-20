from Tkinter import *
from docutils.nodes import compound
from pygments.styles.paraiso_dark import BACKGROUND
import random
import time
import Player

class MyApp:
    def __init__(self, parent):
       
        self.myParent = parent   
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()   
        self.myContainer2 =Frame(self.myContainer1)
        self.myContainer2.pack()
        
        self.button1 = Button(self.myContainer1, command=self.button1Click) ### (1)
        self.button1.configure(text="NewTurn", background= "green")
        self.button1.pack(side=LEFT)
        self.button1.focus_force()                
        
        self.dimX=14
        self.dimY=14
        
                
        self.turnTimer=0
        self.MapGeneration(self.dimX,self.dimY) # Args are dimensions of the map       
        
        self.AllPlayers=[]
        self.player1=Player.NewPlayer(name="Gabriel",color="blue")
        self.AllPlayers.append(self.player1)    
        self.player2=Player.NewPlayer(name="Jaap",color="yellow")
        self.AllPlayers.append(self.player2)    
        self.player3=Player.NewPlayer(name="Barbarian",color="red")
        self.AllPlayers.append(self.player3)    
        

        self.CreateArmy(self.player1, 0, 0, 20)
        self.CreateArmy(self.player1, 0, 0, 20)       
        self.CreateArmy(self.player2, self.dimX-1, self.dimY-1, 20)
        self.CreateArmy(self.player3, int((self.dimX)/2),int( (self.dimY-1)/2), 20)
        
        #self.RemoveArmy(0,0, 20)
        print self.player1.ownedTiles
        


    def NewTurn(self):
        self.turnTimer=self.turnTimer+1
        

        #self.moves=[[-1,0],[1,0],[0,1],[0,-1]]
        #self.pos=[random.randint(0,self.dimX-1),random.randint(0,self.dimY-1)]                
        #self.map[self.pos[0]][self.pos[1]].configure(bg="green")   
        
        #print self.pos         
        
             

        #for i in range(100):         
            #self.myContainer2.after(i*400,self.RandomMove)  
            #self.myContainer1.after(200,self.RandomMove)
            
            #self.delay
            
            
            
    def MoveArmy(self,strtTile, dstTile):
        pass
    
    def RemoveArmy(self,x,y,size):
        """
        Removes a number of units from an army.
        When army size reaches 0, reverts tile to unoccupied state       
        """
        
        if size >= self.map[x][y]["Army"]:
            self.map[x][y]["Army"]=0
            self.map[x][y]["Owner"].ownedTiles.remove([x,y])                        
            self.map[x][y]["Owner"]=" "
            self.map[x][y]["Tile"].configure(text=str(self.map[x][y]["TileValue"])+"\n"+str(self.map[x][y]["Army"]))
            self.map[x][y]["Tile"].configure(fg="black")
        else:
            self.map[x][y]["Army"]=self.map[x][y]["Army"]-size
            self.map[x][y]["Tile"].configure(text=str(self.map[x][y]["TileValue"])+"\n"+str(self.map[x][y]["Army"]))        
 
    def CreateArmy(self,plyr,x,y,size): 
        """
        Creates an army of size 'size' at position x and y for the player       
        Also sets ownership of the tile 
        If tile is already occupied initiates battle
        """
        
        #if self.map[x][y]["TileValue"] == 6:
            #print "Impassable Terrain!"
            #return "Impassable Terrain!"
        
        if size<0:
            print "Army size may not be nagative. Use RemoveArmy() instead"
            return "Army size may not be nagative. Use RemoveArmy() instead"
        
        if x<0 or x>self.dimX-1 or y<0 or y>self.dimY-1:
            print "Coordinates outside of map!"
            return "Coordinates outside of map!"       
        
        if self.map[x][y]["Owner"]!=plyr and self.map[x][y]["Owner"]!=" ":
            self.Battle()
            return        
        

        self.map[x][y]["Army"]=self.map[x][y]["Army"]+size       
        self.map[x][y]["Owner"]=plyr
        if self.map[x][y]["Owner"]==plyr:
            plyr.ownedTiles.append([x,y])
            
        self.map[x][y]["Tile"].configure(text=str(self.map[x][y]["TileValue"])+"\n"+str(self.map[x][y]["Army"]))        
        self.map[x][y]["Tile"].configure(fg=plyr.color)
        
        
        
        
    def Battle(self,x,y):
        print "Battle on tile "+str(x)+" x "+ str(y)
        
        
    def MapGeneration(self,dimX,dimY):  
        """
        Creates a dimX x dimY Map and fills it with Tile Values
        The map is a dimX x dimY 2D Array and each array-element contains a dictionary
        Keys are TileValue, Tile, Owner,Army
        
        """
        
        self.p=PhotoImage() # empty image needed for proper scaling of the tiles
        
        self.TileWidth=50 
        self.TileHeight =50 
        
        self.map=[[{} for y in range(dimY)] for x in range(dimX)] # map is a dimX x dimY 2D Array and each array-element contains a dictionary
        
        for x in range(dimX):
            for y in range(dimY):
                self.map[x][y]["Army"]=0
                self.map[x][y]["Owner"]=" "
                self.map[x][y]["TileValue"]=" "
                self.map[x][y]["Tile"]=Label(self.myContainer2,relief='solid',image=self.p,height=self.TileHeight, compound='left',width=self.TileWidth,text=self.map[x][y]["TileValue"])
                self.map[x][y]["Tile"].grid(row=dimY-y,column=x)
        
        prb6 = 10 # chance in % for 6
        prb5 = 80
        prb4 = 40
        prb3 = 0
        prb2 = 50
           
        #Pass 1: Assign 6s        
           
        for x in range(dimX):
            for y in range(dimY):
                if random.randint(1,100) <= prb6:
                    self.map[x][y]["TileValue"]=6
                    self.map[x][y]["Tile"].configure(text=6)
                    self.map[x][y]["Tile"].configure(bg="sienna4")
                       
        #Pass 2: Assign 5s       
                 
        for x in range(dimX):
            for y in range(dimY):
                if self.map[x][y]["Tile"].cget("text")==" ":                  
   
                    if 6 in self.SurroundingTiles(x, y) and random.randint(1,100) <= prb5:
                            self.map[x][y]["TileValue"]=5
                            self.map[x][y]["Tile"].configure(text=5)
                            self.map[x][y]["Tile"].configure(bg="sienna3")              
                 
        #pass 3: Assign 4s
           
        for x in range(dimX):
            for y in range(dimY):
                if self.map[x][y]["Tile"].cget("text")==" ":                  
    
                    if 5 in self.SurroundingTiles(x, y) and random.randint(1,100) <= prb4:
                            self.map[x][y]["TileValue"]=4
                            self.map[x][y]["Tile"].configure(text=4)
                            self.map[x][y]["Tile"].configure(bg="sienna2")  
                                
        #pass 4: Assign 3s
             
        for x in range(dimX):
            for y in range(dimY):
                if self.map[x][y]["Tile"].cget("text")==" ":                  
     
                    if 4 in self.SurroundingTiles(x, y) and random.randint(1,100) <= prb3:
                            self.map[x][y]["TileValue"]=3   
                            self.map[x][y]["Tile"].configure(text=3)
                            self.map[x][y]["Tile"].configure(bg="sienna1")
        #pass 5: Assign 2s
             
        for x in range(dimX):
            for y in range(dimY):
                if self.map[x][y]["Tile"].cget("text")==" ":                  
    
                    if 3 in self.SurroundingTiles(x, y) and random.randint(1,100) <= prb2:
                            self.map[x][y]["TileValue"]=2
                            self.map[x][y]["Tile"].configure(text=2)
                            self.map[x][y]["Tile"].configure(bg="green3")
        #pass 6: Assign 1s
            
        for x in range(dimX):
            for y in range(dimY):
                if self.map[x][y]["Tile"].cget("text")==" ":   
                            self.map[x][y]["TileValue"]=1         
                            self.map[x][y]["Tile"].configure(text=1)   
                            self.map[x][y]["Tile"].configure(bg="green2")
     
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
        self.NewTurn()
            
    def SurroundingTiles(self, x,y):
        ### Returns a list with the tile Values of the surrounding Tiles
        ST=[]
        
        try:
            if x>1: #when Array-Index is negative, Python starts counting from behind
                ST.append(self.map[x-1][y]["Tile"].cget("text"))
        except:
            pass
        try:
            ST.append(self.map[x+1][y]["Tile"].cget("text"))
        except:
            pass
        try:
            ST.append(self.map[x][y+1]["Tile"].cget("text"))
        except:
            pass
        try:
            if y>1: #when Array-Index is negative, Python starts counting from behind
                ST.append(self.map[x][y-1]["Tile"].cget("text"))
        except:
            pass
        
        return ST



root = Tk()
myapp = MyApp(root)
root.mainloop()
