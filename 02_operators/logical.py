# Logical operators perform Logical AND, Logical OR and Logical NOT operations. It is used to combine conditional statements.

# 1.Logical not--- reverse the boolean result
# 2.logical and--- returns true if both conditions are true
# 3.logical or---  returns true if at least one condition is true



a = 5
b = 6
c=8
print(a>b and c>b)     #false


d = 10
e = 6
f=8
print(d>e and f>e)         #true


print(b>a or c<b)  #true


print(not a>b)   #true