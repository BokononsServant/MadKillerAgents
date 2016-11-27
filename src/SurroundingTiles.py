class get():
    """
    Instatiate this class to get access to the get function
    """
    
    def __init__(self):
        pass    
    
    def get(self,x,y,map,attr=None,PT = [[-1, 1],  [0, 1], [1, 1],
                                        [-1, 0],           [1, 0],
                                        [-1, -1], [0, -1], [1, -1]]):
            """
            This function returns the content of the tiles surrounding the given coordinates.
            If attr=None the list contains the Tile objects.
            if atrr = 'value' for example, it returns a list of the 'value' atttribute of the surrounding tiles.
            PT is a list of possible tiles, as default those are the 8 tiles directly adjacent to the given coordinates.    
        
            """
            tiles = []
            for t in PT:
                try:
                    if x + t[0] >= 0 and y + t[1] >= 0:
                        if map[x + t[0]][y + t[1]] is None:
                            pass
                        else:
                            if attr != None:           
                                tiles.append(getattr(map[x + t[0]][y + t[1]],attr))
                            else: 
                                tiles.append(map[x + t[0]][y + t[1]])                           
                except:
                    pass    
                        
            return tiles     

            
            
            
        
            