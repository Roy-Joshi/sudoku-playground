class PrintSudoku:

    def __init__(self):
        return

    def printSudoku(puzzle):
        print()
        for i in range(len(puzzle)):
            print(puzzle[i], end =" ")
            if (i + 1) % 9 == 0:
                print()
            elif (i + 1) % 3 == 0:
                print ("|", end=' ')

            if (i + 1) % 27 == 0:
                print ("---------------------")
        print()