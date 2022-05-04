import random

class starter():

    def lowerCard(playerCard):
        botCard = random.randrange(1, 13)
        """if playerCard == 11 :
            playerCard = "jack"
        elif playerCard == 12:
            playerCard = "queen"
        elif playerCard == 13:
            playerCard = "king"

        if botCard == 11 :
            botCard = "jack"
        elif botCard == 12:
            botCard = "queen"
        elif botCard == 13:
            botCard = "king" """

        print("Your card is a " + str(playerCard))
        print("The bot's card is a " + str(botCard))
        print()

        if botCard < playerCard:
            print("The bot gets the crib first")
        else:
            print("You get the first crib")
        print()
    
    def intro():
        print("\nWelcome to cribbage.\n")
        print("Press c to pick a card. Whoever gets a lower card value goes first")
        playerInput = input("> ")
        again = True
        while again == True:
            if playerInput == "c" or "C":
                again = False
                playerCard = random.randrange(1, 13)
                starter.lowerCard(playerCard)
            else:
                print("Please press c to continue.")

    
        