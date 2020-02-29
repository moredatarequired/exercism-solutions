class Matrix:
    def __init__(self, matrix_string):
        self.data = [[int(v) for v in r.split()] for r in matrix_string.split("\n")]

    def row(self, index):
        return self.data[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self.data]
