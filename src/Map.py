import random
from Tile import Tile
import SurroundingTiles

class Map:
    def __init__(self, dimX, dimY):
        """
        If instatiated this class will generate a Map object with the specified dimensions.
        The map is a 2D array, and every array field contains a Tile object.
        For each tile object the following fields are set:
            'value' gets assigned according to the used algorithm
            'surrounding_tiles" gets a list containing the 8 immediately adjacent Tiles
        To print the map to the console use print_map.
        To reassign surrounding_tiles for all tiles use update_map_tiles
        
        """
        self.dimX = dimX
        self.dimY = dimY
        self.GST=SurroundingTiles.get()
        self.create()
        self.update_map_tiles()
    def create(self):
        self.map = [[None for y in range(self.dimY)] for x in range(self.dimX)]
        prb6 = 10  # chance in % for 6
        prb5 = 80
        prb4 = 40
        prb3 = 0
        prb2 = 50
        # Pass 1: Assign 6s
        for x in range(self.dimX):
            for y in range(self.dimY):
                if random.randint(1, 100) <= prb6:
                    self.map[x][y] = Tile(x, y, 6)
        # Pass 2: Assign 5s
        for x in range(self.dimX):
            for y in range(self.dimY):
                if self.map[x][y] is None:
                    if 6 in self.GST.get(x,y,self.map,attr='value') and random.randint(1, 100) <= prb5:
                        self.map[x][y] = Tile(x, y, 5)
        # pass 3: Assign 4s
        for x in range(self.dimX):
            for y in range(self.dimY):
                if self.map[x][y] is None:
                    if 5 in self.GST.get(x,y,self.map,attr='value') and random.randint(1, 100) <= prb4:
                        self.map[x][y] = Tile(x, y, 4)
        # pass 4: Assign 3s
        for x in range(self.dimX):
            for y in range(self.dimY):
                if self.map[x][y] is None:
                    if 4 in self.GST.get(x,y,self.map,attr='value') and random.randint(1, 100) <= prb3:
                        self.map[x][y] = Tile(x, y, 3)
        # pass 5: Assign 2s
        for x in range(self.dimX):
            for y in range(self.dimY):
                if self.map[x][y] is None:
                    if 3 in self.GST.get(x,y,self.map,attr='value') and random.randint(1, 100) <= prb2:
                        self.map[x][y] = Tile(x, y, 2)
        # pass 6: Assign 1s
        for x in range(self.dimX):
            for y in range(self.dimY):
                if self.map[x][y] is None:
                    self.map[x][y] = Tile(x, y, 1)
    def update_map_tiles(self):
        for x in range(self.dimX):
            for y in range(self.dimY):                
                #self.map[x][y].surrounding_tiles = self.GST.get(x, y, self.map,attr='value')       
                self.map[x][y].surrounding_tiles = self.GST.get(x, y, self.map)           
    def print_map(self):        
        for y in range(self.dimY):
            for x in range(self.dimX):
                print self.map[x][self.dimY-1-y].value,
                if x == self.dimX-1: print "\n"
        
                    

 
# my_map = Map(12, 12)
# my_map.create()
# my_map.update_map_tiles()
# 
#  
# my_map.map[1][1].value = "J"
# my_map.map[1][1].owner = "Jaap"
# 
# my_map.print_map()
# 
# print "ST:"
# print my_map.map[1][1].surrounding_tiles

