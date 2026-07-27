# 3. Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

inp=int(input("enter your number=-"))
for i in range(1,11):
    if i==5:
        continue
    print(inp,"X",i,"=",inp*i )