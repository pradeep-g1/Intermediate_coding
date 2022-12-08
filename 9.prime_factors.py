def prime_factors(n):
    #even number divisible
    while n%2==0:
        print(2)
        n=n/2
    #n became odd
    for i in range(3,int(n**0.5),2):
        while n%i==0:
            print(i,end=" ")
            n=n/i
    if n>2:
        print(n)
n=int(input("enter the numbers: "))
prime_factors(n)
            