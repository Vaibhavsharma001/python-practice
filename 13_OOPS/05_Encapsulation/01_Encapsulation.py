#--------------------------------------------------------------------------|
                         # 1.Encapsulation in Python
#--------------------------------------------------------------------------|

# Encapsulation is one of the important concepts of Object-Oriented Programming (OOP) in Python.

# 1. What is Encapsulation?

# Encapsulation means wrapping data (variables) and methods (functions) together inside a class.
# It also helps us control access to data so that important data cannot be changed directly from outside the class.

# HINDI
# Encapsulation ka matlab hai data (variables) aur methods (functions) ko ek class ke andar wrap karna.
# Iska use hum data ko directly outside access ya modify hone se control karne ke liye karte hain.

# Simple Example

# Imagine a Bank Account:

# balance + private data
# deposit() - balance ko update karne ka method
# withdraw() - balance se money withdraw karne ka method

# User ko directly balance change nahi karna chahiye. Instead, methods ke through access karna chahiye.



#----------------------------------------------------------|
             # 2.Why do we use Encapsulation?
#----------------------------------------------------------|

# Encapsulation provides:

# Data protection
# Controlled access
# Better security
# Code organization
# Easy maintenance
# Hindi


# Encapsulation ke benefits:

# Data protection - data ko protect karta hai.
# Controlled access - data access ko control karta hai.
# Security - important data ko directly modify hone se bachata hai.
# Code organization - code ko properly organize karta hai.
# Easy maintenance - code ko maintain karna easy hota hai.


#----------------------------------------------------------------------------\
                       #3. Access modifiers in python
#-----------------------------------------------------------------------------\
    
    
# Type        |         syntax        |            meaning                                     |
# ---------------------------------------------------------------------------------------------|
# Public      |         'name'        |         anywhere access                                |
# Protected   |         '_name'       |         class aur subclasses ke lie intended           |
# Private     |         '__name'      |         class ke andar direct access ke lie intended   |


#----------------------------------------------------------------------------------|
# 4.public variable
# public variable ko directly class ke bahar access ke skte hain.

class Student:
    def __init__(self, name):
        self._name = name

student = Student("vaibhav")
print(student._name)
#-----------------------------------------------------------------------------------|

#5. Private Variable
# Private variable banane ke liye double underscore __use karte hain

class Student:
    def __init_(self, name):
        self.__name = name

student = Student("vaibhav sharma")

print(student.__name)
# This will give an error similar to:
# AttributeError because
# name is treated as a private attribute through Python's name mangling mechanism.


# -----------------------------------------------------------------|
            # 6. Private Data with Getter and Setter
#------------------------------------------------------------------|
# Encapsulation ka ek common example hai getter and setter methods.
# Code

class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

# Getter
    def get_name(self):
        return self.__name

# Setter
    def set_name(self, name):
        self.__name = name

student = Student("vaibhav", 20)

print(student.get_name())

student.set_name("paritosh")

print(student.get_name())


#------------------------------------------example ----------------------------------------
class Student:
    def __init__(self):
        self.__marks = 80

    def show_marks(self):
        print(self.__marks)


s = Student()

s.show_marks()