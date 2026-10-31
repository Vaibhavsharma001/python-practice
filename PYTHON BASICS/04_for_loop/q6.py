                                                 # QUES 6

# Count Vowels in a String
# Question: Write a program to count the number of vowels in
# the word "education".
# Input: education
# Expected Output: 5
# Hint: Check if each character in the string is a vowel and keep
# a count.


                                                 # ANSWER

vovels="aeiou"
word="education"
c=0
for i in word:
    if i in vovels:
        c+=1
print(c)