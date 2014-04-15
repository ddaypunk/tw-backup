"""
Battleship Game
By: ddaypunk06

Program will print a 5x5 game board each time the player guesses
the coordinates.  Player has 4 turns to sink the battle ship

TO ADD:
* Ability to make more than one ship
** NO overlap
** Dynamic gameboard based on number of ships
* Different sized ships
** only vertical or horizontal
** can't go off the board
* Two players

"""
import random

# Create the Board
board = []
for x in range(0,5):
  board.append(["O"] * 5)

# function to remove extra chars
def print_board(board):
  	for row in board:
   		print " ".join(row)

#functions to randomly determine ship coord
def random_row(board):
	return random.randint(0,len(board)-1)

def random_col(board):
	return random.randint(0,len(board[0])-1)


#begin game
print "Let's play Battleship!"
print_board(board)

ship_row = random_row(board)
ship_col = random_col(board)

# loop game for only 4 turns
for turn in range(4):
	print turn + 1
	guess_row = input("Guess Row:")
	guess_col = input("Guess Col:")

	if guess_row == ship_row and guess_col == ship_col:
  		print "Congratulations! You sunk my battleship!"
  		break
	else:
		if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
			print "Oops, that's not even in the ocean."
		elif(board[guess_row][guess_col] == "X"):
			print "You guessed that one already."
		else:
			print "You missed my battleship!"
			board[guess_row][guess_col] = "X"
			if turn == 3:
				print "Game Over."
  	print_board(board)