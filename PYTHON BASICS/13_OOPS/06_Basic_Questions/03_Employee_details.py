# Create a class Employee with attributes name, id, and salary. Add a method to display the
# employee details.


class Employee:
    def __init__(self,name,id_no,salary):
        self.name = name
        self.id_no = id_no
        self.salary = salary
    
    def display(self):
        print("\n---Employee details---")
        print(f"employee name:-- {self.name}")
        print(f"this is your id_no:--{self.id_no}")
        print(f"salary:---{self.salary}")   
            
data = Employee(
    name = input(" enter your name:-"),
    id_no = int(input("enter your id no--")),
    salary = int(input("enter your salary--"))
)     

data.display()