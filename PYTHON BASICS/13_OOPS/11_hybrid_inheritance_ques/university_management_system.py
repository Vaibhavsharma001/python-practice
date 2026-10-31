# Question: Create a Python program for a university management system using hybrid inheritance.
# Create a base class Person with attributes name and age.
# Create two derived classes, Student and Employee, that inherit from Person.
# Create a class TeachingAssistant that inherits from both Student and Employee.
# Add suitable methods to display personal details, student details, employee details, and teaching-assistant details.
# Create an object of TeachingAssistant and display all its information.
# Use super() where appropriate and print the method resolution order using TeachingAssistant.mro().


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
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")


class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display_employee(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ₹{self.salary}")


class TeachingAssistant(Student, Employee):
    def __init__(self, name, age, student_id, course, employee_id, salary, subject):
        Person.__init__(self, name, age)
        self.student_id = student_id
        self.course = course
        self.employee_id = employee_id
        self.salary = salary
        self.subject = subject

    def display_ta(self):
        self.display_person()
        self.display_student()
        self.display_employee()
        print(f"Teaching Subject: {self.subject}")



ta = TeachingAssistant(
    "vaibhav",
    22,
    "ST101",
    "Computer Science",
    "EMP505",
    30000,
    "Python Programming"
)

print("Teaching Assistant Details")
print("--------------------------")
ta.display_ta()

print("\nMethod Resolution Order:")
print(TeachingAssistant.mro())
