num=int(input("enter the num: "))
sum=0
while num!=0:
    sum=sum+num%10
    num=num//10
print("sum is {0}".format(sum))

num=int(input("enter the "))
s=str(num)
y=s[::-1]
print(y)
s=[int(x) for x in s]
print(s)
#this is for positive numbers

#this is for neg numbers
def rev(n):
    n=str(abs(n))+"-"
    return int(str(n)[::-1])
neg=int(input("enter the neg num: "))
print(rev(neg))



