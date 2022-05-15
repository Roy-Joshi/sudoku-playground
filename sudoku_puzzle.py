class SudokuPuzzle:
    puzzle = []
    solution = []
    emptyCells = 0

    def __init__(self, puzzle, solution):
        self.puzzle = puzzle
        self.solution = solution
        self.emptyCells = puzzle.count(0);

    # return 0 for correct, 1 for incorrect, -1 for error
    def updatePuzzle(self, row, column, digit):
        if row > 9 or row <= 0:
            print("Row is invalid. Must between 1-9")
            return -1
        if column > 9 or row <= 0:
            print("Column is invalid. Must between 1-9")
            return -1
        if digit > 9 or digit <= 0:
            print("Digit is invalid. Must between 1-9")
            return -1

        position = 9 * (row - 1) + (column - 1)
        if self.puzzle[position] != 0:
            print("Position based on row and column is filled")
            return -1

        if self.solution[position] != digit:
            print("Wrong answer")
            return 1

        print("Correct answer")
        self.puzzle[position] = digit
        self.emptyCells -= 1
        return 0