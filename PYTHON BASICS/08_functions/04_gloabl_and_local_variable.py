
# Local variables are defined inside a function and exist only during its execution. They cannot be accessed from outside the function.

def greet():
    msg = "Hello from inside the function!"
    print(msg)

greet()

#example 2

def greet():
    msg = "Hello!"
    print("Inside function:", msg)


# Global Variables
# Global variables are declared outside all functions and can be accessed anywhere in the program, including inside functions.

msg = "Python is awesome!"

def display():
    print("Inside function:", msg)

display()
print("Outside function:", msg)
