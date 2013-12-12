import worldmap as wm
import parser
import player
import game
import sys


def main():
    if len(sys.argv) != 2:
        print ("Proper usage: python", sys.argv[0], "/path/to/tagml/file")
        return

    tagml_parse = parser.Parser(sys.argv[1])
    parse_result = tagml_parse.parse()

    worldmap = parse_result[0][1]

    player_name = str(input("What is your name? "))
    user = player.Player(worldmap, name = player_name)

    game_loop = game.Game(worldmap, user)

    print("Thank you for using TagML")

if __name__ == "__main__":
    main()
