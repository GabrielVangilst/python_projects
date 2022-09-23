cells = ["-" for __ in range(1,10)]
computer = "x"
player = "0"

def display(cells):
	print(f"\n{cells[0]}|{cells[1]}|{cells[2]}"  )
	print(f"{cells[3]}|{cells[4]}|{cells[5]}"  )
	print(f"{cells[6]}|{cells[7]}|{cells[8]}\n"  )



def spaceIsFree(cells,location):
	return cells[location] == "-"




def playMove(cells,location,piece):
	if spaceIsFree(cells,location):
		cells[location] = piece
		display(cells)

		if checkDraw(cells):
			print("It is a draw!!")
			exit()

		if isWinner(cells):
			if piece == "X":
				print("The computer wins!!")

			else:
				print("You win!!")

			exit()

	else:
		print("invalid spot!!")
		location = int(input("Enter a new position: "))
		playMove(cells, location, piece)




def checkDraw(cells):
	for x in cells:
		if x == "-":
			return False
	return True


def isWinner(cells):
	if cells[0] == cells[1] == cells[2] != "-" :
		return True

	elif cells[3] == cells[4] == cells[5] != "-" :
		return True

	elif cells[6] == cells[7] == cells[8] != "-" :
		return True

	elif cells[0] == cells[3] == cells[6] != "-" :
		return True

	elif cells[1] == cells[4] == cells[7] != "-" :
		return True

	elif cells[2] == cells[5] == cells[8] != "-" :
		return True

	elif cells[0] == cells[4] == cells[8] != "-" :
		return True

	elif cells[2] == cells[4] == cells[6] != "-" :
		return True

	else:
		return False

def checkIfWinner(cells,piece):
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



def playerMove(cells):
	location = int(input("It is your turn! Select a location to play (1-9):"))
	playMove(cells,location,player)

def computerMove(cells):
	bestScore = -1000
	bestMove = 0
	for x in range(9):
		if cells[x] == "-":
			cells[x] = computer
			score = minimax(cells,False)
			cells[x] = "-"
			if score > bestScore:
				bestScore = score
				bestMove = x 

	playMove(cells,bestMove,computer)
	return


def minimax(cells,isMaximizing):
	if checkIfWinner(cells, computer):
		return 1

	elif checkIfWinner(cells, player):
		return -1

	elif(checkDraw(cells)):
		return 0

	if(isMaximizing):
		bestScore = -1000
		for x in range(9):
			if (cells[x] == "-"):
				cells[x] = computer
				score = minimax(cells,False)
				cells[x] = "-"
				if score > bestScore:
					bestScore = score

		return bestScore

	else:
		bestScore = 1000
		for x in range(9):
			if (cells[x] == "-"):
				cells[x] = player
				score = minimax(cells,True)
				cells[x] = "-"
				if score < bestScore:
					bestScore = score



		return bestScore


while not isWinner(cells):
	computerMove(cells)
	playerMove(cells)
