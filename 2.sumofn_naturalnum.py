# n=int(input("enter the num: "))
# sum=0
# for i in range(n+1):
#     sum=sum+i
# print("sum is {0}".format(sum))

n=int(input("enter the num: "))
sum=0
while n>=0:
    sum=sum+n
    n=n-1
print("sum is {0}".format(sum))

n=10
print((n*(n+1))/2)