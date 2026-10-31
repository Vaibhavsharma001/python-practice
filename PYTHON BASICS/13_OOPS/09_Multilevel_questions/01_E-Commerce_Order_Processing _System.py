# Design a multilevel inheritance-based E-Commerce system in Python.

# Create:

# User → Customer → PremiumCustomer

# Requirements:

# User: store name and email.
# Customer: add customer_id, total_orders, and total_spending.
# PremiumCustomer: calculate discount based on total spending:
# < ₹5,000 → 0%
# ₹5,000–₹9,999 → 10%
# ≥ ₹10,000 → 20%
# Implement place_order(amount) and final_bill(amount).
# Use super() wherever appropriate.

class User:
    def __init__(self,name,email):
        self.name = name 
        self.email= email
        print(f"NAME: {self.name}")
        print(f"E mail: {self.email}")
        
        
class Costumer(User):
    def __init__(self,name,email,costumer_id):
        super().__init__(name,email)
        self.costumer_id = costumer_id
        self.total_orders = 0
        self.total_spendings = 0
        
class Premium_coustmer(Costumer):
    def calculate(self):
        if self.total_spendings < 5000:
            print("Discount applied: 0%")
            return 0

        elif self.total_spendings < 10000:
            print(f"Discount applied: 10%")
            return 10

        else:
            print(f"Discount applied: 20%")
            return 20
            
    def place_order(self,amount):
        self.total_orders+=1
        self.total_spendings += amount
        print(f"Order placed: ₹{amount}")
        
    def final_bill(self,amount):
        discount = self.calculate()
        discount_amount = amount*discount/100
        final_amount = amount - discount_amount
        
        print(f"DISCOUNT: {discount}%")
        print(f"Discount Amount: ₹{discount_amount}")
        print(f"Final Bill: ₹{final_amount}")
        
final = Premium_coustmer(
    name = "vaibhav",
    email = "vaibhav5443@gmail.com",
    costumer_id= 233456,
 
)
final.place_order(10000)

final.final_bill(1000)


         
        