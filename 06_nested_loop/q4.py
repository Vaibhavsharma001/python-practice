# 1
# 12
# 123
# 1234
# 12345

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end = "")
    print()
    
# ------------------/
print()
#-------------------/


i = 1
while i<=5:
    j= 1
    while j<=i:
        print(j, end = "")
        j+=1
    i+=1
    print()