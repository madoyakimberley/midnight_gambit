class Player():
    def __init__(self,type="pc", cards=[], total_amount_bet=0,name="" ,amount=0):
        self.name=name
        self.type=type
        self.cards=cards
        self.total_amount_bet=total_amount_bet
        self.amount=amount
        #human,pc