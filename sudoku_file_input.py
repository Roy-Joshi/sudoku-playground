import csv


class SudokuFileInput:
    sudoku_puzzles = []
    sudoku_solutions = []
    sudoku_puzzles_str = []
    sudoku_solutions_str = []
    number_of_puzzles = 10

    def __init__(self, number_of_puzzles):
        filename = "sudoku.csv"
        fields = []
        rows = []

        with open(filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            fields = next(csvreader)
            for row in csvreader:
                rows.append(row)

        for row in rows[:number_of_puzzles]:
            self.sudoku_puzzles_str.append(row[0])
            self.sudoku_solutions_str.append(row[1])

        for item in self.sudoku_puzzles_str:
            int_puzzle_list = []
            for character in item:
                int_puzzle_list.append(int(character))
            self.sudoku_puzzles.append(int_puzzle_list)

        for item in self.sudoku_solutions_str:
            int_solution_list = []
            for character in item:
                int_solution_list.append(int(character))
            self.sudoku_solutions.append(int_solution_list)