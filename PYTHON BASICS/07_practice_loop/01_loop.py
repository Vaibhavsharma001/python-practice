# 1. Counting Positive Numbers
# Problem: Given a list of numbers, count how many are positive.

# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
count_positive_number=0
for num in numbers:
    if num>0:
        count_positive_number+=1
print(count_positive_number)        