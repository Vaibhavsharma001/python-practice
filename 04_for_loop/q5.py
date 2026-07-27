                                         # oues 5

# Reverse a Word
# Question: Write a program to print the word "Python" in
# reverse using a for loop.
# Expected Output: nohtyP
# Hint: Use reverse indexing or loop through the word in reverse
# order.

                                     # ANSWER

a= "PYTHON"
for i in range(len(a)-1,-1,-1):
    print(a[i],end=" ")