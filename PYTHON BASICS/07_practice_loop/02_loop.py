# 2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

n=int(input("enter your number=-"))
count=0
for i in range(n+1):
    if i%2==0:
        count=count+i   
print(count)


#calculate the total no. of even no.

n=int(input("enter your number=-"))
total_even=0
for i in range(1,n+1):
    if i%2==0:
        total_even+=1   
print(total_even)
        
        
