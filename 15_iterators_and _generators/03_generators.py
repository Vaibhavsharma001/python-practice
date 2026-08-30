# What is a Generator?

# A generator is a special type of function that gives you values one at a time instead of creating all values at once.

# Think of it like a water tap 🚰:

# Normal function → fills a whole bucket first 🪣
# Generator → gives you water one drop at a time 💧

# Generators use the yield keyword instead of return.

def numbers():
    yield 10
    yield 20
    yield 30

gen = numbers()

print(next(gen))
print(next(gen))
print(next(gen))