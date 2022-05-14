from sudoku_file_input import SudokuFileInput
from print_sudoku import PrintSudoku
import time


startTime = time.time()

puzzles = SudokuFileInput(10)
PrintSudoku.printSudoku(puzzles.sudoku_puzzles[0])

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))