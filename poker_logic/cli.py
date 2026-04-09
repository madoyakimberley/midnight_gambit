
from Game import Game

def play_game():
    game=Game()

    human=game.human
    pc=game.pc

    game.turn=human
    #request to make bet

    human_amount=human.place_initial_bet()
    human.update_amount_bet(human_amount)

    pc_amount=pc.auto_match_or_raise(human_amount)
    pc.update_amount_bet(pc_amount)

    if pc_amount=="loss":
        print("White flag flown. You Win >_<")
        return

    game.turn=human
    game.pot=pc_amount+human_amount

    

play_game()