import random

class AI_Player():
    
    def __init__(self,MAO,plyr,AI_type):
        self.MAO=MAO
        self.plyr=plyr
        self.AI_type=AI_type
    
    def play_turn(self):
        if self.AI_type=='random':self.play_turn_random()
        if self.AI_type=='human':self.play_turn_human()

    def play_turn_random(self):
        for army in self.plyr.armies:
            if 
            
            
            mvmnt=army.surrounding_tiles
            for tile in mvmnt:
                if tile.value==3:mvmnt.remove(tile)
            mvmnt.Append(army.tile)
            mvmnt=random.choice(mvmnt)
                    
                
    def play_turn_human(self):
        pass
                
                
            
    