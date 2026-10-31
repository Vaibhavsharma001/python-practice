# In Python, an iterator is an object that produces values one at a time. Iterators are what make for loops work behind the scenes.

#EXAMPLE

numbers = [10, 20, 30,40]

my_iterator = iter(numbers)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))