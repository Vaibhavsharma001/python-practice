# |----------------------------------------------------------------------------|
#           Multilevel (inheritance through multiple generations.)
# |----------------------------------------------------------------------------|

# A class inherits from another child class, creating a chain of inheritance.

class animal:
    def eat(self):
        print("eat")
        
        
class mammal(animal):
    pass

class dog(mammal):
    pass


dog().eat()