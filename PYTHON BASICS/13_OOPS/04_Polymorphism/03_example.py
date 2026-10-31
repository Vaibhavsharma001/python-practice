class Payment:
    def pay(self, amount):
        print(f"Processing payment of ₹{amount}")


class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class PayPal(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal")


# Polymorphism
payments = [
    CreditCard(),
    UPI(),
    PayPal()
]

for payment in payments:
    payment.pay(1000)