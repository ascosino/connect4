# Aira Sofia Cosino
#
# A Connect-Four Player class 
#  

from createBoard import Board

# write your class below

class Player:
    """ contructs new Player for Connect 4
    """

    def __init__(self, checker):
        """ contructs a new Player object by initializing the attributes
        checker (a one-character string that represents the gamepiece for
        the player, as specified by the parameter checker) and num_moves
        (an integer that stores how many moves the player has made so far
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        """ returns a string representing a Player object; the string should
        indicate which checker the Player object is using
        """
        return 'Player ' + self.checker

    def opponent_checker(self):
        """ returns a one-character string representing the checker of the
        Player object's opponent; the method may assume that the calling
        Player object has a checker attribute that is either 'X' or '0'
        """
        if self.checker == 'X':
            return '0'
        elif self.checker == '0':
            return 'X'

    def next_move(self, board):
        """ accepts a Board object as a parameter and returns the column
        where the player wants to make the next move
        """
        col = int(input('Enter a column: '))
        while board.can_add_to(col) == False:
            print('Try again!')
            col = int(input('Enter a column: '))
        self.num_moves +=1
        return col
