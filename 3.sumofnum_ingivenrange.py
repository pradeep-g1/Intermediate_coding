from re import I


a=int(input("enter the a: "))
b=int(input("enter the b: "))
sum=0
for i in range(a,b+1):
    sum=sum+i
print("sum is {0}".format(sum))

print(((b*(b+1))/2-(a*(a+1))/2)+a)