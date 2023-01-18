#(a)Generate positive list of numbers from a given list of integer
l=[2,4,3,-1,-5,-6]
print("list is: ",l)
y=[i for i in l if i >0]
print(y)