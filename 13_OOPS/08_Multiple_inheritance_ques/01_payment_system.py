# Payment System

# Suppose a company is building a payment system.

# Create these classes:

# PaymentGateway → has a method process_payment(amount)
# Discount → has a method apply_discount(amount)
# Order → has a method create_order()
# OnlineOrder → inherits from all three classes

# Your OnlineOrder class should:

# Store the order amount.
# Apply a 10% discount.
# Process the discounted amount through the payment gateway.
# Create the order.

# Example expected usage
# order = OnlineOrder(5000)
# order.create_order()
# order.apply_discount(5000)
# order.process_payment(4500)



#PAYMENT SYSTEM

class PaymentGateway:
    def process_payment(self,amount):
        self.amount = amount
        print(f"payment processed:amount {self.amount}")
        
      
class Discount:
    def apply_discount(self,amount):
        self.amount = amount
        
        final_discount = self.amount *10/100
        self.amount = self.amount - final_discount
        return self.amount
        
class Order:
    def create_order(self,amount):
        self.amount = amount
        print("Order created successfully")


class online_order(PaymentGateway,Discount,Order):
    def __init__(self,amount):
        self.amount = amount
    def place_order(self):
         print(f"Original amount: ₹{self.amount}")
         discounted_amount = self.apply_discount(self.amount)
         print(f"Amount after 10% discount: ₹{discounted_amount}")
         self.process_payment(discounted_amount)
         self.create_order(discounted_amount)
         print("Thanks for ordering")
        
order = online_order(1000)  
order.place_order() 
        
    
                