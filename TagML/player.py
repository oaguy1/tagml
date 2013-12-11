from random import randrange

class Character(object):

    def __init__(self, worldmap, name = " ", start_col = 0, start_row = 0, 
            AC = 10 + randrange(4), HP = randrange(1, 7), max_attack = 8):
        self.worldmap = worldmap
        self.name = name
        self.col = start_col
        self.row = start_row
        self.AC = AC
        self.HP = HP
        self.max_attack = max_attack

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getPos(self):
        return {'cols' : self.col, 'rows' : self.row}

    def __str__(self):
        return_string = self.name + '\n'
        return_string += '=' * len(self.name) + '\n'
        return_string += "AC :" + str(self.AC) + '\n'
        return_string += "HP :" + str(self.HP)
        return return_string

class Player(Character):

    def moveNorth(self):
        if self.worldmap.inBounds(self.col, self.row - 1):
            self.row -= 1
            return True
        else:
            return False

    def moveSouth(self):
        if self.worldmap.inBounds(self.col, self.row + 1):
            self.row += 1
            return True
        else:
            return False

    def moveEast(self):
        if self.worldmap.inBounds(self.col + 1, self.row):
            self.col += 1
            return True
        else:
            return False

    def moveWest(self):
        if self.worldmap.inBounds(self.col - 1, self.row):
            self.col -= 1
            return True
        else:
            return False

