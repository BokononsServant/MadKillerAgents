cnt=0

class newCity:
    
    def __init__(self,plyr,x,y,map):
        #if x<0 or y<0 or x>map.
        global cnt        
        self.name = plyr.name[:2]+str(cnt)        
        cnt=cnt+1
        self.pos=[x,y]
        self.pop=1
        map[x][y]['Owner']=plyr
        map[x][y]['Tile'].configure(text="TV: "+str(map[x][y]["TileValue"])+"\n"+"AS: "+str(map[x][y]["Army"])+"\n"+self.name+": "+str(self.pop))
        map[x][y]['Tile'].configure(fg=plyr.color)
        plyr.ownedTiles.append([x,y])
        plyr.cities.append([x,y])
        self.FirstRing(x,y,map)
        
    def FirstRing(self,x,y,map):
        
        self.SurroundingTilesValues=[]
        
        #PT=possible Tiles
        
        PT=[[-1,1 ],[0, 1],[1,1],
            [-1,0 ],       [1,0],
            [-1,-1],[0,-1],[1,-1]]
        
        for t in PT:
            
            try: 
                if x+t[0]>=0 and y+t[1]>=0:
                    if map[x+t[0]][y+t[1]]['TileValue'] == 0: pass
                    else:
                        self.SurroundingTilesValues.append(map[x+t[0]][y+t[1]]['TileValue'])
                        self.SurroundingTilesValues.sort(reverse=True)
            except:
                pass
                

        
#     def addXY(self,T1,T2):
#         """
#         add two coordinates [1,1] + [2,3] = [3,4]
#         """
#         if len(T1)!=2 or len(T2)!=2:
#             print "Error: Not coordinates! Array length !=2!"
#             return "Error: Not coordinates! Array length !=2!"
#         else:
#             try:
#                 T1[0]+1
#                 T1[1]+1
#                 T2[0]+1
#                 T2[1]+1
#             except:
#                 print "Error: Not coordinates! Array Elements not integers!"
#                 return "Error: Not coordinates! Array Elements not integers!"
#             
#             T=[T1[0]+T2[0],T1[1]+T2[1]]
#             return T
        
            





        
