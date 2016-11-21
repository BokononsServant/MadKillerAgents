import random
import Map
import Agent
import time
import Population


map1=Map.Map()

pop1=Population.Population(map1,8)    
    
# for i in range(0,50):
#     for agnt in pop1.Members:
#         agnt.move(random.randint(-1,1),random.randint(-1,1))
#         pop1.spawn(agnt)
#         map1.drawMap(pop1.Members)
#         print("")
      
      
prnt1 = Agent.Agent(map1)
chld1 = Agent.Child(prnt1)      

print(chld1.health)
