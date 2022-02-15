# Blackjack by Gabriel vanGilst



from random import shuffle
from os import system




class Card():
    def __init__(self, suit, value, actual_value=0):
        conversion = {
            "A": 11,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 10,
            "Q": 10,
            "K": 10
            }

        # suit of the card
        self.suit = suit

        # number or letter displayed on the card
        self.value = value

        # numerical value of card used to calculate score
        self.actual_value = conversion[value]


class Deck():
    def __init__(self):
        self.suit = ["♠", "♥", "♣", "♦"]
        self.value = ["A", "2", "3", "4", "5", "6",
                		 "7", "8", "9", "10", "J", "Q", "K"]
        # creates deck full of cards
        self.deck = []
        for x in self.suit:
            for y in self.value:
                self.deck.append(Card(x, y))

    # randomly shuffles deck
    def shuffle(self):
        return shuffle(self.deck)

   	# returns a card while removing it from the deck
    def deal(self):
        return self.deck.pop()

    # checks if deck is empty and resets it if so
    def verify(self):
	    if len(self.deck) == 0:
		    for x in self.suit:
			    for y in self.value:
				    self.deck.append(Card(x, y))
	    self.shuffle()


class Player():

	def __init__(self):
		self.hand = []
		self.score = 0
		self.chips = 500

	# draws cards from deck to hand
	def draw(self, deck):
		self.hand.append(deck.deal())
		self.score += self.hand[-1].actual_value

	# checks for soft aces when busted
	def check(self):
		if self.score > 21:
			for x in self.hand:
				if x.actual_value == 11:
					x.actual_value = 1
					self.score -= 10

	# print cards
	def display_hand(self):
		for x in self.hand:
			print('┌───────┐', end=" ")
		print(" ")
		for x in self.hand:
			if x.value == "10":
				print(f'| {x.value}    |', end=" ")
			else:
				print(f'| {x.value}     |', end=" ")
		print(" ")
		for x in self.hand:
			print('|       |', end=" ")
		print(" ")
		for x in self.hand:
			print(f'|   {x.suit}   |', end=" ")
		print(" ")
		for x in self.hand:
			print('|       |', end=" ")
		print(" ")
		for x in self.hand:
			if x.value == "10":
				print(f'|    {x.value} |', end=" ")
			else:
				print(f'|    {x.value}  |', end=" ")
		print(" ")
		for x in self.hand:
			print('└───────┘', end=" ")
		print(" ")


class Game():

	def __init__(self):
		system("cls")
		print("Blackjack")
		input("\nPress enter to play:")

	# prints score and cards of player and dealer
	def display_score(self,player, dealer):
		system("cls")
		print(f"Your hand:")
		player.display_hand()
		print(f"Your score: {player.score}\n")
		print(f"Dealer's hand:")
		dealer.display_hand()
		print(f"Dealer's score: {dealer.score}\n")

	# resets score and hands
	def reset(self,dealer,player):
		dealer.hand.clear()
		player.hand.clear()
		dealer.score = 0
		player.score = 0

	# main function to play game
	def play(self,dealer,player,new_deck):

		dealer.draw(new_deck)
		for x in range(2):
			new_deck.verify()
			player.draw(new_deck)
		player.check()
		self.display_score(player, dealer)

		# checks if player immediately got a blackjack
		if player.score == 21:
			print("Blackjack!!!! You win!!")
			self.reset(dealer,player)
			return 1


		# players turn
		while player.score < 21:

			answer = input("Do you want to Hit or Stand?(H/S) ").upper()
			if answer == "S":
				break

			new_deck.verify()

			player.draw(new_deck)

			player.check()

			self.display_score(player, dealer)

		if player.score > 21:
			print("You busted!!!! You Lose!!!!")
			self.reset(dealer,player)
			return -1


		# dealers turn (hits as long as hand value is lower than 17)
		while dealer.score < 17:
			new_deck.verify()
			dealer.draw(new_deck)
			dealer.check()

			self.display_score(player, dealer)
			input("Press Enter to continue:")

		if dealer.score > 21:
			print("You win!!! Dealer busted!!")
			self.reset(dealer,player)
			return 1
		elif dealer.score > player.score:
			print("You lose!! Dealer has a better hand!!")
			self.reset(dealer,player)
			return -1
		elif dealer.score == player.score:
			print("It is a tie!!!")
			self.reset(dealer,player)
			return 0
		else:
			print("You win!! You have a better hand!!")
			self.reset(dealer,player)
			return 1

	# function that takes bets and checks if player wishes to continue playing
	def start(self):
		i=0
		new_deck = Deck()
		new_deck.shuffle()
		dealer = Player()
		player = Player()
		while True:
			if player.chips == 0:
				print("\nYou are all out of chips!")
				input("\nPress enter to quit:")
				return 0
			if i>0:
				answer = input("Do you want to keep playing?(Y/N) ")
				if answer =="N":
					return 0

			print(f"\nYour current chip balance: {player.chips}")
			while True:
				bet = int(input("How many chips do you want to bet? "))
				if bet < 0 or bet > player.chips:
					print("Invalid amount\n")
				else:
					break

			# returns chips depending on result of game
			result = self.play(player,dealer,new_deck)
			if result == 1:
				player.chips += bet
			elif result == -1:
				player.chips -= bet
			i+=1





if __name__ == "__main__":
	blackjack = Game()
	blackjack.start()