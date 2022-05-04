import random

class rankSuit():

    def randCard():
        suitList = ["hearts", "clubs", "spades", "diamonds"]
        rankList = ["Ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "Jack", "Queen", "King"]
        cardSuit = random.choice(suitList)
        cardRank = random.choice(rankList)

        return (cardRank, cardSuit)