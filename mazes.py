from itertools import cycle, repeat

from maze import Maze

ORIGINAL = Maze(10, 10,
"0001010000"
"0111010101"
"0100000011"
"0110100010"
"0000100110"
"1111100000"
"0000001000"
"1000111010"
"0010001010"
"1100101010") * (2, 2)

OPEN = Maze(20, 20,
"10000000000001000000"
"01000001100010000000"
"01000001000111111000"
"00100011111000000100"
"00100000000000001000"
"00100000001111100000"
"00001000000000100000"
"00110110000000100000"
"00000001110000011110"
"00000100001110000000"
"00000001000001001000"
"00001111111110110010"
"00000100000000000100"
"00011000110000001000"
"00000111000000010000"
"00000000100011100000"
"00000000011100000000"
"00000000110000000000"
"00000000100000000000"
"00000000000000000000")


TIGHT = Maze(20, 20,
"00000000000000000000"
"01111111111111111110"
"00000000110000000000"
"00110111111110011111"
"00100000000000000000"
"00111111111111110010"
"00000000000000000010"
"01001111111111001110"
"10000000000000000000"
"10111111110111011111"
"00000000000000000000"
"11111111111111111110"
"00000000000000000000"
"00000000000000000000"
"01111111111111111111"
"00100100010010010100"
"00100100000010010100"
"00100100010010010100"
"00001110011011010110"
"00000000001000000000"
)

ALL = [ORIGINAL, OPEN, TIGHT]
DOUBLE = [maze * (2, 2) for maze in ALL]

def maze_cycler(mazes, repeats):
    ''' Cycle through mazes.
        e.g. mazes = [A, B, C], repeats = 4
        -> AAAABBBBCCCC
    '''
    for maze in cycle(mazes):
        for instance in repeat(maze, repeats):
            yield instance