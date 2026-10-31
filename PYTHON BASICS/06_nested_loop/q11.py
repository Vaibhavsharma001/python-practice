# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

for i in range(6):
    for j in range(i):
        print("*",end="")
    print()
for i in range(5):
    for j in range(5 - i):
        print("*",end ="")
    print()
    

# -------------------------------
print()
# -------------------------------

i =1
while i<=5:
    j=1
    while j<=i:
        print("*", end="")
        j+=1
        
    i+=1
    print()
i =5
while i>=1:
    j=1
    while j<=i:
        print("*",end="")
        j+=1
        
    i-=1
    print()
