#(b)
lst = []
n = int(input('Enter number of elements : '))
print('elements are:')
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
    print(lst)
lst2= []
n = int(input('Enter number of elements :'))
print('elements are:')
for i in range(0, n):
    el = int(input())
    lst2.append(el)
    print(lst2)
sum=0
for i in range(len(lst)):
    sum=sum+lst[i]
sum1=0
for j in range(len(lst2)):
    sum1=sum1+lst2[j]
if(sum==sum1):
    print('both list have same sum')
else:
    print('both list are of different sum')