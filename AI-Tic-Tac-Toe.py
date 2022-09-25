# Tic-Tac-Toe with unbeatable AI by Gabriel vanGilst


# Prints the Tic-Tac-Toe board with any pieces that are occupying any cells of the board
def display(cells):
	print(f"\n{cells[0]}|{cells[1]}|{cells[2]}")
	print("-+-+-")
	print(f"{cells[3]}|{cells[4]}|{cells[5]}")
	print("-+-+-")
	print(f"{cells[6]}|{cells[7]}|{cells[8]}\n")


# Function that accepts any an cell of the board as an argument then checks if the cell is empty
def spaceIsFree(cells,location):
	return cells[location] == "-"



# Function that places a piece in any empty cell of the board
def playMove(cells,location,piece):

	# Checks if the given cell is empty and if so places the given piece there
	if spaceIsFree(cells,location):
		cells[location] = piece

		#prints the board
		display(cells)

		#Checks if the move resulted in a draw and if so prints a message and ends the game
		if checkDraw(cells):
			print("It is a draw!!")
			exit()

		#Checks if the move resulted in a win and if so prints a message stating who won and ends the game
		if isWinner(cells,piece):
			if piece == computer:
				print("The computer wins!!")

			else:
				print("You win!!")

			exit()

	# If the given space was not free the user is asked to give another location to place their piece
	else:
		print("invalid spot!!")
		location = int(input("Enter a new position: "))
		location -= 1
		playMove(cells, location, piece)



# Function that checks if the game is a draw
def checkDraw(cells):

	# If there are no empty cells remaining the game is a draw
	for x in cells:
		if x == "-":
			return False
	return True


# Function that checks if the game has been won
def isWinner(cells,piece):

	# If there are any horizontal, vertical or diagonal lines where each cell is the same piece the game has been won
	if cells[0] == cells[1] == cells[2] == piece:
		return True

	elif cells[3] == cells[4] == cells[5] == piece:
		return True

	elif cells[6] == cells[7] == cells[8] == piece:
		return True

	elif cells[0] == cells[3] == cells[6] == piece:
		return True

	elif cells[1] == cells[4] == cells[7] == piece:
		return True

	elif cells[2] == cells[5] == cells[8] == piece:
		return True

	elif cells[0] == cells[4] == cells[8] == piece:
		return True

	elif cells[2] == cells[4] == cells[6] == piece:
		return True

	else:
		return False


# Function that prompts the user to input a location to play a piece
def playerMove(cells):
	location = int(input("It is your turn! Select a location to play (1-9):"))

	# 1 is subtracted from the input so the user can input 1-9 instead of 0-8
	location -= 1

	# The playMmove function is called with the location the user inputted passed as the location
	playMove(cells,location,player)


# Function where computer picks best move and then plays it
def computerMove(cells):

	# bestScore and bestMove initialized with values that will be replaced
	bestScore = -100 
	bestMove = 0

	# Loops through each cell in the board
	for x in range(9):
		# If the cell is empty the computer plays a move there then calls the minimax function to assign that move a score
		if cells[x] == "-":
			cells[x] = computer
			# calls the minimax function minimizing as the computer has just played a move for itself
			score = minimax(cells,False)
			# Sets that cell as empty again
			cells[x] = "-"
			# If that move resulted in the highest score that move will be set as the best move
			if score > bestScore:
				bestScore = score
				bestMove = x 

	# Computer plays the best move
	playMove(cells,bestMove,computer)
	return


# Recursive algorithm that plays every possible game of Tic-Tac-Toe from a given position to assign a move a score
def minimax(cells,isMaximizing):

	# If a move resulted in a win for the computer a score of 1 is returned
	if isWinner(cells, computer):
		return 1

	# If a move resulted in a loss for the computer a score of -1 is returned
	elif isWinner(cells, player):
		return -1

	# If a move resulted in a draw a score of 0 is returned
	elif(checkDraw(cells)):
		return 0

	# When maximizing the computer is trying to find the move that results in the higest score for the computer
	if(isMaximizing):
		bestScore = -100
		# Loops through each cell in the board
		for x in range(9):
			# If the cell is empty the computer plays a move there then calls the minimax function to assign that move a score
			if (cells[x] == "-"):
				cells[x] = computer
				# calls the minimax function minimizing as the computer has just played a move for itself
				score = minimax(cells,False)
				# Sets that cell as empty again
				cells[x] = "-"
				# If that move resulted in the highest score that score will be set as the best score
				if score > bestScore:
					bestScore = score

		return bestScore


	# When minimizing the computer is trying to find the move the player can play that results in the lowest score for the computer
	else:
		bestScore = 100
		# Loops through each cell in the board
		for x in range(9):
			# If the cell is empty the computer plays a move there then calls the minimax function to assign that move a score
			if (cells[x] == "-"):
				cells[x] = player
				# calls the minimax function maximizing as the computer has just played a move against itself
				score = minimax(cells,True)
				# Sets that cell as empty again
				cells[x] = "-"
				# If that move resulted in the lowest score that score will be set as the best score
				if score < bestScore:
					bestScore = score

		return bestScore




if __name__ == "__main__":
	# Creates a list of the cells of the Tic-Tac-Toe board with each assigned a dash indicating it is blank
	cells = ["-" for __ in range(1,10)]

	# Piece to be used by the computer
	computer = "X"

	# Piece to be used by the player
	player = "O"

	print("\nUnwinnable Tic-Tac-Toe:")

	display(cells)	

	# User is prompted to input if they want to go first
	order = int(input("Enter 1 to go first or 2 to go second: "))

	# If the user's input is invalid they will be stuck in loop until their input is valid
	while(order != 1 and order != 2):
		order = int(input("Invalid Input! Please enter 1 to go first and 2 to go second: "))

	# Switches between player and computer move until game is over
	while True:
		if order == 1:
			playerMove(cells)
			computerMove(cells)

		else:
			computerMove(cells)
			playerMove(cells)
