import random
from SurroundingTiles import get
import Army

class AI_Player():
    
    def __init__(self,MAO,plyr,AI_type):
        self.MAO=MAO
        self.plyr=plyr
        self.AI_type=AI_type
        self.gt=get()
    
    def play_turn(self):
        if self.AI_type=='random':self.play_turn_random()
        if self.AI_type=='human':self.play_turn_human()

    def play_turn_random(self):
        PT = [
         [-2,2],  [-1, 2], [0, 2], [1, 2], [2,2],
         [-2,1],  [-1, 1], [0, 1], [1, 1], [2,1],
         [-2,0],  [-1, 0],         [1, 0], [2,0],
         [-2,-1], [-1, -1],[0, -1],[1, -1],[2,-1],
         [-2,-2], [-1, -2],[0, -2],[1, -2],[2,-2]
         ]  
        
        for army in self.plyr.armies:
            build_city=True
               
            for T in self.gt.get(army.tile.x,army.tile.y,self.MAO.map1.map,PT=PT):
                if T.city != None or Army.cost_build_city>army.units:
                    build_city=False
            
            if army.tile.city!=None and Army.cost_grow_city[army.tile.city.pop]<=army.units:
                build_city=True

            if build_city==True:
                army.build_city()
            
            if army.units<=0: continue
            
            mvmnt=army.tile.surrounding_tiles
            for tile in mvmnt:
                if tile.value==3:mvmnt.remove(tile)
            mvmnt.append(army.tile)
            mvmnt=random.choice(mvmnt)
            #self.MAO.printl( "Moving army on tile %s %s to %s %s" %(army.tile.x, army.tile.y,mvmnt.x, mvmnt.y))
            army.move(mvmnt)
            
        self.MAO.NewTurn()
                  
    def play_turn_human(self):
        pass
                
                
            
    