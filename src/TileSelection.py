prev_selection= None

class TileSelection():
    
    def __init__(self,clicked_widget,MAO):
        global prev_selection
        self.MAO=MAO
        for x in range(self.MAO.dimX):
            for y in range(self.MAO.dimY):
                if self.MAO.map1.map[x][y].label == clicked_widget:
                    if prev_selection == None: 
                        prev_selection = self.MAO.map1.map[x][y]
                        print "Selected %s %s !"%(self.MAO.map1.map[x][y].x,self.MAO.map1.map[x][y].y)
                    elif prev_selection == self.MAO.map1.map[x][y]: 
                        prev_selection = None
                        print "Nothing selected!"
                    elif prev_selection.army == None: 
                        prev_selection=self.MAO.map1.map[x][y]
                        print "Selected %s %s"%(self.MAO.map1.map[x][y].x,self.MAO.map1.map[x][y].y)
                    self.tile_selection(self.MAO.map1.map[x][y])

    def tile_selection(self,Tile):
        global prev_selection
        if Tile.army == None:
            prev_selection = None
            return
        elif Tile.army.owner !=self.MAO.active_player:
            prev_selection = None
            return
        else:
            if prev_selection in Tile.surrounding_tiles:
                prev_selection.army.move(Tile)
                
        
        
        
    