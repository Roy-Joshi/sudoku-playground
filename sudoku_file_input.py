import csv


class SudokuFileInput:
    sudoku_puzzles = []
    sudoku_solutions = []
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
            self.sudoku_puzzles.append(row[0])
            self.sudoku_solutions.append(row[1])
