with open('input') as file:
    puzzle = file.readlines()



def solvePuzzle():
    frequncies = set()
    duplicateFound = False;
    frequncy = 0

    while not duplicateFound:
        for line in puzzle:
            if (line[0] == '+'):
                frequncy += int((line[1:]))
            else:
                frequncy -= int((line[1:]))

            number_unique = len(frequncies)
            frequncies.add(frequncy)
            if(number_unique == len(frequncies)):
                print(frequncy)
                duplicateFound = True
                break




solvePuzzle()