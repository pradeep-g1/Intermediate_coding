def hex(num):
    x=list(str(num))
    d={'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
    res=[]
    for i in x:
        if i in d:
            res.append(d[i])
        else:
            res.append(i)
    print(res)
    r=res[::-1]
    sum=0
    for i in range(len(r)):
        sum=sum+int(r[i])*(16**i)
    print("deci is: {0}".format(sum))
num=input("enter the: ")
hex(num)

