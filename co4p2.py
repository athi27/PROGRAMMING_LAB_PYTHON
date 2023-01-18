''' CO4. 2. Create a Bank account with members account number, name, type of account and balance.
Write constructor and methods to deposit at the bank and withdraw an amount from the bank. '''

class Bank_Account:
    def __init__(self):
        self.acc_no=int(input("Enter the account no.:"))
        self.name=input("Enter the account holder's name : ")
        self.acc_typ=input("Enter the account type (S/C):")
        self.bal=0
    def deposit(self,amt):
        self.bal=self.bal+amt
        return(self.bal)
    def withdraw(self,amt):
        if self.bal < amt:
            print("Insufficient balance!!")
        else:
            self.bal=self.bal-amt
        return(self.bal)
    def disp(self):
        print("Account Number : ",self.acc_no)
        print("Name : ",self.name)
        print("Account type : ",self.acc_typ)
        print("Current balance : ",self.bal)

new_acc=Bank_Account()
try:
    while True:
        print("Bank operations...\n\t1.Deposit \n\t2.Withdraw\n\t3.Display Account Details\n\t4.Exit.")
        ch=int(input("Enter your choices(1-4):"))
        if ch==1:
            amt=int(input("Enter the amount to be deposited : "))
            print("Current balance : ",new_acc.deposit(amt))
        elif ch==2:
            amt=int(input("Enter the amount to be withdrawn: "))
            print("Current balance : ",new_acc.withdraw(amt))
        elif ch==3:
            print("Account details...")
            new_acc.disp()
        elif ch==4:
            print("Exit!!")
            sys.exit(0)
        else:
            print("Invalid choice!!")
except:
    print("Invalid data provided!!")
finally:
    print("\n ..........Thank  you for availing the banking facility...........")