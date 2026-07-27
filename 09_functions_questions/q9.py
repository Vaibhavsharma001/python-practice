# Write a function is_prime(n) that returns True if the number is prime, otherwise False.

def is_prime(n):

    if n<2:
        return False
    
    for i in range(2,n):
        if n%i==0:
            return False
        
        else:
            return True
        
print(is_prime(7))        