# What is wraps in Python?

# wraps comes from the functools module:

# from functools import wraps

# We mainly use it inside decorators.

# First, the problem

# Suppose we make a decorator:

def my_decorator(func):

    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper


@my_decorator
def greet():
    """This function says hello."""
    print("Hello!")


greet()

# This works perfectly.

# But Python now considers greet to actually be the wrapper function.

# Try:

print(greet.__name__)
print(greet.__doc__)

# You might expect:

# greet
# This function says hello.

# But you'll get something like:

# wrapper
# None

# The original function's information has been lost.

# Enter @wraps

# We fix this using wraps:

from functools import wraps

def my_decorator(func):

    @wraps(func)
    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper

# Now:

@my_decorator
def greet():
    """This function says hello."""
    print("Hello!")

# And:

print(greet.__name__)
print(greet.__doc__)

# Output:

# greet
# # This function says hello.
# # So basically:
# @wraps(func)

# means:

# "Hey Python, this wrapper is representing the original function, so preserve the original function's information."