from random import randrange

class Character(object):

    def __init__(self, worldmap, name = " ", AC = 10 + randrange(4), 
            HP = randrange(1, 7), max_attack = 8):
        self.worldmap = worldmap
        self.name = str(name)
        self.AC = int(AC)
        self.HP = int(HP)
        self.max_attack = int(max_attack)

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name
 
    def getHP(self):
        return self.HP

    def setHP(self, HP):
        self.HP = HP

    def getAC(self):
        return self.AC

    def setAC(self, AC):
        self.AC = AC

    def takeDamage(self, damage):
        self.HP -= damage

    def heal(self, hp):
        self.HP += hp

    def isDead(self):
        return self.HP <= 0

    def attack(self, enemy):
        dice_roll = randrange(1,21)
        if dice_roll >= enemy.getAC():
            damage = randrange(self.max_attack)
            enemy.takeDamage(damage)
            print(self.name, "hits", enemy.getName(), "for", damage, "damage")
        else:
            print(self.name, "misses!")

    def __str__(self):
        return_string = self.name + '\n'
        return_string += '=' * len(self.name) + '\n'
        return_string += 'Attack: ' + str(self.max_attack) + '\n'
        return_string += 'Armor: ' + str(self.AC) + '\n'
        return_string += 'Health: ' + str(self.HP)
        return return_string

class Player(Character):
    
    def __init__(self, worldmap, name = " ", start_col = 0, start_row = 0, 
            AC = 10 + randrange(4), HP = randrange(1, 7), max_attack = 8):
        Character.__init__(self, worldmap, name, AC, HP, max_attack)
        self.col = start_col
        self.row = start_row

    def getPos(self):
        return {'col' : self.col, 'row' : self.row}

    def setPos(self, row, col):
        self.row = row
        self.col = col

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
