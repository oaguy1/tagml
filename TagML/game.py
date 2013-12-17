import player
import worldmap
import operator
from random import randrange


class Game(object):

    def __init__(self, worldmap, player):
        self.worldmap = worldmap
        self.player = player
        self.game_loop()

    def encounter(self, enemies):
        print("You are being attacked!")
        print()

        init_roll = {'player': randrange(1, 21)}
        fighters = []
            
        for enemy in enemies:
            init_roll[enemy.getName()] = randrange(1, 21)

        for fighter in sorted(init_roll, key=init_roll.get, reverse=True):
            fighters.append(fighter)

        keep_fighting = True

        while keep_fighting:
            for fighter in fighters:
                current_fighter = fighter
                
                if current_fighter == 'player':
                    response = str(input('What will you do next? '))
                    if 'attack' in response:
                        self.player.attack(enemies[0])
                        if enemies[0].isDead():
                            fighters.remove(enemies[0].getName())
                            enemies.remove(enemies[0])
                            print("You won the encounter")
                    elif 'run' in response:
                        dice_roll = randrange(1, 21)
                        if dice_roll >= 15:
                            print("You escaped!")
                            keep_fighting = False
                            return
                        else:
                            print('Couldn\'t escape')
                    elif 'kill' in response:
                        enemies[0].setHP(0)
                        if enemies[0].isDead():
                            fighters.remove(enemies[0].getName())
                            enemies.remove(enemies[0])
                            print("You won the encounter!")
                else:
                    for enemy in enemies:
                        if enemy.getName() == current_fighter:
                            if not enemy.isDead():
                                enemy.attack(self.player)
                                if self.player.isDead():
                                    print("You died")
                                    quit(0)

                if not enemies:
                    keep_fighting = False

    def enter_mapnode(self, row, col):

        current_node = self.worldmap.getNode(row, col)
        
        print(current_node.getDesc())
        
        if current_node.hasEncounter():
            self.encounter(current_node.getEnemies())
            print()

    def game_loop(self):

        start_row = self.worldmap.getStartRow()
        start_col = self.worldmap.getStartCol()

        self.player.setPos(start_row, start_col)
        self.enter_mapnode(start_row, start_col) 

        cont = True

        while cont:
            response = str(input("What will you do next? "))
            response = response.lower()
            
            player_wants_to_move = False
            player_moved = False

            if response == "north" or response == "n":
                player_wants_to_move = True
                player_moved = self.player.moveNorth()
            elif response == "south" or response == "s":
                player_wants_to_move = True
                player_moved = self.player.moveSouth()
            elif response == "east" or response == "e":
                player_wants_to_move = True
                player_moved = self.player.moveEast()
            elif response == "west" or response == "w":
                player_wants_to_move = True
                player_moved = self.player.moveWest()
            elif response == "quit" or response == "exit" or response == "q":
                cont = False
            else:
                print("Not a proper command")

            if player_wants_to_move and not player_moved: 
                print("Cannot move further in that direction")

            if cont and player_moved:
                player_pos = self.player.getPos()
                row = player_pos['row']
                col = player_pos['col']
                print()
                self.enter_mapnode(row, col)
