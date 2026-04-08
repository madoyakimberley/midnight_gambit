import random
from Card import Card

class Deck():
    def __init__(self):
        self.deck = []
        for rank in Card.ranks:
            for suit in Card.suits:
                card = Card(suit=suit, rank=rank)
                self.deck.append(card)

    def shuffle(self):
        newDeck = []
        deck_to_shuffle = self.deck 
        
        while len(deck_to_shuffle) > 0:
            n = random.randint(0, len(deck_to_shuffle) - 1)
            card = deck_to_shuffle.pop(n)
            newDeck.append(card)
        
        self.deck = newDeck 

    def print_deck(self):
        for card in self.deck:
            card.print_card() 
            print("---------------------")

    def burn_card(self):
        print("--- Burning Top Card ---")
        burned_card = self.deck.pop(0) 
        return burned_card

    def give_card(self):
        if len(self.deck) > 0:
            return self.deck.pop(0)
        else:
            print("Deck is empty!")
            return None


if __name__ == "__main__":
    deck1 = Deck()
    deck1.shuffle()
    card = deck1.give_card()
    print("Given Cards:")
    card.print_card()
    deck1.print_deck()