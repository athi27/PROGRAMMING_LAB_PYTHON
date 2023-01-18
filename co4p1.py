class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def peri(self):
        return 2*(self.length+self.breadth)
    def area(self):
        return self.length*self.breadth
    def compare(self,obj2):
        try:
            if (obj1.area()==obj2.area()):
                print("both areas are equal")
            elif(obj1.area()>obj2.area()):
                print("area of 1st rectangle is greater than area of 2nd rectangle")
            elif(obj1.area()<obj2.area()):
                print("area of 1st rectangle is lesser than area of 2nd rectangle")
        except:
            print("an error is occured")
a=int(input("enter the length for 1st rectangle "))
b=int(input("enter the breadth for 1st rectangle "))
a1=int(input("enter the length for 2nd rectangle "))
b1=int(input("enter the breadth for 2nd rectangle "))
obj1=rectangle(a,b)
obj2=rectangle(a1,b1)
print("area of 1st rectangle ",obj1.area())
print("area of 2nd rectangle ",obj2.area())
obj1.compare(obj2)