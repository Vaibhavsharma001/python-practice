# A dictionary stores data in key : value pairs.
# Dictionaries are mutable, so we can add, update or remove data.

# ----------------------------------------------------------
# Empty dictionary
# ----------------------------------------------------------

student = {}

print(student)


# ----------------------------------------------------------
# Creating a dictionary
# ----------------------------------------------------------

student = {
    "name": "Vaibhav",
    "age": 19,
    "course": "Python"
}

print(student)


# ----------------------------------------------------------
# Dictionary with different data types
# ----------------------------------------------------------

person = {
    "name": "Vaibhav",
    "age": 19,
    "height": 5.9,
    "student": False
}

print(person)


# ----------------------------------------------------------
# Accessing values
# ----------------------------------------------------------

car = {
    "brand": "Toyota",
    "model": "Fortuner"
}

print(car["brand"])
print(car["model"])


# ----------------------------------------------------------
# Using get()
# ----------------------------------------------------------

book = {
    "title": "Python",
    "price": 499
}

print(book.get("title"))

# Key doesn't exist
print(book.get("author"))

# Default value
print(book.get("author", "Not Found"))


# ----------------------------------------------------------
# Adding new item
# ----------------------------------------------------------

mobile = {
    "brand": "Lenovo"
}

mobile["price"] = 30000

print(mobile)


# ----------------------------------------------------------
# Updating a value
# ----------------------------------------------------------

laptop = {
    "brand": "Dell",
    "ram": "8GB"
}

laptop["ram"] = "16GB"

print(laptop)


# ----------------------------------------------------------
# Removing item using pop()
# ----------------------------------------------------------

fruits = {
    "apple": 120,
    "banana": 50,
    "orange": 80
}

fruits.pop("banana")

print(fruits)


# ----------------------------------------------------------
# Removing last Item
# ----------------------------------------------------------

country = {
    "India": 91,
    "USA": 1,
    "Japan": 81
}

country.popitem()

print(country)


# ----------------------------------------------------------
# Removing item using del
# ----------------------------------------------------------

course = {
    "name": "Python",
    "duration": "3 Months"
}

del course["duration"]

print(course)


# ----------------------------------------------------------
# Clearing Dictionary
# ----------------------------------------------------------

game = {
    "Vaibhav": 80,
    "Aditi": 75
}

game.clear()

print(game)


# ----------------------------------------------------------
# Length of dictionary
# ----------------------------------------------------------

movie = {
    "name": "Interstellar",
    "year": 2014,
    "rating": 8.7
}

print(len(movie))


# ----------------------------------------------------------
# Checking if key exists
# ----------------------------------------------------------

user = {
    "username": "vaibhav",
    "password": "12345"
}

if "username" in user:
    print("Key Found")

print("password" in user)
print("email" in user)


# ----------------------------------------------------------
# keys()
# ----------------------------------------------------------

animals = {
    "lion": "Wild",
    "cow": "Domestic",
    "dog": "Pet"
}

print(animals.keys())


# ----------------------------------------------------------
# Loop through keys
# ----------------------------------------------------------

marks = {
    "Math": 95,
    "Science": 90,
    "English": 88
}

for key in marks:
    print(key)


# ----------------------------------------------------------
# values()
# ----------------------------------------------------------

marks = {
    "Math": 90,
    "Science": 88,
    "English": 95
}

print(marks.values())


# ----------------------------------------------------------
# Loop Through Values
# ----------------------------------------------------------

temp = {
    "Morning": 25,
    "Afternoon": 35,
    "Night": 28
}

for value in temp.values():
    print(value)


# ----------------------------------------------------------
# items()
# ----------------------------------------------------------

computer = {
    "CPU": "Intel i5",
    "RAM": "16GB",
    "Storage": "512GB SSD"
}

print(computer.items())


# ----------------------------------------------------------
# Loop Through Keys and Values
# ----------------------------------------------------------

employee = {
    "Vaibhav": 45000,
    "Paritosh": 52000,
    "Aditi": 48000
}

for key, value in employee.items():
    print(key, value)


# ----------------------------------------------------------
# update()
# ----------------------------------------------------------

bank = {
    "name": "Vaibhav",
    "balance": 5000
}

bank.update({"balance": 8000})

print(bank)


# ----------------------------------------------------------
# copy()
# ----------------------------------------------------------

dict1 = {
    "language": "Python",
    "version": 3.13
}

dict2 = dict1.copy()

print(dict2)


# ----------------------------------------------------------
# setdefault()
# Adds the key only if it is not present.
# ----------------------------------------------------------

student = {
    "name": "Vaibhav"
}

student.setdefault("age", 19)

print(student)


# ----------------------------------------------------------
# fromkeys()
# ----------------------------------------------------------

subjects = ["Math", "Science", "English"]

marks = dict.fromkeys(subjects, 0)

print(marks)


# ----------------------------------------------------------
# Nested Dictionary
# ----------------------------------------------------------

school = {
    "student1": {
        "name": "Vaibhav",
        "age": 15
    },
    "student2": {
        "name": "Bob",
        "age": 16
    }
}

print(school["student1"]["name"])


# ----------------------------------------------------------
# Dictionary with List
# ----------------------------------------------------------

cart = {
    "customer": "Vaibhav",
    "items": ["Milk", "Bread", "Butter"]
}

print(cart)


# ----------------------------------------------------------
# Dictionary with Tuple
# ----------------------------------------------------------

location = {
    "city": "Haryana",
    "coordinates": (28.61, 77.20)
}

print(location)


# ----------------------------------------------------------
# Dictionary Comprehension
# ----------------------------------------------------------

squares = {
    num: num ** 2
    for num in range(1, 6)
}

print(squares)


# ----------------------------------------------------------
# Sorting Dictionary Keys
# ----------------------------------------------------------

marks = {
    "Vaibhav": 80,
    "Aditi": 95,
    "Paritosh": 90
}

for key in sorted(marks):
    print(key, marks[key])


# ----------------------------------------------------------
# Dictionary Methods
# ----------------------------------------------------------

# clear()       - Removes all items
# copy()        - Returns a copy
# get()         - Returns value of a key
# items()       - Returns key-value pairs
# keys()        - Returns all keys
# values()      - Returns all values
# pop()         - Removes a key
# popitem()     - Removes last inserted item
# update()      - Updates dictionary
# setdefault()  - Adds key if not present
# fromkeys()    - Creates a new dictionary


# ----------------------------------------------------------
# Important Points
# ----------------------------------------------------------

# 1. Dictionary stores data in key : value pairs.
# 2. Keys must be unique.
# 3. Values can be duplicated.
# 4. Dictionaries are mutable.
# 5. Keys can be strings, numbers or tuples.
# 6. Values can be any data type.
# 7. Dictionaries keep insertion order (Python 3.7+).
# 8. Values are accessed using keys, not indexes.