# |----------------------------------------------------------------------------------------|
       #TYPE 2: ---Multiple inheritance(one child inherits from multiple parents)
# |----------------------------------------------------------------------------------------|

# One child class inherits from more than one parent class.

class father:
    def skills(self):
        print("driving")
        
        
class mother:
    def talent(self):
        print("cooking")
        
class child(father,mother):
    pass

c=child()
c.skills()
c.talent()

