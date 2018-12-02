with open('input') as file:
    puzzle = file.readlines()


def solvePuzzle():

    for line_to_compare in puzzle:

        for line in puzzle:
            different = 0
            id = ''
            for j, ch in enumerate(line):

                if ch != line_to_compare[j]:
                    different += 1
                else:
                    id += ch
                if different > 1:
                    break

            if different == 1:
                print(id)
                return


solvePuzzle()
