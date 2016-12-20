from SurroundingTiles import get

class City:
    
    def __init__(self,owner,Tile,MAO):
        self.MAO=MAO
        gt=get()
        PT = [
         [-2,2],  [-1, 2], [0, 2], [1, 2], [2,2],
         [-2,1],  [-1, 1], [0, 1], [1, 1], [2,1],
         [-2,0],  [-1, 0],         [1, 0], [2,0],
         [-2,-1], [-1, -1],[0, -1],[1, -1],[2,-1],
         [-2,-2], [-1, -2],[0, -2],[1, -2],[2,-2]
         ]
        
        if Tile.city != None:
            self.MAO.printl( "Can't found city: City already present!")
            return
        if Tile.owner!=owner and Tile.owner !=None:
            self.MAO.printl( "Can't found city: Tile belongs to another player!")
            return
        
        for T in gt.get(Tile.x,Tile.y,self.MAO.map1.map,PT=PT):
            if T.city != None: 
                self.MAO.printl( "Can't found city: Too close to another City!")
                return
            
        self.owner = owner      
        self.name = owner.name[:2]+str(len(self.owner.cities))
        self.tile=Tile
        self.tile.owner=self.owner
        self.tile.city=self
        self.owner.cities.append(self)
        self.pop=1        
        self.first_ring=gt.get(self.tile.x,self.tile.y,self.MAO.map1.map)
        self.MAO.tile_renderer(self.tile)
    
    def destroy(self):
        tmp_tile=self.tile
        self.tile.city=None
        self.owner.cities.remove(self)
        self.MAO.tile_renderer(tmp_tile)
        

        
        

                

        

            





        
