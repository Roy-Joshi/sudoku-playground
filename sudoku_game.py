from sudoku_puzzle import SudokuPuzzle
from print_sudoku import PrintSudoku


class SudokuGame:
    sudoku_obj: SudokuPuzzle
    total_num_of_tries: int

    def __init__(self, puzzle, solution):
        self.sudoku_obj = SudokuPuzzle(puzzle, solution)

    def PlayGame(self, num_of_tries):
        self.total_num_of_tries = num_of_tries

        while num_of_tries > 0:
            try:
                PrintSudoku.printSudoku(self.sudoku_obj.puzzle)
                print(f"Number of tries remaining: {num_of_tries}")
                print(f"Cells to fill: {self.sudoku_obj.emptyCells}")

                user_input = input("Please enter a row, column, and digit separated by spaces (i.e. '4 8 3'):\n")
                print("--------------------------------------------------------------------------")
                user_input = user_input.replace(' ', '')
                if len(user_input) != 3:
                    print("Too many characters entered, please enter a row, column, and digit separated by spaces (i.e. '4 8 3')")
                    continue

                row = int(user_input[0])
                column = int(user_input[1])
                digit = int(user_input[2])

                result = self.sudoku_obj.updatePuzzle(row, column, digit)
                if result == 1:
                    num_of_tries -= 1

                if (self.sudoku_obj.emptyCells == 0):
                    print("Congrats! You've finished the game")
                    print(f"You made {self.total_num_of_tries - num_of_tries} errors")
                    PrintSudoku.printSudoku(self.sudoku_obj.puzzle)
                    return

            except Exception as error:
                print(f"Error in converting or input {error}")

        print("You lost. Finished number of tries. Better luck next time")
