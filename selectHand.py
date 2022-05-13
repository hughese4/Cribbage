from rankSuit import rankSuit

class selectHand():

    def dealPlayerHand():
        print("You have been dealt 6 cards. Choose 2 of them to put into the crib, whether it's you crib or not\n")

        handDict = {"card1": '', "card2": '', "card3": '', "card4": '', "card5": '', "card6": ''}

        print("Your hand is: \n")
        num = 0
        for i in handDict.keys():
            num += 1
            card = rankSuit.randCard()
            handDict[i] = (card[0] + " of " + card[1])
            
        print(handDict)
        print()

        cribCard1 = input("Select the first card to put into the crib (by typing the number in front it).\n> ")
        cribCard2 = input("Select the second card to put into the crib.\n> ")

        #needs to call a method in bothand to select crib cards and send them to crib class
        