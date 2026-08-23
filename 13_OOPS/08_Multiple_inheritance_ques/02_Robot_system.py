# The Challenge: The "Hybrid Multi-Role Robot" System
# Scenario:
# You are building a software system for a high-tech factory. You have different types of robot modules.

# Class Robot: The base class. Every robot has a name and a method work() that returns "Basic processing".
# Class Cleaner: Inherits from Robot. Its work() method should return "Cleaning the floor".
# Class Repairer: Inherits from Robot. Its work() method should return "Fixing machinery".
# Class SuperBot: This is a hybrid robot that inherits from both Cleaner and Repairer.
# The Logical Tasks:
# Method Overriding: Implement the classes such that SuperBot inherits from both.
# The MRO Logic: Without defining a work() method inside SuperBot, which work() method will be called when you run SuperBot().work()? Why?
# Combined Functionality: Now, override the work() method inside SuperBot. It should call the work() methods of both parent classes and combine them into a single string.
# Constructor Logic: Ensure that the name attribute is initialized only once in the base Robot class, even though the inheritance path splits and merges.

class Robot:
    def __init__(self, name):
        self.name = name
        print(f"Robot {self.name} initialized")

    def work(self):
        return "Basic processing"

class Cleaner(Robot):
    def __init__(self, name):
        super().__init__(name)

    def work(self):
        return "Cleaning the floor"

class Repairer(Robot):
    def __init__(self, name):
        super().__init__(name)

    def work(self):
        return "Fixing machinery"

class SuperBot(Cleaner, Repairer):
    def __init__(self, name):
        super().__init__(name)

    def work(self):
        clean_task = Cleaner.work(self)
        repair_task = Repairer.work(self)
        return f"{clean_task} and {repair_task}"


bot = SuperBot("Nexus-6")

print(f"MRO order: {[cls.__name__ for cls in SuperBot.__mro__]}")

print(f"Task: {bot.work()}")