from genericboard import Board

class Connect4Board(Board):
	ROWS = 6
	COLUMNS = 7

	WINNER = 4

	def __init__(self):
    		super(Connect4Board,self).__init__(self.ROWS,self.COLUMNS)

	def isWinner(self,character):
		horizontal = super(Connect4Board, self).findConsecutiveInRow(character,self.WINNER)
                vertical = super(Connect4Board, self).findConsecutiveInColumn(character,self.WINNER)
                diagonal = super(Connect4Board, self).findConsecutiveInDiagonal(character,self.WINNER)
		
		if horizontal or vertical or diagonal:
			return True
		return False
