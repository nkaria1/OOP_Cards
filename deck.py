import random
from cards import Card
from property import valid_suits, valid_ranks
class Deck:
	"The Deck class is a collection of 52 cards. "
	def __init__(self):
		self._cards =[ Card(s,n) for s in valid_suits for n in valid_ranks]
		print (self._cards)
		print (len(self._cards))

	def shuffle(self):
		random.shuffle(self._cards)
		print(self._cards)

	def is_card_in_deck(self,card):
		for card_from_deck in self._cards:
			if card.matches(card_from_deck):
				return True
		return False


if __name__ == '__main__':

	deck_of_cards = Deck()
	#deck_of_cards.shuffle()
	my_card_1 = Card("H", "3")
	my_card_2 = Card("H", "1")
	print (my_card_1.matches( my_card_2))
	print ("let's search for :", my_card_1)
	print(deck_of_cards.is_card_in_deck(my_card_2))

