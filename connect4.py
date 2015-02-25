import connect4board
import sys

PLAYER1_CHARACTER = 'R'
PLAYER2_CHARACTER = 'B'

PLAYER1 = 1
PLAYER2 = 2

INPUT_OFFSET = 1

PLAYER_TURN = 1
board = connect4board.Connect4Board()

TURN_TO_PLAYER = {PLAYER1 : PLAYER1_CHARACTER, PLAYER2 : PLAYER2_CHARACTER}

PROVIDE_VALID_INT_MSG = "Please provide a valid integer between " + str(1) + " and " + str(board.getColumns())
THANKS = "Thanks for playing!"

QUIT = "quit"

print r'Enter "quit" any time to stop the game'
while 1:		
        board.printBoard()
	
	if board.isWinner(PLAYER1_CHARACTER):
		print "Player " + PLAYER1_CHARACTER + " has won!"				
		break
	
	if board.isWinner(PLAYER2_CHARACTER):
		print "Player " + PLAYER2_CHARACTER + " has won!"           
                break

	if board.getSpacesLeft() == 0:
		print "No more spaces left, play again"
                break
						
	print "It is Player " + str(TURN_TO_PLAYER[PLAYER_TURN]) + " turn"
	try:
		rawInput = raw_input()
		if rawInput == QUIT:
			print THANKS
			break
	
		rawInput = int(rawInput)
		playerInput = board.checkColumnInput(rawInput-INPUT_OFFSET)
	except Exception,e:
		print PROVIDE_VALID_INT_MSG
		continue
	
        if playerInput > board.ERROR:
                print "Player " + TURN_TO_PLAYER[PLAYER_TURN] + " picked column " + str(rawInput)
		row = board.getAvailableRow(board, playerInput)
		if row > board.ERROR:
			if PLAYER_TURN == PLAYER1:
				board.markBoard(row,playerInput,PLAYER1_CHARACTER)
				PLAYER_TURN = PLAYER2
			else:
				board.markBoard(row,playerInput,PLAYER2_CHARACTER)
				PLAYER_TURN = PLAYER1
			
		else:
			print "Sorry column " + str(rawInput) + " is full, pick again."
	else:
		print "Sorry but " + str(rawInput) + " is not between " + str(1) + " and " + str(board.getColumns())	
