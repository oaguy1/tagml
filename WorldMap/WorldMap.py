class WorldMapNode(object):

    def __init__(self):
        self.desc = ""

    def setDesc(self, string):
        self.desc = string

    def getDesc(self):
        return self.desc

    def __str__(self):
        return self.desc

class WorldMap(object):

    def __init__(self,rows,cols):
        self.map_data = {}
        self.rows = rows
        self.cols = cols

        for i in range(rows):
            for j in range(cols):
                self.map_data[(i,j)] = WorldMapNode()
                self.map_data[(i,j)].setDesc(str(i) + ":" + str(j))

    def __str__(self):
        return_string = ""

        for i in range(self.rows):
            for j in range(self.cols):
                return_string += str(self.map_data[(i,j)]) + " "
            if i != (self.rows - 1):
                return_string += '\n'
        
        return return_string

    def getNode(self, row, col):
        return self.map_data[(row,col)]

world_map = WorldMap(3,3)
world_map.getNode(1,2).setDesc("There are trees!")
print world_map
