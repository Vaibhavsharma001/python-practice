class Student:
    school = "ABC Public School"                  #class  attribute

    def __init__(self, name, age, marks):
       self.name = name                             # Instance Attribute
       self.age = age                                #Instance Attribute
       self.marks = marks
     
student1 = Student("Rahul", 20, 88)
student2 = Student("Priya", 21, 95)


print(student1.name)
print(student1.age)
print(student1.marks)


print(student2.name)
print(student2.age)
print(student2.marks)