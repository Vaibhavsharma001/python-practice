#  |---------------------------------------------------------------------------------|
                #TYPE 1:--- Single inheritance (one parent-> one child)
                
# One child class inherits from one parent class.
# |----------------------------------------------------------------------------------|
class animal:
    def eat(self):
        print("eat")
        
        
class dog(animal):
    pass


dog().eat()