import worldmap as wm
import parser
import player
import sys

def __init__():
    if len(sys.argv) != 2:
        print ("Proper usage: python", sys.argv[0], "/path/to/tagml/file")
        return

    tagml_parse = parser.Parser(sys.argv[1])
    parse_result = tagml_parse.parse()

    worldmap = parse_result[0][1]

    cont = True

    user = player.Player(worldmap)
    user_pos = user.getPos()

    print(worldmap.getNode(user_pos['rows'], user_pos['cols']).getDesc())
    
    while cont:
        response = str(input("What will you do next? "))
        response = response.lower()

        user_wants_to_move = False
        user_moved = False

        if response == "north" or response == "n":
            user_wants_to_move = True
            user_moved = user.moveNorth()
        elif response == "south" or response == "s":
            user_wants_to_move = True
            user_moved = user.moveSouth()
        elif response == "east" or response == "e":
            user_wants_to_move = True
            user_moved = user.moveEast()
        elif response == "west" or response == "w":
            user_wants_to_move = True
            user_moved = user.moveWest()
        elif response == "quit" or response == "exit" or response == "q":
            cont = False
        else:
            print("Not a proper command")

        if user_wants_to_move and user_moved:
            user_pos = user.getPos()
            print(worldmap.getNode(user_pos['rows'], user_pos['cols']).getDesc())
        elif user_wants_to_move:
            print("Cannot move further in that direction")

__init__()
