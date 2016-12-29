import AI

class NewPlayer:

    def __init__(self, name, color,MAO,AI_type='random'):

        self.name = name
        self.color = color
        self.armies = []
        self.cities = []        
        self.AI=AI.AI_Player(MAO,self,AI_type)
