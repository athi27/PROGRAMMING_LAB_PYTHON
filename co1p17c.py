#(c)
lst = []
n = int(input("Enter number of elements : "))
print("elements are:")
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
    print(lst)
lst2= []
n = int(input("Enter number of elements : "))
print("elements are:")
for i in range(0, n):
    el = int(input())
    lst2.append(el)
count=0
for x in lst:
    if (x in lst2 ):
        count=count+1
if(count==1):
    print("both list have same element")
else:
    print("both list have same elements")