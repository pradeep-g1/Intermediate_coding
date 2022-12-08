def prime(n):
    a=True
    for i in range(2,n):
        if n%i==0:
            a=False
    if a==True:
        return True
    else:
        return False
num=int(input("enter the num: "))
primes=[]
for i in range(2,num):
    if prime(i):
        primes.append(i)
res=[]
for i in primes:
    while num%i==0:
        res.append(i)
        print(num)
        num=num/i     
print(res)
    

