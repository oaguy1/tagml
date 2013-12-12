import xml.etree.ElementTree as et
import worldmap as wm
import player as ply
from random import randrange

class Parser(object):

    def __init__(self, docname):
        self.docname = docname
        self.worldmap = None
        self.intro = ""

        try:
            open(docname)
        except IOError:
            print('File', docname, 'does not exist, aborting program')
            quit(1)

    def trim(self, string):
        return " ".join(string.split())

    def isEmpty(self, string):
        return string is None or string.isspace()

    def parse_enemy(self, node):
        if 'name' in node.attrib.keys():
            if self.isEmpty(node.attrib['name']):
                print('Tag "enemy" required attribute "name" to be non-empty')
                quit(1)
            else:
                name = node.attrib['name']

        if 'armor' in node.attrib.keys():
            if self.isEmpty(node.attrib['armor']):
                print('Tag "enemy" required attribute "armor" to be non-empty')
                quit(1)
            else:
                AC = int(node.attrib['armor'])

        if 'health' in node.attrib.keys():
            if self.isEmpty(node.attrib['health']):
                print('Tag "enemy" required attribute "health" to be non-empty')
                quit(1)
            else:
                HP = int(node.attrib['health'])
        
        if 'attack' in node.attrib.keys():
            if self.isEmpty(node.attrib['attack']):
                print('Tag "enemy" required attribute "attack" to be non-empty')
                quit(1)
            else:
                max_attack = node.attrib['attack']        
        
        return ply.Character(worldmap = self.worldmap, 
                name = name, 
                AC = AC, 
                HP = randrange(1, HP + 1),
                max_attack = max_attack)

    def parse_encounter(self, node):
        enemies = []

        tree_iter = node.iter()

        for current in tree_iter:
            if current.tag == 'enemy':
                enemies.append(self.parse_enemy(current))
        
        return enemies

    def parse_cell(self, node, i, j):
        map_node = self.worldmap.getNode(i, j)
        
        if self.isEmpty(node.text): 
            print('Map cell {0}:{1} must contain a description'.format(i, j))
            quit(1)
        else:
            desc = self.trim(node.text)
            map_node.setDesc(desc)

        tree_iter = node.iter()

        for current in tree_iter:
            if current.tag == 'encounter':
                enemies = self.parse_encounter(current)
                map_node.setEnemies(enemies)

    def parse_map(self, node):
        rows = int(node.attrib['rows'])
        cols = int(node.attrib['cols'])

        if 'startrow' in node.attrib.keys():
            startrow = int(node.attrib['startrow'])
        else:
            startrow = 0

        if 'startcol' in node.attrib.keys():
            startcol = int(node.attrib['startcol'])
        else:
            startcol = 0

        self.worldmap = wm.WorldMap(rows = rows, cols = cols, 
                start_row = startrow, start_col = startcol)

        tree_iter = node.iter()
        i = -1
        j = 0

        for current in tree_iter:
            if current.tag == 'row':
                i += 1
                j = 0
            elif current.tag == 'cell':
                self.parse_cell(current, i, j)
                j += 1


    def parse_game(self, node):
        tree_iter= node.iter()

        for current in tree_iter:
            if current.tag == 'map':
                self.parse_map(current)
            if current.tag == 'intro':
                if self.isEmpty(current.text):
                    print('Empty "intro" tag, tag must have text or be removed')
                    quit(1)
                else:
                    self.intro = self.trim(current.text)

    def parse(self):
        tree = et.parse(self.docname)
        root = tree.getroot()
        tree_iter = tree.iter()

        if root.tag != 'tagml':
            print('Document error: does not open with tagml tag')
            quit(1)

        for current in tree_iter:
            if current.tag == 'game':
                self.parse_game(current)
            elif current.tag == 'meta':
                pass

        return {'worldmap':self.worldmap, 'intro':self.intro}
