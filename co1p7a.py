#(a)
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
    print(lst2)
if(len(lst)==len(lst2)):
    print("both list are of same length")
else:
    print("both list are of different length")
