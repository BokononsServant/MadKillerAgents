import random
idnt=0
class Agent:     
    def __init__(self, map):
        self.strength = random.gauss(0,1)
        self.position = [random.randint(0,map.dimension-1),random.randint(0,map.dimension-1)]
        self.reproRate = 2
        self.health = 100
        self.assignedMap = map
        global idnt        
        idnt=idnt +1
        self.identifier = idnt       
        self.age=0
        
        if random.randint(0,1) == 1:
            self.color = "green"
        else:
            self.color = "red"
            
    def move(self, horizontal, vertical):
        self.position= [self.position[0]+horizontal,self.position[1]+vertical]
##        self.position[0] = self.position[0]+horizontal
##        self.position[1] = self.position[1]+vertical
        ##Prevent the Agent from wandering beyond boundaries. If going out of Range it will instead move in the opposite direction.        
        if self.position[0] < 0:
            self.position[0] = self.position[0]+2*abs(horizontal)
        if self.position[0] > self.assignedMap.dimension-1:
            self.position[0]= self.position[0]-2*abs(horizontal)
        if self.position[1]<0:
            self.position[1] = self.position[1] + 2*abs(vertical)
        if self.position[1]>self.assignedMap.dimension-1:
            self.position[1] = self.position[1] - 2*abs(vertical)  

class Child(Agent):
    Agent.__init__(self, self.assignedMap)
    def __init__(self, prnt):    
        self.color=prnt.color
        self.strength=random.gauss(prnt.strength,1)
        self.assignedMap = prnt.assignedMap
        self.color = prnt.color
        global idnt 
        idnt=idnt +1
        self.identifier = idnt 
        self.position=prnt.position
        
        
        
        
            
         


