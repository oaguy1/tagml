import xml.etree.ElementTree as et
import worldmap as wm

class Parser(object):

    def __init__(self, docname):
        self.docname = docname
        self.worldmap = None

        try:
            open(docname)
        except IOError:
            print('File', docname, 'does not exist, aborting program')
            quit(1)

    def trim(self, string):
        string = " ".join(string.split())
        return string

    def parse_cell(self, node, i, j):
        if node.text is None or node.text.isspace():
            print("Map cell {0}:{1} must contain a description".format(i, j))
            quit(1)
        else:
            desc = self.trim(node.text)
            self.worldmap.getNode(i, j).setDesc(desc)


    def parse_map(self, node):
        rows = int(node.attrib['rows'])
        cols = int(node.attrib['cols'])

        self.worldmap = wm.WorldMap(rows, cols)

        tree_iter = node.iter()
        i = -1
        j = 0

        for current in tree_iter:
            if current.tag == "row":
                i += 1
                j = 0
            elif current.tag == "cell":
                self.parse_cell(current, i, j)
                j += 1


    def parse_game(self, node):
        tree_iter= node.iter()

        for current in tree_iter:
            if current.tag == "map":
                self.parse_map(current)

    def parse(self):
        tree = et.parse(self.docname)
        root = tree.getroot()
        tree_iter = tree.iter()

        if root.tag != "tagml":
            print('Document error: does not open with tagml tag')
            quit(1)

        for current in tree_iter:
            if current.tag == "game":
                self.parse_game(current)
            elif current.tag == "meta":
                pass

        return [('World Map', self.worldmap)]