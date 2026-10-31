# Create a parent class Employee with the attributes name, base_salary, and working_days. Add a method calculate_salary() that returns the base salary.

# Create a child class Developer that inherits from Employee. Add the attributes overtime_hours and overtime_rate. Override calculate_salary() so that the final salary is calculated as:
# ---- final_salary = base_salary + (overtime_hours × overtime_rate)----

# If the employee worked fewer than 20 days, reduce the final salary by 10%. If the overtime is more than 40 hours, apply a 5% bonus to the overtime amount.


class Employee:
    def __init__(self, name, base_salary, working_days):
        self.name = name
        self.base_salary = base_salary
        self.working_days = working_days

    def calculate_salary(self):
        return self.base_salary


class Developer(Employee):
    def __init__(self, name, base_salary, working_days, overtime_hours, overtime_rate):
        super().__init__(name, base_salary, working_days)
        self.overtime_hours = overtime_hours
        self.overtime_rate = overtime_rate

    def calculate_salary(self):
        # Base salary + overtime
        overtime_amount = self.overtime_hours * self.overtime_rate
        final_salary = self.base_salary + overtime_amount

        # 5% bonus if overtime is more than 40 hours
        if self.overtime_hours > 40:
            bonus = overtime_amount * 5 / 100
            final_salary = final_salary + bonus

        # 10% reduction if working days are fewer than 20
        if self.working_days < 20:
            reduction = final_salary * 10 / 100
            final_salary = final_salary - reduction

        return final_salary
     

obj=Developer(
    name = input("enter your name:--"),
    base_salary=30000,
    working_days=19,
    overtime_hours=42,
    overtime_rate=200
)
print(f"NAME: {obj.name}")
print(f"Base salary: {obj.base_salary}")
print(f"Working days:{obj.working_days} days")
print(f"Overtime: {obj.overtime_hours} hours")
print(f"Overtime rate: {obj.overtime_rate} rupees ")
print(f"this is your final salary: {obj.calculate_salary()}")
print("Thank you!")