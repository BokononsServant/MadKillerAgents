import random
import Map
import Agent
import time

map1=Map.Map()

pop1=Population.Population(map1,8)    


##    print(agnt.position)
    
for i in range(0,50):
    for agnt in pop1.Members:
        agnt.move(random.randint(-1,1),random.randint(-1,1))
        pop1.spawn(agnt)
        map1.drawMap(pop1.Members)
        print("")
        
        
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
