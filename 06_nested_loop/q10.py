#     * 
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *

for i in range(1,6):
    # spaces
    for j in range(5-i):
        print(" ", end = "")
        
    #stars
    for j in range(2*i-1):
        print("*", end = "")
    print()
for i in range(1, 6):
    for j in range(i - 1):
        print(" ", end="")

    for j in range(11 - 2 * i):
        print("*", end="")
    print()


# --------------------------------
print()
# ---------------------------------


i = 1

while i <= 5:
    j = 1
    while j <= 5 - i:
        print(" ", end="")
        j += 1
    j = 1
    while j <= 2 * i - 1:
        print("*", end="")
        j += 1

    print()
    i += 1

i = 1

while i <= 5:
    j = 1
    while j <= i - 1:
        print(" ", end="")
        j += 1
    j = 1
    while j <= 11 - 2 * i:
        print("*", end="")
        j += 1
    print()
    i += 1


