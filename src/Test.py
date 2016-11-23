class Til:

 def __init__(self, x, y, value):
  self.x = x
  self.y = y
  self.value = value

 def get_neighbors(self, map):
  self.neighbors = []

        PT=[[-1,1 ],[0, 1],[1,1],
            [-1,0 ],       [1,0],
            [-1,-1],[0,-1],[1,-1]]

        for t in PT:
            try:
                if self.x+t[0]>=0 and self.y+t[1]>=0:
                    if map[self.x+t[0]][self.y+t[1]] is None: pass
                    else:
                        self.neighbors.append(map[self.x+t[0]][self.y+t[1]])
                        #self.neigbors.sort(reverse=True)
            except:
                pass

     return neigbors