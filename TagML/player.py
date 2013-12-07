class Player(object):
    
    def __init__(self, worldmap, name = " ", startx = 0, starty = 0):
        self.worldmap = worldmap
        self.name = name
        self.pos_x = startx
        self.pos_y = starty

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getPos(self):
        return {'cols' : self.pos_x, 'rows' : self.pos_y}

    def moveNorth(self):
        if self.worldmap.inBounds(self.pos_x, self.pos_y - 1):
            self.pos_y -= 1
            return True
        else:
            return False

    def moveSouth(self):
        if self.worldmap.inBounds(self.pos_x, self.pos_y + 1):
            self.pos_y += 1
            return True
        else:
            return False

    def moveEast(self):
        if self.worldmap.inBounds(self.pos_x + 1, self.pos_y):
            self.pos_x += 1
            return True
        else:
            return False

    def moveWest(self):
        if self.worldmap.inBounds(self.pos_x - 1, self.pos_y):
            self.pos_x -= 1
            return True
        else:
            return False
