from Tkinter import *
from docutils.nodes import compound
from pygments.styles.paraiso_dark import BACKGROUND
import random
import time
import Player
from random import Random
import City

class MyApp:
    def __init__(self, parent):
        
        #initialize GUI
        self.myParent = parent   
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()   
        self.myContainer2 =Frame(self.myContainer1)
        self.myContainer2.pack()
        
        self.button1 = Button(self.myContainer1, command=self.button1Click) ### (1)
        self.button1.configure(text="NewTurn", background= "green")
        self.button1.pack(side=LEFT)
        self.button1.focus_force()                
        
        #dimensions of the map        
        self.dimX=14
        self.dimY=14        

        #generate Map
        self.MapGeneration(self.dimX,self.dimY)         

        #initialize Turn Timer        
        self.turnTimer=0       
        
        #initialize Players
        self.SetUpPlayers()        
  
        #generate starting units
        self.CreateArmy(self.player1, x=1, y=0, size=20,ignore6=True)
#         self.CreateArmy(self.player1, x=2, y=2, size=20,ignore6=True)
#         self.CreateArmy(self.player1, x=6, y=6, size=20,ignore6=True)
#         self.CreateArmy(self.player2, x=7, y=8, size=20,ignore6=True)
#         self.CreateArmy(self.player2, x=1, y=1, size=20,ignore6=True)
#         self.CreateArmy(self.player2, x=3, y=3, size=20,ignore6=True)
        #generate starting cities
        self.CreateCity(self.player1, 0, 0)
        self.CreateCity(self.player1, 0, 1)
        
        
        
        #self.CreateArmy(self.player1, x=3, y=6, size=20,ignore6=True)
        #self.CreateArmy(self.player2, self.dimX-1, self.dimY-1, 20)
        #self.CreateArmy(self.player3, int((self.dimX)/2),int( (self.dimY-1)/2), 20)
        
        #start game 
        #for i in range(1220):
            #self.myContainer1.after(i*400,self.NewTurn) #Dont use NewTurn with brackets!
            #self.NewTurn()


        


    def NewTurn(self):
        
        self.MoveArmy(1, 0, -1, 0, 'all')
        self.MoveArmy(0, 0, 1, 0, 'all')
        
        
        
        #Random move
        self.turnTimer=self.turnTimer+1
        
        """
        LP1=list(self.player1.ownedTiles) #make copy of List bc. otherwise the list would be updated when it is modified by MoveArmy, breaking the iteration
        LP2=list(self.player2.ownedTiles)      
        for T in LP1: 
            self.MoveArmy(x=T[0],y=T[1],units='all', rnd=True)
        for T in LP2: 
            self.MoveArmy(x=T[0],y=T[1],units='all', rnd=True)           
        
        
              
        print "Turn "+str(self.turnTimer)+" done"
        """

    def MoveArmy(self,x,y, mvmtX=0,mvmtY=0,units='all',rnd=False):
        """
        Move army consits of two functions:
        First a new army is created on the destination tile then the old army is deleted
        Check against Coordinates outside of Map, impassable Terrain, battle, too many units
        """        
        
        if rnd:
            moves=[[-1,0],[1,0],[0,1],[0,-1]]
            rndMv=random.choice(moves)
            mvmtX=rndMv[0]
            mvmtY=rndMv[1]  
        
        if units == "all": units=self.map[x][y]["Army"]
        if units > self.map[x][y]["Army"]: units=self.map[x][y]["Army"]   
        
        if x<0 or y<0 or x>self.dimX-1 or y>self.dimX-1 or x+mvmtX<0 or y+mvmtY<0 or x+mvmtX>self.dimX-1 or y+mvmtY>self.dimX-1:
            print "Coordinates outside of map!"
            return "Coordinates outside of map!" 
        
        if self.map[x+mvmtX][y+mvmtY]["TileValue"] == 6:
            print "Impassable Terrain!"
            return "Impassable Terrain!"
        
        if self.map[x+mvmtX][y+mvmtY]["Owner"]!=self.map[x][y]["Owner"] and self.map[x+mvmtX][y+mvmtY]["Owner"]!=" ":
            print "Battle!"
            self.Battle(x,y, mvmtX,mvmtY,units)
            return 
        
        if mvmtX==mvmtY==0:
            return        

        if self.map[x][y]["Owner"]!=" ":
            self.CreateArmy(plyr=self.map[x][y]["Owner"],x=x+mvmtX,y=y+mvmtY,size=units)
            self.RemoveArmy(x, y, units)        
          
          
    def RemoveArmy(self,x,y,size):
        """
        Removes a number of units from an army.
        When army size reaches 0, reverts tile to unoccupied state       
        """
        
        if size >= self.map[x][y]["Army"]:
            self.map[x][y]["Army"]=0
            self.map[x][y]["Owner"].ownedTiles.remove([x,y])                        
            self.map[x][y]["Owner"]=" "
            self.map[x][y]["Tile"].configure(text=str(self.map[x][y]["TileValue"]))
            self.map[x][y]["Tile"].configure(fg='black')
        else:
            self.map[x][y]["Army"]=self.map[x][y]["Army"]-size
            self.map[x][y]["Tile"].configure(text=str(self.map[x][y]["TileValue"])+"\n"+str(self.map[x][y]["Army"]))        
 
    def CreateArmy(self,plyr,x,y,size,ignore6=False): 
        """
        Creates an army of size 'size' at position x and y for the player       
        Sets ownership of the tile 
        If tile is already occupied initiates battle
        Check against Coordinates outside of Map, Impassable Terrain (can be ignored), negative army size
        """
        
        if self.map[x][y]["TileValue"] == 6 and ignore6==False:
            print "Impassable Terrain!"
            return "Impassable Terrain!"
        
        if size<0:
            print "Army size may not be negative. Use RemoveArmy() instead"
            return "Army size may not be negative. Use RemoveArmy() instead"
        
        if x<0 or x>self.dimX-1 or y<0 or y>self.dimY-1:
            print "Coordinates outside of map!"
            return "Coordinates outside of map!"       
        
   
            
        if self.map[x][y]["Owner"]==" ":
            plyr.ownedTiles.append([x,y])
            self.map[x][y]["Owner"]=plyr       
        
        self.map[x][y]["Army"]=self.map[x][y]["Army"]+size
        if self.map[x][y]['City']!=" ":
            self.map[x][y]["Tile"].configure(text="TV: "+str(self.map[x][y]["TileValue"])+"\n"+"AS: "+str(self.map[x][y]["Army"])+"\n"+self.map[x][y]['City'].name+": "+str(self.map[x][y]['City'].pop))
        else:
            self.map[x][y]["Tile"].configure(text="TV: "+str(self.map[x][y]["TileValue"])+"\n"+"AS: "+str(self.map[x][y]["Army"]))
            
        self.map[x][y]["Tile"].configure(fg=plyr.color)
        #print str(x)+" "+str(y)
        
    def CreateCity(self,plyr,x,y):
        
        tmp=City.newCity(plyr,x,y,map=self.map)
        
        plyr.cities.append(tmp)
        if self.map[x][y]['City'] == " ":
            self.map[x][y]['City'] = tmp
            
        
  
    def Battle(self,x,y, mvmtX,mvmtY,units):
        
        print "Battle for tile "+str(x+mvmtX)+" "+str(y+mvmtY)
        
        attackerUnits=units
        defenderUnits=self.map[x+mvmtX][y+mvmtY]["Army"]
        attacker=self.map[x][y]["Owner"].name
        defender=self.map[x+mvmtX][y+mvmtY]["Owner"].name
        #attackerArmor=self.map[x][y]["TileValue"]
        defenderArmor=self.map[x+mvmtX][y+mvmtY]["TileValue"]
        
        print attacker+" has "+str(attackerUnits)+" units against "+defender+ "\'s "+str(defenderUnits)+" units"
        print defender+" fights on "+str(defenderArmor)
        
        
        if attackerUnits<defenderUnits+defenderArmor:             
            self.RemoveArmy(x, y, attackerUnits) #if attacker has less units than defender+TV he looses all his attacking units
        else:
            self.RemoveArmy(x, y, defenderUnits+defenderArmor) #if attacker has equal or more units than defender he looses units equal to the amount of defending units+TV
        
        
        self.RemoveArmy(x+mvmtX, y+mvmtY, attackerUnits-defenderArmor)
        
        
        if self.map[x][y]["Army"] > 0 and self.map[x+mvmtX][y+mvmtY]<=0:
            self.MoveArmy(x, y, mvmtX, mvmtY, units)
            print attacker + " wins " + str(self.map[x][y]["Army"]) + " : "+str(self.map[x+mvmtX][y+mvmtY]["Army"])
        else:
            print defender + " wins " + str(self.map[x][y]["Army"]) + " : "+str(self.map[x+mvmtX][y+mvmtY]["Army"])   
                                        
        
    def SetUpPlayers(self):
        
        self.AllPlayers=[]
        self.player1=Player.NewPlayer(name="Gabriel",color="blue")
        self.AllPlayers.append(self.player1)    
        self.player2=Player.NewPlayer(name="Jaap",color="yellow")
        self.AllPlayers.append(self.player2)    
        self.player3=Player.NewPlayer(name="Barbarian",color="red")
        self.AllPlayers.append(self.player3) 
            
    def MapGeneration(self,dimX,dimY):  
        """
        Creates a dimX x dimY Map and fills it with Tile Values
        The map is a dimX x dimY 2D Array and each array-element contains a dictionary
        Keys are TileValue, Tile, Owner, Army, City
        
        """
        
        self.p=PhotoImage() # empty image needed for proper scaling of the tiles
        
        self.TileWidth=50 
        self.TileHeight =50 
        
        self.map=[[{} for y in range(dimY)] for x in range(dimX)] # map is a dimX x dimY 2D Array and each array-element contains a dictionary
        
        for x in range(dimX):
            for y in range(dimY):
                self.map[x][y]["Army"]=0
                self.map[x][y]["City"]=" "
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
