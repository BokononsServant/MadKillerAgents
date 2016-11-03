class Map:
    def __init__(self):
        self.dimension=10
        while self.dimension<0 :
            try:
                self.dimension= int(input("Enter Dimension of the map: "))       
            except:
                print("Enter an integer!")
        self.baseMap = [[0 for x in range(self.dimension)] for x in range(self.dimension)]
    def drawMap(self,AgentsList):
        self.baseMap = [[0 for x in range(self.dimension)] for x in range(self.dimension)]
        for agnt in AgentsList:
            self.baseMap[agnt.position[0]][agnt.position[1]]=1
        for line in self.baseMap:
            print(line)
            
        
        
        
    
    
            
        
            
