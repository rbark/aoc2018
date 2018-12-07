import re
from collections import defaultdict

id = 1
inch_from_left = 4
inch_from_top = 5
width = 7
heigt = 8

words = "#123 @ 3,2: 5x4"
matris = defaultdict(int)


with open('input') as file:
    puzzle = file.readlines()


def tokenizer(area):
    tokens = re.split("[# @ , x :]", area)
    return tokens[id], tokens[inch_from_left], tokens[inch_from_top], tokens[width], tokens[heigt]
    # print(tokens)

def populate_matris():
    over_lap_cell = 0
    for line in puzzle:
        id, x,y, w, h= tokenizer(line)
        for i in range(int(w)):
            for j in range(int(h)):
                x_coord = str(int(x)+i)
                y_coord = str(int(y)+j)
                matris[str(x_coord + ',' + y_coord)] += 1

    for line in puzzle:
        correct = True
        id, x,y, w, h= tokenizer(line)
        for i in range(int(w)):
            for j in range(int(h)):
                x_coord = str(int(x)+i)
                y_coord = str(int(y)+j)
                if matris[str(x_coord + ',' + y_coord)] > 1:
                    correct = False

        if correct:
            print(line)






populate_matris()
