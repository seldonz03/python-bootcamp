


class Payment:
    def __init__(self,initial_amount = 0):
        self.amount = initial_amount
    def valid(self):
        return self.amount >= 0

class CashPayment(Payment):

    def __init__(self, amount, currency):
        super().__init__(amount)
        self.currency=currency
    def valid(self):
        return super().valid() and self.currency =="PH"

class CardPayment(Payment):

    def __init__(self, amount, cardnumber):
        super().__init__(amount)
        self.card=cardnumber
    def valid(self):

        return super().valid() and self.card

class Coupon(Payment)
    def __init__(self, amount, expired:
        super().__init__amount >= 0)


