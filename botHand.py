from rankSuit import rankSuit

class botHand():

    def dealBot():
        """This method deals the bot a hand"""

        print("The bot has been dealt 6 cards. It will put 2 of them into the crib.\n")

        botHandDict = {"card1": '', "card2": '', "card3": '', "card4": '', "card5": '', "card6": ''}

        print("Your hand is: \n")
        num = 0
        for key in botHandDict:
            num += 1
            card = rankSuit.randCard()
            key = (card[0] + " of " + card[1])