from sudoku_file_input import SudokuFileInput
from sudoku_game import SudokuGame


sudokus = SudokuFileInput(10)

game = SudokuGame(sudokus.sudoku_puzzles[0], sudokus.sudoku_solutions[0])
game.PlayGame(3)