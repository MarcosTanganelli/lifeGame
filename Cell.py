class Cell:
    def __init__(self, life = False):
        self.life = life
    
    def getLife(self):
        return self.life
    
    def setLife(self, valor):
        self.life = valor