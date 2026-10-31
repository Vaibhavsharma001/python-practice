# Write a class "calculator" capable of finding square, cube and square root of a
# number.

class Calculator:
    def __init__(self,number):
        self.number = number
        
    def calculate(self):
        square = self.number ** 2
        cube = self.number ** 3
        square_root = self.number ** 0.5
        print("Square:", square)
        print("Cube:", cube)
        print("Square Root:", square_root)

data = Calculator(
    number = int(input("enter your number:-"))
)

data.calculate()
