# Aira Sofia Cosino
#
# ps9pr1
#

class Board:
    """ creates a board for Connect 4
    """

    def __init__(self, height, width):
        """ constructs a new Board object by initializing height,
        width, and slots
        """
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]

    def __repr__(self):
        """ returns a string representing a Board object
        """
        s = ''
        for r in range(self.height):
            s += '|'
            for c in range(self.width):
                s += self.slots[r][c] + '|'
            s += '\n'

        s += (self.width * 2) * '-' + '-' + '\n'
        for n in range(self.width):
            s += ' ' + str(n)[-1]

        return s

    def add_checker(self, checker, col):
        """ adds checker in column
        """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)
        for r in range(self.height):
            if self.slots[r][col] == ' ':
                r += 1
            elif self.slots[r][col] != ' ':
                break
        self.slots[r - 1][col] = checker

    def reset(self):
        """ reset the Board object on which it is called by setting
        all slots to contain a space character
        """
        for r in range(self.height):
            for c in range(self.width):
                if self.slots[r][c] != ' ':
                    self.slots[r][c] = ' '

    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
        checkers in those columns of the called Board object, 
        starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def can_add_to(self, col):
        """ returns True if it is valid to place a checker in the
        column col on the calling Board object. Otherwise, it should
        return False
        """
        if col < 0 or col >= self.width:
            return False
        elif self.slots[0][col] == ' ':
            return True
        else:
            return False
        
    def is_full(self):
        """ returns True if the called Board object is completely full
        of checkers, and returns False otherwise
        """
        for col in range(self.width):
            if self.can_add_to(col) == True:
                return False
        return True

    def remove_checker(self, col):
        """ removes the top checker from column col of the called Board
        object; if the column is empty, then the method should do nothing
        """
        for r in range(self.height):
            if self.slots[r][col] != ' ':
                self.slots[r][col] = ' '
                break

    def is_win_for(self, checker):
        """ accepts a parameter checker that is either 'X' or '0', and
        returns True if there are four consecutive slots containing
        checker on the board; otherwise, it should return False
        """
        assert(checker == 'X' or checker == 'O')
        if self.is_horizontal_win(checker) == True:
            return True
        elif self.is_vertical_win(checker) == True:
            return True
        elif self.is_down_diagonal_win(checker) == True:
            return True
        elif self.is_up_diagonal_win(checker) == True:
            return True
        else:
            return False

    def is_horizontal_win(self, checker):
        """ checks for a horizontal win for the specified checker
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True

        return False

    def is_vertical_win(self, checker):
        """ checks for a vertical win for the specified checker
        """
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True

        return False

    def is_down_diagonal_win(self, checker):
        """ checks for a downward diagonal win for the specified
        character
        """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                    return True

        return False

    def is_up_diagonal_win(self, checker):
        """ checks for an upward diagonal win for the specified
        character
        """
        for row in range(self.height):
            for col in range(self.height - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                    return True

        return False
