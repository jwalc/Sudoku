

class Sudoku:
    """
    The Sudoku class uses a row-wise string representation of a Sudoku of length 81 where the digit 0 represents empty
    positions. The first digit of the string represents the position at the top-left and the last digit represents the
    bottom right.
    """
    def __init__(self, s_string):
        self.s_string = s_string

    def is_filled(self):
        """
        Returns if the sudoku has any empty positions by checking if there are any 0s in the string.
        :return: boolean
        """
        return "0" not in self.s_string

    def is_valid(self):
        """
        Checks if the Sudoku is valid, meaning there is no filled position defying the standard Sudoku-rules
        :return: boolean
        """
        pass

    def check_rows(self):
        """
        Checks if all rows of the Sudoku are valid.
        :return: boolean
        """
        for i in range(9):
            row = self.filter_empties(self.row(i))
            if len(row) != len(set([d for d in row])):
                return False
        return True

    def check_columns(self):
        """
        Checks if all columns of the Sudoku are valid.
        :return: boolean
        """
        for j in range(9):
            column = self.filter_empties(self.column(j))
            if len(column) != len(set([d for d in column])):
                return False
        return True

    def check_blocks(self):
        pass

    def row(self, i):
        """
        Returns the (i+1)-th row of the sudoku
        :param i: int; row index (0-8)
        :return: str; the i+1-th row of the sudoku
        """
        return self.s_string[9*i:9*(i+1)]

    def column(self, j):
        """
        Returns the (j+1)-th column of the sudoku as a string
        :param j: int; column index (0-8)
        :return: str; the (j+1)-th column of the sudoku
        """
        return self.s_string[j::9]

    def block(self, i, j):
        """
        Returns the 3x3 block that the position (i, j) belongs to.
        :param i: int; row index (0-8)
        :param j: int; column index (0-8)
        :return: str; block
        """
        block = ""
        for r in range(3*(i//3), 3*((i//3)+1)):
            block += self.row(r)[3*(j//3):3*((j//3)+1)]
        return block

    @staticmethod
    def filter_empties(s):
        """
        Returns a string of digits without 0s
        :param s: str; string containing digits
        :return: str; a string without 0s
        """
        return "".join([d for d in s if d != "0"])

    def __repr__(self):
        pass


class Solver:

    def __init__(self):
        pass

