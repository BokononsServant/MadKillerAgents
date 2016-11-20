
dimX=2
dimY=2


map=[[[] for y in range(dimY)] for x in range(dimX)]


for x in range(dimX):
    for y in range(dimY):
        map[x][y].append(["X"+str(x)])
        map[x][y].append(["Y"+str(y)])
        
print map[0][0]
