#   Name: Chris Chavez
#   Date: 13 JULY 2021
#   Class: CMPSC 132
#   Description: Program deals a random card from a deck of cards. 

import random



class Card: 
	def __init__(self, suit, val):
		self.suit = suit
		self.value = val

	def show(self): 
		print("{} of {}".format(self.value, self.suit))


# Construct Deck with 52 cards, 4 suits and 13 cards per suit
class Deck: 
	def __init__(self):
		self.cards = []
		self.build()

	def build(self): 
		for s in ["Clubs (♣)", "Diamonds (♦)", "Hearts (♥)", "Spades (♠)"]:
			for v in range(1, 14):
				if v <= 10:
					self.cards.append(Card(s, v))
				elif v == 11:
					self.cards.append(Card(s, "Jack"))
				elif v == 12: 
					self.cards.append(Card(s, "Queen"))
				elif v == 13:
					self.cards.append(Card(s, "King"))

	def shuffle(self): 
		for i in range(len(self.cards) -1, 0, -1):
			r = random.randint(0, i)
			self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

	def drawCard(self):
		return self.cards.pop()

	def show(self): 
		for c in self.cards: 
			c.show()

class Player: 
	def __init__(self, name):
		self.name = name 
		self.hand = []
		#self.intro = print("This program allows you to pick a set number of randomly dealt cards. ")
		#self.num = int(input("Please input an integer/whole\nnumber between 40: \n"))

	def draw(self, deck):
		self.hand.append(deck.drawCard())
		return self

	def showHand(self): 
		for card in self.hand:
			card.show() 


if __name__ == '__main__':

	deck = Deck()
	deck.shuffle()

	intro = print("This program allows you to pick a set number of randomly dealt cards. ")
	num = int(input("Please input an integer/whole\nnumber between 40: \n"))
    
	for i in range(len(num)):
		chris.draw(deck) 

	chris = Player("Chris")
	#chris.draw(deck) 
	chris.showHand() 


"""

"""
