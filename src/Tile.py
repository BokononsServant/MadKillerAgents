class Tile:
    
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.owner = None
        self.surrounding_tiles = []
        self.label = None
        self.army = None
        self.city = None


