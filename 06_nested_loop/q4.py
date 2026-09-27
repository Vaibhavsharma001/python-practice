# Write a program in Python to read 10 numbers from keyboard and find their sum and average.


total = 0
i =1

while i<=10:
    num = int(input("enter your 10 number:--"))
    total = total+num
    i=i+1
    
average = total/10
print(total)
print(average)
    


    