#Example 1 -------->>>>>>>>>>>>>>>

#SAME CLASSES,DIFFERENT DATA TYPES
#INBUILT  FUNCTION

print(len("python"))
print(len([10,20,30]))
print(len((1,2,3,4)))


# Example 2 -------->>>>>>>

#DIFFERENT CLASSES,SAME METHOD

class dog :
    def sound(self):
        print("dog barks")
        
class cat:
    def sound(self):
        print("cat meows")
        
        
d = dog()
c = cat()

d.sound()
c.sound()

 # EXAMPLE 3 -------------------->>>>>>>   
        
#loop with multiple objects

class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

class Cow:
    def sound(self):
        print("Moo")

animals = [Dog(), cat(), Cow()]

for animal in animals:
    animal.sound()

#English

#The same sound() method is called for different objects, and each object responds in its own way.

