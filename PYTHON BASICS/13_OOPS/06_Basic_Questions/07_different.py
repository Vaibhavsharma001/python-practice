# Create a class with a class attribute a; create an object from it and set 'a'
# directly using object.a = o. Does this change the class attribute?

class Demo:
    a=2
    
object = Demo()
object.a = 0
    
print(object.a)

#Changing an attribute through an object does NOT change the class attribute. It creates/changes that object's instance attribute.