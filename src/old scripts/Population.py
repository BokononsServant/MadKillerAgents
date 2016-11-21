import Agent
import Map
import random


class Population():
    def __init__(self,map,PopSize):
        self.Members = []
        for i in range (0,PopSize):
            self.Members.append(Agent.Agent(map))

    def die (self, agnt):        
        self.Members.remove(agnt)
    def spawn(self,agnt):
        if random.randrange(0,100)<agnt.reproRate:         
            self.Members.append(Agent.Child(agnt))
            agnt.move

            
            
    
    
