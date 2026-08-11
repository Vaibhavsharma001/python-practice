# Example 1 — 
# Amazon-style: Payment System

# Design a simple payment system using inheritance.

# Create a parent class Payment with a method pay().

# Create two child classes:

# CreditCardPayment
# UPIPayment

# Each child class should implement pay() differently.



class payment:
    def pay(self):
        print("making payment")


class creditcardpayment(payment):
    def pay(self):
        print("payment made using Credit Card")


class UPIpayment(payment):
    def pay(self):
        print("payment made using UPI")