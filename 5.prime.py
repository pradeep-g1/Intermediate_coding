def prime(n):
    isprime=True
    for i in range(2,n):
        if n%i==0:
            isprime=False
            break
    if isprime==True:
        return True
    else:
        return False
n=int(input("enter the num: "))
if n == 0 or 1:
    print("{0} is not a prime number".format(n))
if prime(n):
    print("{0} is a prime number".format(n))
else:
    print("{0} is not a prime number".format(n))         
            
            
    
