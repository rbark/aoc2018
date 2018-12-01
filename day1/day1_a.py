with open('input') as file:
    puzzle = file.readlines()

def solvePuzzle():
    frequncy = 0
    for line in puzzle:
        if (line[0] == '+'):
            frequncy += int((line[1:]))
        else:
            frequncy -= int((line[1:]))
    print(frequncy)


solvePuzzle()