from Tkinter import *
import random
import Player
import City
import SurroundingTiles
import Map
import Army
import tkMessageBox
import TileSelection
from VictoryConditions import check
from Board_Setup import place_players


class MyApp:

    def __init__(self, parent):

        self.myParent = parent
        
        #Game setup
        
        #self.Starting
        

        # initialize GUI
        
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        self.myContainer2 = Frame(self.myContainer1)
        self.myContainer2.pack()

        self.button1 = Button(
            self.myContainer1, command=self.button1Click)  # (1)
        self.button1.configure(text="Next Turn", background="green")
        self.button1.pack(side=LEFT)
         
        self.button2 = Button(
            self.myContainer1, command=self.button2Click)  # (1)
        self.button2.configure(text="Build City", background="green")
        self.button2.pack(side=LEFT)
         
        self.button3 = Button(
            self.myContainer1, command=self.button3Click)  # (1)
        self.button3.configure(text="Help", background="green")
        self.button3.pack(side=RIGHT)
        
        self.slider=Scale(self.myContainer1, from_=0, to=100,orient=HORIZONTAL,state='disabled')
        self.slider.pack(side=LEFT)

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

        # initialize Turn Timer
        self.turnTimer = 0
        self.round = 1

        # initialize Players
        self.SetUpPlayers()      

        # generate starting units
        place_players(self, 20)
        
        # start game
        
        self.printl("The game begins!")
        self.printl (("Round %s started!")%(self.round))
        self.printl( "%ss turn begins!"%(self.active_player.name))
        
        self.BeginningOfTurn(self.active_player)
        
        sim=False
        if sim: self.simulation() 
     
    def simulation(self):
            for i in range(50):
            #Dont use NewTurn with brackets!
                #self.myContainer1.after(i * 600, self.NewTurn)
                self.NewTurn()

    def NewTurn(self):
        self.turnTimer=self.turnTimer+1
        if self.turnTimer%len(self.AllPlayers)==0:
            """
            Checks for victory conditions etc.
            """
            if check(self)=="Game over!":
                tkMessageBox.showwarning("Game over!")
                return
            
            self.round=self.round+1
            self.printl (("Round %s started!")%(self.round))
               
        TileSelection.prev_selection=None  
           
        try:            
            self.active_player=self.AllPlayers[self.AllPlayers.index(self.active_player)+1]
            self.printl( "%ss turn begins!"%(self.active_player.name))
        except:                      
            self.active_player=self.AllPlayers[0]
            self.printl( "%ss turn begins!"%(self.active_player.name))
            
        self.BeginningOfTurn(self.active_player)    

    def BeginningOfTurn(self,plyr):        
        gt=SurroundingTiles.get()
        for cty in plyr.cities:
            producedArmies=0
            try:                
                for i in range(cty.pop):
                    producedArmies=producedArmies+sorted(gt.get(cty.tile.x,cty.tile.y,self.map1.map,attr='value'),reverse=True)[i]
            except:
                pass  
              
            producedArmies=producedArmies+cty.tile.value
            Army.Army(cty.tile,plyr,self,producedArmies,ignore6=True)
            self.printl( "%s armies produce in %s for %s!"%(producedArmies,cty.name,plyr.name))
                
        """
        Reset Movement points
        """
        
        for arms in plyr.armies:
            arms.MP=1
            
        plyr.AI.play_turn()
            
    def SetUpPlayers(self):

        self.AllPlayers = []
        self.player1 = Player.NewPlayer(name="Gabriel", color="blue", MAO=self,AI_type='human')
        self.AllPlayers.append(self.player1)
        self.player2 = Player.NewPlayer(name="Jaap", color="yellow", MAO=self,AI_type='random')
        self.AllPlayers.append(self.player2)
        self.player3 = Player.NewPlayer(name="Barbarian", color="red",MAO=self,AI_type='random')
        self.AllPlayers.append(self.player3)
        
        self.active_player=self.player1
    
    def tile_renderer(self, Tile, simulation=False,relief='solid'):
        
        if Tile == None or simulation==True:return
        
        self.p = PhotoImage()  # empty image needed for proper scaling of the tiles

        self.TileWidth = 50
        self.TileHeight = 50
        
        Tile.label=Label(self.myContainer2, relief=relief, image=self.p, height=self.TileHeight,
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
        
        Tile.label.bind("<Button-1>",self.call_tile_selection)      
        Tile.label.grid(row=self.dimY-Tile.y, column=Tile.x)
        
    def button1Click(self):
        self.NewTurn()
    
    def button3Click(self):
        InfoText="""Left-click selects or deselects an army.
                    Left-click to move a selected army.
                    Build city creates a new city (costs %s units) or increases population.
                    Population costs are:
                    1->2: %s units 
                    2->3: %s units 
                    3->4: %s units 
                    4->5: %s units 
                    5->6: %s units 
                    6->7: %s units 
                    7->8: %s units
                    8->9: %s units
                    9->10: %s units
                    10->11: %s units
                    """%(Army.cost_build_city, Army.cost_grow_city[1],Army.cost_grow_city[2],Army.cost_grow_city[3],Army.cost_grow_city[4]
                         ,Army.cost_grow_city[5],Army.cost_grow_city[6],Army.cost_grow_city[7],Army.cost_grow_city[8],Army.cost_grow_city[9]
                         ,Army.cost_grow_city[10])
        
        tkMessageBox.showinfo("Help", InfoText)


        
    
    
    def button2Click(self):
        try:
            TileSelection.prev_selection.army.build_city()
        except:
            self.printl( "Couldn't build city! No army selected!")

    def call_tile_selection(self,event):
        TileSelection.TileSelection(event.widget,self)
        
    def printl(self,txt):
        try:
            self.listbox.insert(0,txt)
        except:
            self.game_log=Toplevel()
            self.game_log.title("Game Log")
            
            self.scrollbar1 = Scrollbar(self.game_log)
            self.scrollbar1.pack(side=RIGHT, fill=Y)
            
            self.scrollbar2 = Scrollbar(self.game_log,orient=HORIZONTAL)
            self.scrollbar2.pack(side=BOTTOM, fill=X)
            
            
            
            self.listbox = Listbox(self.game_log, width=70, height=40)
            self.listbox.pack()
    
            self.listbox.insert(0, txt)
            # attach listbox to scrollbar
            self.listbox.config(yscrollcommand=self.scrollbar1.set)
            self.scrollbar1.config(command=self.listbox.yview)
            
            self.listbox.config(xscrollcommand=self.scrollbar2.set)
            self.scrollbar2.config(command=self.listbox.xview)
    def test(self,Tile):
        print Tile.label.cget('text')
        Tile.label.configure(text="234")
        print Tile.label.cget('text')

if __name__ == "__main__":
    root = Tk()
    myapp = MyApp(root)
    root.mainloop()
