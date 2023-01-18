a,b,c=[int(a) for a in input("enter 3 values ").split()]
if(a>b and a>c):
    print("{} is greater".format(a))
elif(b>c):
    print("{} is greater".format(b))
else:
    print("{} is greater ".format(c))