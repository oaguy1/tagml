class WorldMapNode(object):

    def __init__(self):
        self.desc = ""
        self.enemies = []

    def setDesc(self, string):
        self.desc = string

    def getDesc(self):
        return self.desc

    def __str__(self):
        return self.desc

    def addEnemy(self, enemy):
        self.enemies.append(enemy)

    def removeEnemy(self, enemy):
        self.enemies.remove(enemy)

    def  hasEncounter(self):
        if not self.enemies:
            return False
        else:
            return True

    def getEnemies(self):
        return self.enemies

class WorldMap(object):

    def __init__(self, rows, cols, start_row = 0, start_col = 0):
        self.map_data = {}
        self.rows = rows
        self.cols = cols
        self.start_row = start_row
        self.start_col = start_col

        for i in range(rows):
            for j in range(cols):
                self.map_data[(i, j)] = WorldMapNode()

    def __str__(self):
        return_string = ""

        for i in range(self.rows):
            for j in range(self.cols):
                return_string += str(self.map_data[(i, j)]) + " "
            if i != (self.rows - 1):
                return_string += '\n'

        return return_string

    def getNode(self, row, col):
        return self.map_data[(row, col)]

    def inBounds(self, x, y):
        if x >= 0 and y >= 0 and x < self.cols and y < self.rows:
            return True
        else:
            return False

    def test_fill(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.map_data[(i, j)].setDesc(str(i) + ":" + str(j))

    def getStartCol(self):
        return self.start_col

    def getStartRow(self):
        return self.start_row
