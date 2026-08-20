# PRODUCT

# Create a Product class containing:
# •	Product_name 
# •	Price 
# •	Quantity 

# Create a method:
# Total_price()

# It should calculate:
# price × quantity

# Take all three values from the user and create the object.
# Trick: The user enters the price and quantity, but the total should be calculated by the object.


class Product:
    def __init__(self,Product_name,Price,Quantity):
        self.Product_name = Product_name
        self.price = Price
        self.quantity = Quantity
        
    def Total_price(self):
        return self.price * self.quantity
        

data = Product(
    input("enter your product name:--"),
    float(input("enter price:--")),
    int(input("enter quantity:--"))
)
        

print(f"Product name: {data.Product_name}")
print(f"Product price:-{data.price}")
print(f"Quantity: {data.quantity}")
print(f"Total Price: {data.Total_price()}")