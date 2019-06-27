#Bank Accont transfer
#Joseph Karl Magnussen - Student ID: H00069811
# Module: CKIT-535 Week 3 - Individual Assignment - Unit Testing

class account:
    def __init__(self, initial_amount):
        self.balance = initial_amount

    def transfer(self, amount, target_acc):
        if self.balance < amount:
            print ("Sorry, you have insuficcient funds.")
            return False
        elif amount < 0:
            print("You can not steal money from other accounts") 
            return False
        else:
            self.balance -= amount
            target_acc.balance += amount
            return True
