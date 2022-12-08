def dec_bin(num):
    zz=[]
    while num>=1:
        zz.append(num)
        num=num//2
    print(zz)
    for i in range(len(zz)-1,-1,-1):
        print(zz[i]%2,end=" ")
    print()
num=int(input("enter the num: "))
dec_bin(num)
