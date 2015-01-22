import random

standardDeckChoices = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

class GeneratePlayer():
    def __init__(self, name, money, hand):
        self.name = name
        self.money = money
        self.hand = hand

def drawCards(deck):
	"""

	Accepts param of current deck in use,
	Returns two cards from aforementioned deck

	"""

	card1 = deck[random.randrange(0, len(deck))]
	card2 = deck[random.randrange(0, len(deck))]

	return card1, card2

def highCard(p1name, p2name, p1hand, p2hand):
	"""

	Accepts params of player names & player hands.
	Runs a card comparison algorithm to determine winner.
	Returns winner, and their name, respectively.

	"""
	player1 = list(p1hand)
	player2 = list(p2hand)

	#just a test conditional
	if player1[0] == "A" or player1[1] == "A":
		print("%s wins!" % p1name)


def main():
	testPlayer1 = GeneratePlayer("TJ Steele", 500, drawCards(standardDeckChoices))
	testPlayer2 = GeneratePlayer("Jason Schindler", 500, drawCards(standardDeckChoices))

	#print testPlayer1.name, list(testPlayer1.hand)
	#print testPlayer2.name, list(testPlayer2.hand)

	highCard(testPlayer1.name, testPlayer2.name, testPlayer1.hand, testPlayer2.hand)


if __name__ == "__main__":
	main()