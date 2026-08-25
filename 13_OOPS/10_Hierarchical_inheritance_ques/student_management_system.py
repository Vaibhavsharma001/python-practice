# Question: Create a Python program for a school system using hierarchical inheritance.

# Create a base class Person with attributes name and age.
# Create two child classes, Student and Teacher, that inherit from Person.
# In Student, add student_id and course attributes.
# In Teacher, add employee_id and subject attributes.
# Create suitable methods to display the details of a student and a teacher.
# Create one object of Student and one object of Teacher, then display their details.
# Print the MRO of both child classes.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

    def display_student(self):
        self.display_person()
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")


class Teacher(Person):
    def __init__(self, name, age, employee_id, subject):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.subject = subject

    def display_teacher(self):
        self.display_person()
        print(f"Employee ID: {self.employee_id}")
        print(f"Subject: {self.subject}")


# Create a Student object
student = Student("vaibhav", 20, "S101", "Python Programming")

# Create a Teacher object
teacher = Teacher("aditi", 35, "T501", "Computer Science")

print("Student Details")
print("---------------")
student.display_student()

print("\nTeacher Details")
print("---------------")
teacher.display_teacher()

print("\nMRO of Student:")
print(Student.mro())

print("\nMRO of Teacher:")
print(Teacher.mro())
