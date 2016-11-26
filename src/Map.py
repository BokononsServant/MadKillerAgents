import random
from Tile import Tile
import GetSurroundingTiles

class Map:
    def __init__(self, x, y):
        self.map = []
        self.x = x-1
        self.y = y-1
        self.GST=GetSurroundingTiles.GetSurroundingTiles()        
    def create(self):
        self.map = [[None for y in range(self.y)] for x in range(self.y)]
        prb6 = 10  # chance in % for 6
        prb5 = 80
        prb4 = 40
        prb3 = 0
        prb2 = 50
        # Pass 1: Assign 6s
        for x in range(self.x):
            for y in range(self.y):
                if random.randint(1, 100) <= prb6:
                    self.map[x][y] = Tile(x, y, 6)
        # Pass 2: Assign 5s
        for x in range(self.x):
            for y in range(self.y):
                if self.map[x][y] is None:
                    if 6 in self.GST.GST(x,y,self.map,attr='value') and random.randint(1, 100) <= prb5:
                        self.map[x][y] = Tile(x, y, 5)
        # pass 3: Assign 4s
        for x in range(self.x):
            for y in range(self.y):
                if self.map[x][y] is None:
                    if 5 in self.GST.GST(x,y,self.map,attr='value') and random.randint(1, 100) <= prb4:
                        self.map[x][y] = Tile(x, y, 4)
        # pass 4: Assign 3s
        for x in range(self.x):
            for y in range(self.y):
                if self.map[x][y] is None:
                    if 4 in self.GST.GST(x,y,self.map,attr='value') and random.randint(1, 100) <= prb3:
                        self.map[x][y] = Tile(x, y, 3)
        # pass 5: Assign 2s
        for x in range(self.x):
            for y in range(self.y):
                if self.map[x][y] is None:
                    if 3 in self.GST.GST(x,y,self.map,attr='value') and random.randint(1, 100) <= prb2:
                        self.map[x][y] = Tile(x, y, 2)
        # pass 6: Assign 1s
        for x in range(self.x):
            for y in range(self.y):
                if self.map[x][y] is None:
                    self.map[x][y] = Tile(x, y, 1)
    
#     def get_surrounding_tile_values(self, x, y):
#         values = []
#         PT = [[-1, 1],  [0, 1],  [1, 1],
#               [-1, 0],           [1, 0],
#               [-1, -1], [0, -1], [1, -1]]
#         for t in PT:
#             try:
#                 if x + t[0] >= 0 and y + t[1] >= 0:
#                     if self.map[x + t[0]][y + t[1]] is None:
#                         pass
#                     else:
#                         values.append(self.map[x + t[0]][y + t[1]].value)
#                         values.sort(reverse=True)
#             except:
#                 pass
#         return values
#     def set_surrounding_tiles(self, x, y):
#         tiles = []
#         PT = [[-1, 1],  [0, 1],  [1, 1],
#               [-1, 0],           [1, 0],
#               [-1, -1], [0, -1], [1, -1]]
#         for t in PT:
#             try:
#                 if x + t[0] >= 0 and y + t[1] >= 0:
#                         tiles.append(self.map[x + t[0]][y + t[1]])
#             except:
#                 pass
#         self.map[x][y].surrounding_tiles = tiles

    def update_map_tiles(self):
        for x in range(self.x):
            for y in range(self.y):
                self.map[x][y].surrounding_Tiles = self.GST.GST(x, y, self.map,attr='value') #funktioniert noch nicht           
                
    def print_map(self):
        for x in range(self.x):
            for y in range(self.y):
                if self.map[x][y] is None:
                    print "x",
                else:
                    print self.map[self.x-1-x][y].value, #for proper display, [0][0] is in bottom left corner
                    if y==self.y-1: print "\n"
    def print_field(self, x, y):
        tile = self.map[x][y]
        print "Selected x: %d y: %d value: %d" %(tile.x, tile.y, tile.value)
        #for tile in tile.surrounding_tiles:
        #   print "x: %d y: %d value: %d owner: %s" %(tile.x, tile.y, tile.value, tile.owner)
        print self.GST.GST(x, y, self.map, attr='value')
        print tile.surrounding_tiles

            
my_map = Map(12, 12)
my_map.create()
my_map.update_map_tiles()
#my_map.print_map()

#my_map.map[3][3].value = 100
#my_map.map[3][3].owner = "Jaap"
#my_map.print_field(2,2)
my_map.print_map()
my_map.print_field(0,0)

