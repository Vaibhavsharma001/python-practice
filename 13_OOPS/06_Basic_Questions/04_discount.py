# Design a class Laptop with attributes like brand, model, and price. Add a method
# apply_discount() that reduces the price by 10%.


class Laptop:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
        
    def apply_discount(self):
        discount = self.price * 10 / 100
        self.price = self.price - discount
        return self.price
    
data = Laptop(
    brand = input("enter brand name:--"),
    model = int(input("enter your model:--")),
    price = int(input("enter price:--"))
)
data.apply_discount()

print(f"Brand name--{data.brand}")
print(f"model--{data.model}")
print(f"price with 10%discount---{data.price}")

