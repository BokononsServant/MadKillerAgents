class TileSelection():
    
    def __init__(self,clicked_widget,MAO):
        
        self.MAO=MAO
        for x in range(self.MAO.dimX):
            for y in range(self.MAO.dimY):
                if self.MAO.map1.map[x][y].label == clicked_widget:
                    self.tile_selection(self.MAO.map1.map[x][y])

    def tile_selection(self,Tile):

        if Tile.army == None:
            pass
        
        
        
    