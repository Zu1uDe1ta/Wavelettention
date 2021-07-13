#   Name: Chris Chavez
#   Date: 14 JULY 2021
#   Class: CMPSC 132
#   Description: Program allows user to pick a random card from a deck of cards. 

import random


class Card: 
	def __init__(self, suit, val):
		self.suit = suit
		self.value = val

	def show(self): 
		print("{} of {}".format(self.value, self.suit))

# Construct Deck 
class Deck: 
	def __init__(self):
		self.cards = []
		self.build()

	def build(self): 
		for s in ["Clubs (♣)", "Diamonds (♦)", "Hearts (♥)", "Spades (♠)"]:
			for v in range(1, 14):
				self.cards.append(Card(s, v))

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

	def draw(self, deck):
		self.hand.append(deck.drawCard())
		return self

	def showHand(self): 
		for card in self.hand:
			card.show()



deck = Deck()
deck.shuffle()

bob = Player("Bob")
bob.draw(deck)
bob.showHand()

# Construct a Deck instance, with 52 cards.
#deck = pydealer.Deck()


# deck = clubs + diamonds + hearts + spades 


# 

