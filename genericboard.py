import numpy as np

class Board(object):
	EMPTY = ' '
	ERROR = -1
	COLUMN_DIVIDER = ' | '
	ROW_DIVIDER = '-'

	def __init__(self,rows, columns):
		self.board = []
		self.rows = rows
		self.columns = columns
		self.freeSpaces = rows * columns

		for i in xrange(0,rows):
			self.board.append([])
      			for j in xrange(0, columns):
				self.board[i].append(self.EMPTY)

	def printBoard(self):
		columns = list(xrange(1,self.columns+1))
		print ' ' + self.COLUMN_DIVIDER + self.COLUMN_DIVIDER.join([str(i) for i in columns])
		i = 1

		rowDivider = ''
		for j in xrange(1, self.columns*4+3):
			rowDivider+=self.ROW_DIVIDER

		print rowDivider

		for row in self.board:
	        	print str(i)+ self.COLUMN_DIVIDER + self.COLUMN_DIVIDER.join(row)
			print rowDivider
			i+=1

	def checkColumnInput(self,input):
		if input < 0 or input > self.columns-1:
        		return self.ERROR
		return input

	def checkRowInput(self,input):
                if input < 0 or input > self.rows-1:
                        return self.ERROR
                return input

	def getAvailableRow(self,board,column):
		for i in xrange(self.rows-1,-1,-1):
			for j in xrange(0,self.columns):
                		if j == column:
					if self.board[i][j] == self.EMPTY:
						return i
		return self.ERROR 
	
	def markBoard(self,row,column,character):
		self.board[row][column] = character
		self.freeSpaces -= 1


	def getColumns(self):
		return self.columns

        def getRows(self):
                return self.rows

	def getSpacesLeft(self):
		return self.freeSpaces

	def findConsecutiveInRow(self,character,count):
		if count > self.rows:
			return -1			
		
		seen = 0
		for i in range(0,self.rows):
			for j in range(0,self.columns):
				if j == 0:
					seen = 0
				if self.board[i][j] == character:
					seen+=1
				else:
					seen=0
				if count == seen:
					return True
		return False		
			
        def findConsecutiveInColumn(self,character,count):
                seen = 0
                for i in range(0,self.columns):
                        for j in range(0,self.rows):
				# reset the count at each row
				if j == 0:
					seen = 0
				if self.board[j][i] == character:
                                        seen+=1
                                else:
                                        seen=0
                                if count == seen:
                                        return True
                return False				

	def findConsecutiveInDiagonal(self,character,count):
		# http://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python
		a = np.array(self.board)

		diags = [a[::-1,:].diagonal(i) for i in range(-a.shape[0]+1,a.shape[1])]
		diags.extend(a.diagonal(i) for i in range(a.shape[1]-1,-a.shape[0],-1))

		diagList = [n.tolist() for n in diags]
		needChecking = []

		for n in diagList:
			if len(n) >= count:
				needChecking.append(n)

		for needs in needChecking:
			seen = 0
			for need in needs:
				if need == character:
					seen+=1
				else:
					seen = 0
				if seen == count:
					return True
                return False
