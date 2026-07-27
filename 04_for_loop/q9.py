                                                              #QUES 9

# Check if a Number is Prime
# Question: Write a program to check if a given number, such as
# 7, is a prime number.
# Input: 7
# Expected Output: 7 is a prime number
# Hint: Prime numbers have no divisors other than 1 and
# themselves.
 
                                                                    #ANS


a =int(input("enter your number"))
count=0
for i in range(1,a+1):
    if a%i==0:
        count=count+1
if count==2:
    print("prime number") 

else:
    print("not an prime number")    
   
