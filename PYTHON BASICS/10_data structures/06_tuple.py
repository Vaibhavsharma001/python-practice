# A tuple in Python is an ordered, immutable collection of items. Once a tuple is created, you cannot change, add, or remove its elements.

                         # Creating Tuples
# Empty tuple
t1 = ()

# Tuple with elements
t2 = (1, 2, 3)

# Tuple without parentheses
t3 = 4, 5, 6

# Single-element tuple (comma is required)
t4 = (10,)


                        #  Accessing Elements
numbers = (10, 20, 30, 40)

print(numbers[0])   
print(numbers[-1])  


                          # Slicing
nu = (10, 20, 30, 40, 50)
print(nu[1:4])  


                         # Tuple Operations
a = (1, 2)
b = (3, 4)

print(a + b)     
print(a * 3)      
print(2 in a)     


                          # Tuple Methods
# Tuples have only two built-in methods

t = (1, 2, 2, 3, 4)
print(t.count(2))   # 2
print(t.index(3))   # 3



                       # Packing and Unpacking
# Packing
person = ("Alice", 25, "Engineer")

# Unpacking
name, age, job = person

print(name)           # alice
print(age)            # 25
print(job)            # engineer


                         # Nested Tuples
nested = ((1, 2), (3, 4), (5, 6))

print(nested[1])     # (3, 4)
print(nested[1][0])  # 3
