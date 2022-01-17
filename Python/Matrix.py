class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        row_list = self.matrix_string.split("\n")
        for idx, row in enumerate(row_list):
            row = list(row.split(" ")) 
            if idx+1 == index:
                return self.int_format(row)

    def column(self, index):
        column = []
        column_list = self.matrix_string.split("\n")
        for row in column_list:
            row = list(row.split(" "))
            column.append(row[index-1])
        return self.int_format(column)

    def int_format(self, result):
        int_list = []
        for char in result:
            int_list.append(int(char))
        return int_list