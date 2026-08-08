class Animal:
    
    def eat(self):
        print("Eating ... ")

class Dog(Animal):

    def bark(self):
        print("Dog is barking")

dog = Dog()

dog.eat()
dog.bark()


# example -- Parent and Child Constructor

class Animal:
    
    def _init_(self):
        print("Animal Constructor")


class Dog(Animal):
    

    def _init_(self):
        super() .__init__()

print("Dog Constructor")

dog = Dog()


# Explanation (English)
# super() ._ init_() calls the Parent class constructor.
# Parent constructor runs first, then Child constructor.

# Explanation (Hindi)
# super() ._ init_() Parent Class के Constructor को कॉल करता है।
# पहले Parent Constructor चलता है, फिर Child Constructorl

