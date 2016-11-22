cnt=0

class newCity:
    
    def __init__(self,plyr,x,y,map):
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
        
    def FirstRing(self):
        self.workedTiles=[]
        #self.workedTiles.append(map[x])