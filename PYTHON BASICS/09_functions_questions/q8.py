# Write a function sum_list(numbers) that returns the sum of all elements in a list without using sum().

def sum_list(numbers):
    total=0
    for i in numbers:
        total+=i

    return total
print(sum_list([10,20,30]))
