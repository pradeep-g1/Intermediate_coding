def compute_hcf(x,y,z):

# choose the smaller number
    a=[x,y,z]
    smaller=min(a)
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0) and (z%i==0)):
            hcf = i 
    return hcf

num1 = 28
num2 = 32
num3=99

print("The H.C.F. is", compute_hcf(num1, num2,num3))