yr=int(input("enter the year: "))
if yr<2022:
    print("invalied year!!!")
print("leap year are :")
for yr in range(2022,yr,1):
    if (yr % 4==0):
        print(yr)