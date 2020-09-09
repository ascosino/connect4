# Aira Sofia Cosino
#
# AI Player for use in Connect Four   
#

import random  
from playGame import *

class AIPlayer(Player):

    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AIPlayer object
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        """ returns a string representing an AIPlayer object
        """
        return('Player ' + str(self.checker) + ' (' + str(self.tiebreak) + ', ' + str(self.lookahead) + ')')

    def max_score_column(self, scores):
        """ takes a list scores containing a score for each column of
        the board, and that returns the index of the column with the
        maximum score; if one or more columns are tied for the maximum
        score, the method should apply the called AIPlayer's tiebreaking
        strtegy to break the tie
        """
        indices = []
        highest_score =  max(scores)
        for i in range(len(scores)):
            if scores[i] == highest_score:
                indices += [i]
        if self.tiebreak == 'LEFT':
            return indices[0]
        elif self.tiebreak == 'RIGHT':
            return indices[-1]
        else:
            return random.choice(indices)

    def scores_for(self, board):
        """ takes a Board object board and determines the called AIPlayer's
        scores for the columns in board; returns a list containing one
        score for each column
        """
        scores = [0] * board.width
        for i in range(board.width):
            if board.can_add_to(i) == False:
                scores[i] = -1
            elif board.is_win_for(self.checker) == True:
                scores[i] = 100
            elif board.is_win_for(self.opponent_checker()) == True:
                scores[i] = 0
            elif self.lookahead == 0:
                scores[i] = 50
            elif self.lookahead > 0:
                board.add_checker(self, checker, i)
                opp = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = opp.scores_for(board)
                if max(opp_scores) == 100:
                    scores[i] = 0
                elif max(opp_scores) == 0:
                    scores[i] = 100
                elif max(opp_scores) == 50:
                    scores[i] = 50
                board.remove_checker(i)
        return scores

    def next_move(self, board):
        """ overrides the next_move that is inherited from Player
        """
        score = self.scores_for(board)
        col = self.max_score_column(scores)
        self.num_moves += 1
        return col
