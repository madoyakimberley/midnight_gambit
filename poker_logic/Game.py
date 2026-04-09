from Deck import Deck
from Player import Player

class Game():

    
    def __init__(self):
        self.pot = 0
        deck = Deck()
        deck.shuffle()
        deck.shuffle()
        
        human_cards = [deck.give_card(), deck.give_card()]
        pc_card = [deck.give_card(), deck.give_card()]
        
        self.human = Player(type="human",
                            cards=human_cards,
                            total_amount_bet=0,
                            name="John", amount=2000)
        
        self.pc = Player(type="pc",
                         cards=pc_card,
                         total_amount_bet=0,
                         name="Warwick", amount=2000)
        
        self._turn = self.human
        self.deck = deck

    @property
    def turn(self):
        return self._turn

    @turn.setter
    def turn(self, player):
        if isinstance(player, Player):
            self._turn = player
        else:
            raise ValueError("The turn must be assigned to a player object >_<")

    


if __name__ == "__main__":
    game = Game()
    game.deck.print_deck()
    print("This is the deck")
    
    print("Pc cards")
    game.pc.cards[0].print_card()
    game.pc.cards[1].print_card()
    
    print("This is the deck")
    print("Human cards")
    game.human.cards[0].print_card()
    game.human.cards[1].print_card()