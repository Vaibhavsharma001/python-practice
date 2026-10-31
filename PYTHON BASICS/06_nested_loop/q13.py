# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15

num =1 
for i in range(1,6):
    for j in range(1,i+1):
        print(num, end = " ")
        num+=1

    print()

print()

i = 1
num = 1

while i <= 5:
    j = 1

    while j <= i:
        print(num, end=" ")
        num += 1
        j += 1

    print()
    i += 1