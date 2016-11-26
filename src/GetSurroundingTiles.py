class GetSurroundingTiles():
    
    def __init__(self):
        pass    
    
    def GST(self,x,y,map,attr=None,PT = [[-1, 1],  [0, 1],  [1, 1],
                                        [-1, 0],           [1, 0],
                                        [-1, -1], [0, -1], [1, -1]]):
            tiles = []
            for t in PT:
                try:
                    if x + t[0] >= 0 and y + t[1] >= 0:
                        if map[x + t[0]][y + t[1]] is None:
                            pass
                        else:
                            if attr != None:           
                                tiles.append(getattr(map[x + t[0]][y + t[1]],attr))
                                tiles.sort(reverse=True)
                            else: 
                                tiles.append(map[x + t[0]][y + t[1]])
                           
                except:
                    pass
            
            return tiles
        
