from Tkinter import *

#from docutils.nodes import compound
#from pygments.styles.paraiso_dark import BACKGROUND

import random
import time
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
                self.TileRenderer(self.map1.map[x][y])                
        
        self.map1.print_map()

        # initialize Turn Timer
        #self.turnTimer = 0

        # initialize Players
        #self.SetUpPlayers()
        
        #
        #self.B=SurroundingTiles.get()
        #print self.B.get(3,3,self.map)
        #print self.B.get(3,4,self.map)
        

        # generate starting units
#         self.CreateArmy(self.player1, x=1, y=0, size=20, ignore6=True)
#         self.CreateArmy(self.player1, x=2, y=2, size=20, ignore6=True)
#         self.CreateArmy(self.player1, x=6, y=6, size=20, ignore6=True)
#         self.CreateArmy(self.player2, x=7, y=8, size=20, ignore6=True)
#         self.CreateArmy(self.player2, x=1, y=1, size=20, ignore6=True)
#         self.CreateArmy(self.player2, x=3, y=3, size=20, ignore6=True)
        # generate starting cities

#         self.CreateCity(self.player1, 10, 10)
#         self.CreateCity(self.player2, 5, 5)
#         self.CreateCity(self.player3, 1, 1)

        #self.CreateCity(self.player1, 0, 1)
        
        #self.CreateArmy(self.player1, x=3, y=6, size=20,ignore6=True)
        #self.CreateArmy(self.player2, self.dimX-1, self.dimY-1, 20)
        #self.CreateArmy(self.player3, int((self.dimX)/2),int( (self.dimY-1)/2), 20)
        # start game
        #for i in range(100):
            # Dont use NewTurn with brackets!
            #self.myContainer1.after(i * 400, self.NewTurn)

    def NewTurn(self):

        self.BeginningOfTurn()
        #
        #         self.MoveArmy(1, 0, -1, 0, 'all')
        #         self.MoveArmy(0, 0, 0, 1, 'all')
        #         self.MoveArmy(0, 1, 0, 1, 'all')
        



        

        # Random move
        # make copy of List bc. otherwise the list would be updated when it is
        LP1 = list(self.player1.ownedTiles)
        LP2 = list(self.player2.ownedTiles)
        LP3 = list(self.player3.ownedTiles)
        self.turnTimer = self.turnTimer + 1
        
        for T in LP1:
            self.MoveArmy(x=T[0], y=T[1], units='all', rnd=True)
        for T in LP2:
            self.MoveArmy(x=T[0], y=T[1], units='all', rnd=True)
        for T in LP3:
            self.MoveArmy(x=T[0], y=T[1], units='all', rnd=True)
            

        print "Turn " + str(self.turnTimer) + " done"

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
                
    def MoveArmy(self, x, y, mvmtX=0, mvmtY=0, units='all', rnd=False):
        """
        Move army consits of two functions:
        First a new army is created on the destination tile then the old army is deleted
        Check against Coordinates outside of Map, impassable Terrain, battle, too many units, zero units
        """

        if rnd:
            moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            rndMv = random.choice(moves)
            mvmtX = rndMv[0]
            mvmtY = rndMv[1]

        if mvmtX == mvmtY == 0:
            return

        if units == "all":
            units = self.map[x][y]["Army"]
        if units > self.map[x][y]["Army"]:
            units = self.map[x][y]["Army"]
        if units == 0:
            return

        if x < 0 or y < 0 or x > self.dimX - 1 or y > self.dimX - 1 or x + mvmtX < 0 or y + mvmtY < 0 or x + mvmtX > self.dimX - 1 or y + mvmtY > self.dimX - 1:
            print "Coordinates outside of map!"
            return "Coordinates outside of map!"

        if self.map[x + mvmtX][y + mvmtY]["TileValue"] == 6:
            print "Impassable Terrain!"
            return "Impassable Terrain!"

        if self.map[x + mvmtX][y + mvmtY]["Owner"] != self.map[x][y]["Owner"] and self.map[x + mvmtX][y + mvmtY]["Owner"] != " ":
            print "Battle!"
            self.Battle(x, y, mvmtX, mvmtY, units)
            return

        if self.map[x][y]["Owner"] != " ":
            self.CreateArmy(plyr=self.map[x][y][
                            "Owner"], x=x + mvmtX, y=y + mvmtY, size=units)
            self.RemoveArmy(x, y, units)

    def RemoveArmy(self, x, y, size):
        """
        Removes a number of units from an army.
        When army size reaches 0, reverts tile to unoccupied state
        """

        if size >= self.map[x][y]["Army"] and self.map[x][y]['City'] == " ":
            self.map[x][y]["Army"] = 0
            self.map[x][y]["Owner"].ownedTiles.remove([x, y])
            self.map[x][y]["Owner"] = " "
            self.map[x][y]["Tile"].configure(
                text=str(self.map[x][y]["TileValue"]))
            self.map[x][y]["Tile"].configure(fg='black')

        elif size >= self.map[x][y]["Army"] and self.map[x][y]['City'] != " ":
            self.map[x][y]["Army"] = 0
            self.map[x][y]["Tile"].configure(text="TV: " + str(self.map[x][y]["TileValue"]) + "\n" + "AS: " + str(
                self.map[x][y]["Army"]) + "\n" + self.map[x][y]['City'].name + ": " + str(self.map[x][y]['City'].pop))

        elif self.map[x][y]['City'] != " ":
            self.map[x][y]["Army"] = self.map[x][y]["Army"] - size
            self.map[x][y]["Tile"].configure(text="TV: " + str(self.map[x][y]["TileValue"]) + "\n" + "AS: " + str(
                self.map[x][y]["Army"]) + "\n" + self.map[x][y]['City'].name + ": " + str(self.map[x][y]['City'].pop))

        elif self.map[x][y]['City'] == " ":
            self.map[x][y]["Army"] = self.map[x][y]["Army"] - size
            self.map[x][y]["Tile"].configure(
                text=str(self.map[x][y]["TileValue"]) + "\n" + str(self.map[x][y]["Army"]))

    def CreateArmy(self, plyr, x, y, size, ignore6=False):
        """
        Creates an army of size 'size' at position x and y for the player
        Sets ownership of the tile
        If tile is already occupied initiates battle
        Check against Coordinates outside of Map, Impassable Terrain (can be ignored), negative army size
        """

        if self.map[x][y]["TileValue"] == 6 and ignore6 == False:
            print "Impassable Terrain!"
            return "Impassable Terrain!"

        if size < 0:
            print "Army size may not be negative. Use RemoveArmy() instead"
            return "Army size may not be negative. Use RemoveArmy() instead"

        if x < 0 or x > self.dimX - 1 or y < 0 or y > self.dimY - 1:
            print "Coordinates outside of map!"
            return "Coordinates outside of map!"

        if self.map[x][y]["Owner"] == " ":
            plyr.ownedTiles.append([x, y])
            self.map[x][y]["Owner"] = plyr

        self.map[x][y]["Army"] = self.map[x][y]["Army"] + size
        if self.map[x][y]['City'] != " ":
            self.map[x][y]["Tile"].configure(text="TV: " + str(self.map[x][y]["TileValue"]) + "\n" + "AS: " + str(
                self.map[x][y]["Army"]) + "\n" + self.map[x][y]['City'].name + ": " + str(self.map[x][y]['City'].pop))
        else:
            self.map[x][y]["Tile"].configure(
                text="TV: " + str(self.map[x][y]["TileValue"]) + "\n" + "AS: " + str(self.map[x][y]["Army"]))

        self.map[x][y]["Tile"].configure(fg=plyr.color)
        # print str(x)+" "+str(y)

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
    
    def TileRenderer(self, Tile):
        
        self.p = PhotoImage()  # empty image needed for proper scaling of the tiles

        self.TileWidth = 50
        self.TileHeight = 50
        
        Tile.Label=Label(self.myContainer2, relief='solid', image=self.p, height=self.TileHeight,
                                               compound='left', width=self.TileWidth)
        
        Tile.Label.configure(text="TV: " + str(Tile.value), anchor=N)
        
        try:
            Tile.Label.configure(text="TV: " + str(Tile.value)+"\n"+
                                "AS: " + str(Tile.Army.size), anchor=N)
            Tile.Label.configure
        except:
            pass    
        
        if   Tile.value == 1: Tile.Label.configure(bg="green2")
        elif Tile.value == 2: Tile.Label.configure(bg="green3")
        elif Tile.value == 3: Tile.Label.configure(bg="sienna1")
        elif Tile.value == 4: Tile.Label.configure(bg="sienna2")
        elif Tile.value == 5: Tile.Label.configure(bg="sienna3")
        elif Tile.value == 6: Tile.Label.configure(bg="sienna4")
        
        
        
        Tile.Label.grid(row=self.dimY-Tile.y, column=Tile.x)
        

    def RandomMove(self):

        self.map[self.pos[0]][self.pos[1]].configure(bg="red")

        self.move = random.choice(self.moves)
        self.moveX = self.move[0]
        self.moveY = self.move[1]

        while self.moveX + self.pos[0] < 0 or self.moveX + self.pos[0] > self.dimX - 1 or self.moveY + self.pos[1] < 0 or self.moveY + self.pos[1] > self.dimY - 1:
            self.move = random.choice(self.moves)
            self.moveX = self.move[0]
            self.moveY = self.move[1]

        self.map[self.pos[0] + self.moveX][self.pos[1] +
                                           self.moveY].configure(bg="green")

        self.pos = [self.pos[0] + self.moveX, self.pos[1] + self.moveY]

    def button1Click(self):  # (3)
        self.NewTurn()



root = Tk()
myapp = MyApp(root)
root.mainloop()
