class time:
    def __init__(self):
        self.__hour=int(input("enter the hour"))
        self.__minute=int(input("enter the minute"))
        self.__second=int(input("enter the second"))
    def __add__(self,ob2):
        hour=self.__hour+ob2.__hour
        print("sum of hours",hour)
        minute=self.__minute+ob2.__minute
        print("sum of minutes",minute)
        second=self.__second+ob2.__second
        print("sum of secount",second)
        if hour>=24:
            hour=hour%24
        if minute>=60:
            hour=hour+minute//60
            minute=minute%60
        if second>=60:
            minute=minute+second//60
            second=second%60
        return hour,minute,second
print("enter the time for 1st object")
obj1=time()
print("enter the time for 2nd object")
obj2=time()
sum=obj1+obj2
print("sum is",sum)

        