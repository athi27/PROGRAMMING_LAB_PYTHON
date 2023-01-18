class rectangle:
    def __init__(self):
        self.__length=int(input("enter the length of rectangle"))
        self.__breadth=int(input("enter the breadth of rectangle"))
    def __lt__(self,ob2):
        area1=self.__length*self.__breadth
        area2=ob2.__length*ob2.__breadth
        print("area of rectangle1 is ",area1)
        print("area of rctangle2 is ",area2)
        return area1<area2
print("enter the length and breadth of first object")
og1=rectangle()
print("enter the length and breadth of secont object")
og2=rectangle()
if og1<og2:
    print("rectangle 1 is less than rectangle2")
else:
    print("rectangle 1 is grater than rectangle2")