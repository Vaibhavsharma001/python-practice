# |------------------------------------------------------------------------------|
#             Hierrarchical inheritance(one parent-->multiple children)
#|-------------------------------------------------------------------------------| 

# A combination of two or more types of inheritance.

class animal:
    def eat(self):
        print("eat")
        
class dog(animal):
    pass

class cat(animal):
    pass


dog.eat()
cat.eat()