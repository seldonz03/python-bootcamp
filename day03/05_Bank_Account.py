
class BankAccount:
    def __init__(self, balance = 0):
        self._bal = balance


    def deposit(self, amount):
        if amount < 0:
            print("We cannot deposit negative amounts ")
        else:
            self._bal += amount

    def withdraw(self, amount):
        if amount < 0:
            print("We cannot withdraw negative amounts ")
        elif amount > self._bal:
            print("We cannot withdraw more than the balance ")
        else:
            self._bal -= amount


    def print_balance(self):
        print(self._bal)



