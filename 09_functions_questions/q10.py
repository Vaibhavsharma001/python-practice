# Write a function calculator(a, b, operation) that performs:
# + → addition
# - → subtraction
# * → multiplication
# / → division (handle division by zero)



def calculator(a, b, operation):
    if operation=="+":
        return a+b 
    
    elif operation =="-":
        return a-b
    
    elif operation=="*":
        return a*b
    
    elif operation=="/":
        if b==0:
            return "invalid"
        else:
            return a/b
    else:
        return "invalid operation"  

a=eval(input("enter your first number=-"))
b=eval(input("enter your second number=-"))
operation=(input("enter your operations=-"))

print(calculator(a, b,operation))



    
    
    
