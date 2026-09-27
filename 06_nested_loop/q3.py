# Write a program in Python to display n terms of natural number and their sum.

n = int(input("enter number:-"))

i = 1
sum = 0
while  i<=n:
    sum = sum +i
    i+=1
    
print(f"sum is {sum}")