import random

class Coin:
    # The _ _init_ _ method initializes the
    # sideup data attribute with 'Heads'

    def __init__(self) -> None:
        self.sideup = 'Heads'
    
    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'
        
    # The get_sideup method returns the value
    # referenced by sideup.   

    def get_sideup(self):
        return self.get_sideup