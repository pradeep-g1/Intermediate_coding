def armstrong(num):
    c=str(num)
    n=len(c)
    temp=num
    sum=0
    for i in c:
        sum=sum+(int(i)**n)
    if temp==sum:
        return True
    else:
        return False
num=int(input("enter the num: "))
for i in range(num):
    if armstrong(i):
        print(i,end=" ")
print()