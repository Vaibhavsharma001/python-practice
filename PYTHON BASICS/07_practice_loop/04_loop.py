# 4. Reverse a String
# Problem: Reverse a string using a loop.

input_str =input("enter text=-")
reversed_string=""   
 
for char in input_str:
    reversed_string=char+reversed_string
print(reversed_string)



