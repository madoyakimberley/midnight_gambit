class Card:
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['♠', '♥', '♦', '♣']

    def __init__(self, rank, suit):
        if not isinstance(suit, str):
            raise TypeError(f"Suit expected to be a string, got {type(suit).__name__}")
        if not isinstance(rank, str):
            raise TypeError(f"Rank expected to be a string, got {type(rank).__name__}")
        
        rankUpper = rank.upper()
        if rankUpper not in self.ranks:
            raise ValueError(f"Invalid rank: {rankUpper}")
        
        self.rank = rankUpper
        self.suit = suit

   #Returns the card a readable string
    def __str__(self):
       
        return f"{self.rank}{self.suit}"

    def print_card(self):
        print("Rank", self.rank)
        print("Suit", self.suit)

if __name__ == "__main__":
    card1 = Card(suit="♠", rank="a")
    print(card1) 
