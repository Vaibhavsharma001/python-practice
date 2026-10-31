class dog:
    species = "canine"
    
    def __init__(self,name,age):
        self.name= name
        self.age = age
        

dog1 = dog(input('enter name--'),int(input("enter age--")))

print(dog1.name)
print(dog1.age)
print(dog1.species)


# Explanation:

# class Dog: creates a class named Dog, which acts as a blueprint for dog objects.
# species is a class attribute, meaning it is shared by all instances of the class.
# self refers to the current object, allowing each object to store and access its own data.
# init_() is a constructor method that runs automatically when a new object is created. It is used to initialize object data.
# self.name and self.age are instance attributes, unique to each Dog object created from the class.