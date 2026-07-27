# A function defined inside another function is called an inner function (or nested function). It is used to organize related logic and access variables from the outer function.

def f1():
    s = 'I love GeeksforGeeks'
    def f2():
        print(s)
        
    f2()
f1()



def sq_value(num) :
 return num ** 2

print(sq_value(2))
print(sq_value(-4))