class PrintSudoku:

    def __init__(self):
        return

    def printSudoku(puzzle):
        print("    1 2 3   4 5 6   7 8 9")
        print("    ---------------------")
        for i in range(len(puzzle)):
            if i % 9 == 0:
                print(int(i / 9) + 1, end=' | ')
            print(puzzle[i], end =" ")
            if (i + 1) % 9 == 0:
                print()
            elif (i + 1) % 3 == 0:
                print ("|", end=' ')
            if (i + 1) % 27 == 0:
                print ("    ---------------------")
        print()