from PegBoard import PegBoard as pb
from selectHand import selectHand
from starter import starter
from botHand import botHand

class PlayCribbage:

    def __init__(self) -> None:
        pass

    """calls methods that introduce the game and determines who gets the first crib"""
    def whoGoesFirst(self):
        starter.intro()

    def playGame(self):
        selectHand.dealPlayerHand()
        botHand.dealBot()

    def main(self):
        #self.printBrd()

        #call beginning sequence
        self.whoGoesFirst()
        self.playGame()
    
    
# Using the special variable 
# __name__
if __name__=="__main__":
    PC = PlayCribbage()
    PC.main()