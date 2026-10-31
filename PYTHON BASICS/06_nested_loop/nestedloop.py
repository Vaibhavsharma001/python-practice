# work on row and columns use nested loops 
# A nested loop is a loop placed inside another loop. The inner loop executes completely for each iteration of the outer loop. Python allows any combination of for and while loops to be nested.

i =1
while i <= 3:
    j = 1
    while j <= 3:
        print(i, j)
        j += 1
    i += 1
    
    
for a in range(1, 3):
    for b in range(1, 4):
        print(a, b)
