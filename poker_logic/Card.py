class Card:
    def __init__(self,rank,suit):
        acceptedRanks=['2', '3', '4', '5', '6', '7','8', '9', '10', 'J', 'Q', 'K', 'A']
        acceptedSuits=['♠', '♥', '♦', '♣']

        if not isinstance(suit,str):
            raise TypeError(f"Suit expected to be a string got {type(suit).__name__}")
        if not isinstance(rank, str):
                        raise TypeError(f"Suit expected to be a string got {type(rank).__name__}")
        
        rankUpper = rank.upper()
        if rankUpper in acceptedRanks:
               pass
        else:
                raise TypeError(f"Suit expected to be a string got {type(rank).__name__}")
        
        self.rank = rankUpper
        self.suit = suit

    def printCard(self):
           print("Rank",self.rank)
           print("Suit",self.suit)

if __name__ == "__main__":
       card1=Card(suit="♠", rank = "a")
       card1.printCard()

       card2=Card(suit="♦", rank = "j")
       card2.printCard()