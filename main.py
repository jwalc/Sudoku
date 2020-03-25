

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
        pass

    def check_columns(self):
        pass

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

    def __repr__(self):
        pass


class Solver:

    def __init__(self):
        pass

