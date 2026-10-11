# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321

for i in range(1, 6):

    for j in range(1, i + 1):
        print(j, end="")

    for j in range(2 * (5 - i)):
        print(" ", end="")

    for j in range(i, 0, -1):
        print(j, end="")

    print()

print()

i = 1

while i <= 5:
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
    spaces = 1
    while spaces <= 2 * (5 - i):
        print(" ", end="")
        spaces += 1
    j = i
    while j >= 1:
        print(j, end="")
        j -= 1
    print()
    i += 1