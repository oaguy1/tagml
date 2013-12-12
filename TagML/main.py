import worldmap as wm
import parser
import player
import game
import sys


def main():
    if len(sys.argv) != 2:
        print ('Proper usage: python', sys.argv[0], '/path/to/tagml/file')
        return

    tagml_parse = parser.Parser(sys.argv[1])
    parse_result = tagml_parse.parse()

    worldmap = parse_result['worldmap']
    intro = parse_result['intro']

    if intro is not None and len(intro) > 0:
        print(intro)
        print()

    player_name = str(input('What is your name? '))
    user = player.Player(worldmap, name = player_name)

    print()
    print('Here is your character')
    print(user)
    print()

    game_loop = game.Game(worldmap, user)

    print()
    print('Thank you for using TagML')
    print()

if __name__ == '__main__':
    main()
