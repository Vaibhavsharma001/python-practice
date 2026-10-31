# A
# AB
# ABC
# ABCD
# ABCDE


for i in range(1, 6):
    for j in range(i):
        print(chr(65 + j), end="")
    print()

print()


i = 1

while i <= 5:
    j = 0

    while j < i:
        print(chr(65 + j), end="")
        j += 1

    print()
    i += 1
