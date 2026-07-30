# PYTHON SETS

# A set stores unique values.
# Sets are unordered and mutable.

# Important Points
# 1. Sets are unordered.
# 2. Duplicate values are not allowed.
# 3. Sets are mutable.
# 4. Elements must be immutable.
# 5. Sets don't support indexing.
# 6. Use set() to create an empty set.
# 7. {} creates an empty dictionary.

                                                            # Creating a Set
fruits = {"apple", "banana", "orange"}
print(fruits)

                                                                  # Empty Set
set1 = set()
print(set1)

                                                     # Duplicate values are removed automatically
numbers = {10, 20, 30, 20, 10, 40} 
print(numbers)

                                                             # Different Data Types
data = {10, "Python", 5.5, True}
print(data)

                                                      # Length of Set
colors = {"red", "blue", "green"}
print(len(colors))

                                                       # Checking Item
animals = {"lion", "tiger", "cat"}
print("lion" in animals)
print("dog" in animals)

                                                           # add()
cars = {"BMW", "Audi"}
cars.add("Toyota")
print(cars)

                                                           # update()
cities = {"Delhi", "Mumbai"}
cities.update(["Jaipur", "Pune"])
print(cities)

                                                           # remove()
books = {"Python", "Java", "C++"}
books.remove("Java")
print(books)

                                                        # discard()
games = {"Cricket", "Football", "Hockey"}
games.discard("Football")
print(games)

                                                           # pop()
letters = {"A", "B", "C"}
letters.pop()
print(letters)

                                                           # clear()
subjects = {"Math", "Science", "English"}
subjects.clear()
print(subjects)

                                                           # del
set2 = {1, 2, 3}
del set2

                                                       # Loop Through Set
fruits = {"apple", "banana", "mango"}

for item in fruits:
    print(item)

                                                           # copy()
set1 = {1, 2, 3}
set2 = set1.copy()
print(set2)

                                                            # union()
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))

                                                          # intersection()
a = {1, 2, 3}
b = {2, 3, 4}
print(a.intersection(b))

                                                            # difference()
a = {1, 2, 3}
b = {2, 3, 4}
print(a.difference(b))

                                                        # symmetric_difference()
a = {1, 2, 3}
b = {2, 3, 4}
print(a.symmetric_difference(b))

                                                             # issubset()
a = {1, 2}
b = {1, 2, 3, 4}
print(a.issubset(b))

                                                             # issuperset()
a = {1, 2, 3, 4}
b = {1, 2}
print(a.issuperset(b))

                                                              # isdisjoint()
a = {1, 2}
b = {3, 4}
print(a.isdisjoint(b))

                                                            # Set Comprehension
square = {num ** 2 for num in range(1, 6)}
print(square)

                                                               # frozenset()
set1 = frozenset([1, 2, 3, 4])
print(set1)
