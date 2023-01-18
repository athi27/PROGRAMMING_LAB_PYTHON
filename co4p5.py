class Publisher:
    def __init__(self):
        self.__name=input("Enter the Publisher name:")   
    def disp(self):
        print("Publisher name : ",self.__name)

class Book(Publisher):
    def __init__(self):
        super().__init__()
        self.__title=input("Enter the title of the book:")
        self.__author=input("Enter the author's name: ")
    def disp(self):
        super().disp()
        print("Title of the book : ",self.__title)
        print("Author's name : ",self.__author)
class Python(Book):
    def __init__(self):
        super().__init__()
        self.__price=float(input("Enter the price:"))
        self.__pages=int(input("Enter the no.of pages: "))
    def disp(self):
        super().disp()
        print("Title of the book : ",self.__price)
        print("Author's name : ",self.__pages)

bk=Python()
print("...Book Details...")
bk.disp()