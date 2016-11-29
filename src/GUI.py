from Tkinter import *
import random
import Player
import City
import SurroundingTiles
import Map
import Army

class MyApp:

    def __init__(self, parent):

        # initialize GUI
        self.myParent = parent
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        self.myContainer2 = Frame(self.myContainer1)
        self.myContainer2.pack()
 
        self.button1 = Button(
            self.myContainer1, command=self.button1Click)  # (1)
        self.button1.configure(text="NewTurn", background="green")
        self.button1.pack(side=LEFT)
        self.button1.focus_force()

        # dimensions of the map
        self.dimX = 10
        self.dimY = 10

        # generate Map
        self.map1=Map.Map(self.dimX,self.dimY)       
 
        #draw Map
        for x in range(self.dimX):
            for y in range(self.dimY):
                self.tile_renderer(self.map1.map[x][y])           
                
        #self.map1.print_map()
        #print self.map1.map[2][2]


        # initialize Turn Timer
        self.turnTimer = 0

        # initialize Players
        self.SetUpPlayers()      

        # generate starting units
        Army.Army(Tile=self.map1.map[4][4],owner=self.player1,units=30,MAO=self,ignore6=True)
        Army.Army(Tile=self.map1.map[2][2],owner=self.player1,units=30,MAO=self,ignore6=True)
#         Army.Army(Tile=self.map1.map[0][0],owner=self.player2,units=20,MAO=self,ignore6=True)
#         Army.Army(Tile=self.map1.map[6][6],owner=self.player2,units=20,MAO=self,ignore6=True)
#         Army.Army(Tile=self.map1.map[9][9],owner=self.player3,units=20,MAO=self,ignore6=True)
#         Army.Army(Tile=self.map1.map[0][9],owner=self.player3,units=20,MAO=self,ignore6=True)
        
        
        
        #self.player1.armies[0].move(self.map1.map[2][1],30)
#         print self.player1.armies
        
#         print self.player1.armies
#         print self.map1.map[2][2]
        
        # generate starting cities
        City.City(self.player1,self.map1.map[2][3],self)




        #self.CreateCity(self.player1, 0, 1)
        
        #self.CreateArmy(self.player1, x=3, y=6, size=20,ignore6=True)
        #self.CreateArmy(self.player2, self.dimX-1, self.dimY-1, 20)
        #self.CreateArmy(self.player3, int((self.dimX)/2),int( (self.dimY-1)/2), 20)
        # start game
        for i in range(200):
            #Dont use NewTurn with brackets!
            self.myContainer1.after(i * 600, self.NewTurn)
            #self.NewTurn()
            
        

    def NewTurn(self):

        #self.BeginningOfTurn() 

        # make copy of List bc. otherwise the list would be updated when it is modified by move etc.
#         LP1 = list(self.player1.armies)
#         LP2 = list(self.player2.armies)
#         LP3 = list(self.player3.armies)

        # Random move
        PT=[        [0, 1],
            [-1, 0],        [1, 0],
                    [0, -1]]
        
        gt=SurroundingTiles.get()
        
        for P in self.AllPlayers:
            LP= list(P.armies)
            print P.name+" : "+str(LP)         
            for A in LP:
                randomTile=random.choice(gt.get(A.tile.x,A.tile.y,self.map1.map,PT=PT))
                A.move(randomTile)
    
        print "Turn " + str(self.turnTimer) + " done"
        self.turnTimer = self.turnTimer + 1
        
        
        
    def BeginningOfTurn(self):
        for plyr in self.AllPlayers:
            print plyr.name
            for cty in plyr.cities:
                try:
                    producedArmies=0
                    for i in range(cty.pop):
                        producedArmies=producedArmies+cty.SurroundingTilesValues[i]
                    
                    self.CreateArmy(plyr, cty.pos[0], cty.pos[1], size=producedArmies, ignore6=True)
                except:
                    pass                

    def CreateCity(self, plyr, x, y):

        tmp = City.newCity(plyr, x, y, map=self.map)

        plyr.cities.append(tmp)
        if self.map[x][y]['City'] == " ":
            self.map[x][y]['City'] = tmp

    def Battle(self, x, y, mvmtX, mvmtY, units):

        print "Battle for tile " + str(x + mvmtX) + " " + str(y + mvmtY)

        attackerUnits = units
        defenderUnits = self.map[x + mvmtX][y + mvmtY]["Army"]
        attacker = self.map[x][y]["Owner"].name
        defender = self.map[x + mvmtX][y + mvmtY]["Owner"].name
        # attackerArmor=self.map[x][y]["TileValue"]
        defenderArmor = self.map[x + mvmtX][y + mvmtY]["TileValue"]

        print attacker + " has " + str(attackerUnits) + " units against " + defender + "\'s " + str(defenderUnits) + " units"
        print defender + " fights on " + str(defenderArmor)

        if attackerUnits < defenderUnits + defenderArmor:
            # if attacker has less units than defender+TV he looses all his
            # attacking units
            self.RemoveArmy(x, y, attackerUnits)
        else:
            # if attacker has equal or more units than defender he looses units
            # equal to the amount of defending units+TV
            self.RemoveArmy(x, y, defenderUnits + defenderArmor)

        self.RemoveArmy(x + mvmtX, y + mvmtY, attackerUnits - defenderArmor)

        if self.map[x][y]["Army"] > 0 and self.map[x + mvmtX][y + mvmtY]['Army'] <= 0:
            self.MoveArmy(x, y, mvmtX, mvmtY, units)
            print attacker + " wins " + str(self.map[x][y]["Army"]) + " : " + str(self.map[x + mvmtX][y + mvmtY]["Army"])
        else:
            print defender + " wins " + str(self.map[x][y]["Army"]) + " : " + str(self.map[x + mvmtX][y + mvmtY]["Army"])

    def SetUpPlayers(self):

        self.AllPlayers = []
        self.player1 = Player.NewPlayer(name="Gabriel", color="blue")
        self.AllPlayers.append(self.player1)
        self.player2 = Player.NewPlayer(name="Jaap", color="yellow")
        self.AllPlayers.append(self.player2)
        self.player3 = Player.NewPlayer(name="Barbarian", color="red")
        self.AllPlayers.append(self.player3)
    
    def tile_renderer(self, Tile):
        
        if Tile == None:return
        
        self.p = PhotoImage()  # empty image needed for proper scaling of the tiles

        self.TileWidth = 50
        self.TileHeight = 50
        
        Tile.label=Label(self.myContainer2, relief='solid', image=self.p, height=self.TileHeight,
                                               compound='left', width=self.TileWidth)
        
        Tile.label.configure(text="TV: " + str(Tile.value), anchor=N)
        
        if Tile.army != None and Tile.city == None:
            Tile.label.configure(text="TV: " + str(Tile.value)+"\n"+
                                "AS: " + str(Tile.army.units), anchor=N)
        if Tile.army == None and Tile.city != None:
            Tile.label.configure(text="TV: " + str(Tile.value)+"\n"+
                                 Tile.city.name+": "+str(Tile.city.pop), anchor=N)
        if Tile.army != None and Tile.city != None:
            Tile.label.configure(text="TV: " + str(Tile.value)+"\n"+
                                "AS: " + str(Tile.army.units)+"\n"+
                                Tile.city.name+": "+str(Tile.city.pop), anchor=N)            
        
        try:
            Tile.label.configure(fg=Tile.owner.color)
        except:
            pass
            
        
        if   Tile.value == 1: Tile.label.configure(bg="green2")
        elif Tile.value == 2: Tile.label.configure(bg="green3")
        elif Tile.value == 3: Tile.label.configure(bg="sienna1")
        elif Tile.value == 4: Tile.label.configure(bg="sienna2")
        elif Tile.value == 5: Tile.label.configure(bg="sienna3")
        elif Tile.value == 6: Tile.label.configure(bg="sienna4")         
              
        Tile.label.grid(row=self.dimY-Tile.y, column=Tile.x)
        
    def button1Click(self):  # (3)
        self.NewTurn()


if __name__ == "__main__":
    root = Tk()
    myapp = MyApp(root)
    root.mainloop()
