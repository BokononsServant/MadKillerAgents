import random
import Map
import Agent
import time

map1=Map.Map()
AgentsList=[]
for i in range(0,3):
    AgentsList.append(Agent.Agent(map1))


for agnt in AgentsList:
##    print(agnt.position)
    
    for i in range(0,50):
##        a = random.randint(-1,1)
##        b = random.randint(-1,1)
##        print("Position before move:")
##        print(agnt.position)
##        print("Move horizontal: "+str(a))
##        print("Mover vertical: "+str(b))
##        agnt.move(a,b)
##        print("Position after move:")
##        print(agnt.position)

        
        agnt.move(random.randint(-1,1),random.randint(-1,1))       
        map1.drawMap(AgentsList)
        print("")

##        time.sleep(1)   
##print (agnt.position)
##for i in range(0,10):    
##    Agent1.move(random.randint(-1,1),random.randint(-1,1))
##    print (Agent1.position)
##print (map1.baseMap)
