# |-------------------------------------------------------------------------|
                                #WITH INHERITANCE
# |-------------------------------------------------------------------------|

class animal:
    def eat(self):
        print('can eat')
        
    def sleep(self):
            print("can sleep")
            
class dog(animal):
    pass

class cat(animal):
    pass


dog = dog()

dog.eat()
dog.sleep()

# |---------------------------------------------------------------------|
                              #WITHOUT INHERITANCE 
# |---------------------------------------------------------------------|
class dog:
    def eat(self):
        print('dog can eat')
        
    def sleep(self):
        print('dog can sleep')
        
        
class cat:
    def eat(self):
        print('cat can eat')
        
    def sleep(self):
        print('cat can sleep')
        
        
d1= dog()
c1=cat()  

print(d1.eat())
print(c1.eat())