
# |----------------------------------------------------------|
                    #Hybrid Inheritance
# |----------------------------------------------------------|

# Hybrid inheritance is a combination of more than one type of inheritance. It uses a mix like single, multiple, or multilevel inheritance within th
# same program. Python's method resolution order (MRO) handles such cases.


# A combination of two or more inheritance types.


# Python supports Hybrid Inheritance through combinations of single, multiple, and multilevel inheritance.

# |-----------------------------------|
#  | Method Resolution Order (MRO)    |
# |-----------------------------------|


# When using Multiple Inheritance, Python follows the Method Resolution Order (MRO) to decide which method to execute.

# Method Resolution Order (MRO) defines the order in which Python searches for a method in a class and its parent classes. It becomes important when
# same method exists in more than one class in an inheritance chain, especially in multiple inheritance.

# he example shows how Python decides which method to execute when both a parent and a child class have a method with the same name.

# Method Resolution Order (MRO) उस क्रम (order) को तय करता है जिसमें Python किसी क्लास और उसकी पैरेंट क्लास में किसी मेथड को खोजता है। यह तब ज़रूरी हो जाता है जब
# इनहेरिटेंस चेन में एक से ज़्यादा क्लास में एक ही नाम का मेथड हो, खासकर मल्टीपल इनहेरिटेंस के मामले में।

# यह उदाहरण दिखाता है कि Python कैसे तय करता है कि कौन सा मेथड चलाना है, जब पैरेंट और चाइल्ड क्लास, दोनों में एक ही नाम का मेथड हो।

class a:
    def show(self):
        print("class a")
        
class b(a):
    pass

class c(a):
    pass

class d(b,c):
    pass

d= d()
d.show()

print(d.mro())