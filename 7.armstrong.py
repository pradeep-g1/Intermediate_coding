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
if armstrong(num):
    print("{0} is a armstrong number".format(num))
else:
    print("{0} is not a armstrong number".format(num))
