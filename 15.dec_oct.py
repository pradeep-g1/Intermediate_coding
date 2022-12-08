def oct(num):
    zz=[]
    while num>=1:
        zz.append(num)
        num=num//8
    print(zz[::-1])
    x=zz[::-1]
    for i in x:
        if i in [1,2,3,4,5,6,7]:
            print(i,end="")
        else:
            print(i%8,end="")
    print()
num=int(input("enter the num: "))
oct(num)