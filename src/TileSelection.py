prev_selection= None

class TileSelection():
    
    def __init__(self,clicked_widget,MAO):
        self.MAO=MAO
        for x in range(self.MAO.dimX):
            for y in range(self.MAO.dimY):
                if self.MAO.map1.map[x][y].label == clicked_widget:
                    self.tile_selection(self.MAO.map1.map[x][y])

    def tile_selection(self,Tile):
        global prev_selection
        
        if prev_selection == Tile:
            prev_selection = None
            print "Nothing selected!"
        
        elif prev_selection == None and Tile.owner == self.MAO.active_player and Tile.army != None:
            prev_selection = Tile
            print "Tile %s %s selected!"%(Tile.x, Tile.y)

        elif prev_selection != None and prev_selection.army != None and prev_selection.owner == self.MAO.active_player:
            
            if Tile in prev_selection.surrounding_tiles:
                prev_selection.army.move(Tile)
                prev_selection = None
            else:
                print "Not enough movement points!"
                

        

            
        
            
            
                
        
        
        
    