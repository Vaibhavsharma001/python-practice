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