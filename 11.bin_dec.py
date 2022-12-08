def bin(arr):
    a=arr[::-1]
    sum=0
    for i in range(len(a)):
        sum=sum+(a[i]*(2**i))
    print("deci: ",sum)
arr=[1,1,0,1]
bin(arr)
            
