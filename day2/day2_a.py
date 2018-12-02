with open('input') as file:
    puzzle = file.readlines()

def solvePuzzle():
    two_times = 0
    three_times = 0

    for line in puzzle:
        my_letters = {}

        for ch in line:
            if my_letters.get(ch) == None:
                my_letters[ch] = 1;
            else:
                my_letters[ch] = my_letters.get(ch) + 1

        two_found = False
        three_found = False

        for k, v in my_letters.items():

            if v == 2 and not two_found:
                two_times += 1
                two_found = True
            if (v == 3 and not three_found):
                three_times += 1
                three_found = True

    print(two_times * three_times)

solvePuzzle()