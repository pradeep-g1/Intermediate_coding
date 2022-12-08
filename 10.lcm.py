def compute_lcm(n1,n2):
    higher=max([n1,n2])
    value=higher
    while True:
        if higher%n1==0 and higher%n2==0:
            print("lcm of two numbers is {0}".format(higher))
            break
        else:
            higher+=value
n1=int(input("enter the number: "))
n2=int(input("enter the num2: "))
compute_lcm(n1,n2)

