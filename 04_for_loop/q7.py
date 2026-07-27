                                             # QUES 7

# Print Fibonacci Sequence up to 10 Terms
# Question: Write a program to print the first 10 terms of the
# Fibonacci sequence.
# Expected Output: 0 1 1 2 3 5 8 13 21 34
# Hint: Each term in the Fibonacci sequence is the sum of the
# two preceding ones.



                                            #   ANS
a = 0
b = 1

for i in range(0,11):
    print(a)  
    c = a + b
    a = b
    b=c
