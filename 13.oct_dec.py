def oct(arr):
    x=arr[::-1]
    sum=0
    for i in range(len(x)):
        sum=sum+x[i]*(8**i)
    print("decimal is: ",sum)
arr=[8,9]
oct(arr)