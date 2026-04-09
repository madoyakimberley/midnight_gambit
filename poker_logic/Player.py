import random
import time

class Player():
    def __init__(self, game, type="pc", cards=None, total_amount_bet=0, name="", amount=0):
        self.game = game # Reference to the Game instance
        self.name = name
        self.type = type
        # Using None as default to avoid shared list issues
        self.cards = cards if cards is not None else []
        self.total_amount_bet = total_amount_bet
        self._amount = amount  # Protected variable for the setter

    #getter----->data wrapping data controlling how it behaves(encapsulation ;))
    @property
    def amount(self):
        return self._amount

    #setter------> check if amount is -ve :)
    @amount.setter
    def amount(self, value):
        if value < 0:
            print(f"Warning: {self.name} is out of money!")
            self._amount = 0
        else:
            self._amount = value

    def place_initial_bet(self):
        """Handles human input for the initial bet."""
        while True:
            amount_input = input(f"Place Initial Bet Amount. Current Balance: {self.amount}: ")

            if amount_input.isdigit():
                number = int(amount_input)
                if 0 < number <= self.amount:
                    self.amount -= number 
                    self.update_amount_bet(number)
                    return number
                else:
                    print(f"Invalid amount. Must be between 1 and {self.amount}.")
            else:
                print("Please enter a valid whole number.")

    

    def auto_match_or_raise(self, amount):
        print("PC thinking. What to do....")
        time.sleep(2)
        
        to_do = random.randint(1, 2)
        # The raise amount is the call amount + a random raise
        raise_amount = amount + random.randint(10, 250)

        # Force a match (1) if the PC can't afford the raise
        if raise_amount > self.amount:
            to_do = 1

        # Logic for Matching (Call)
        if to_do == 1:
            if self.amount > amount:
                #trying to do a decrement to actually change the amount
                self.amount -= amount
                print(f"Matching your action. Bet {amount}")
                return amount
            else:
                return "lose"

        # Logic for Raising
        self.amount = self.amount - raise_amount
        print("I have a good feeling. I raise by ", raise_amount)
        return raise_amount

    def update_amount_bet(self, amount):
        self.total_amount_bet = self.total_amount_bet + amount

    def reset_amount_bet(self):
        self.total_amount_bet = 0
