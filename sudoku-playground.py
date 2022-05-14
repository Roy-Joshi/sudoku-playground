from sudoku_file_input import SudokuFileInput
import print_sudoku

puzzles = SudokuFileInput(10)

print_sudoku.PrintSudoku.print(puzzles.sudoku_puzzles[0])