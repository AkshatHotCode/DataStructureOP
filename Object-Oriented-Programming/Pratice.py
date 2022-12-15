#Illustration 1
class Customer:
    def __init__(self, name, iden, acno):
        self.custName = name
        self.custID = iden
        self.custAccNo = acno
    def display(self):
        print('Customer Name: ', self.custName)
        print('Customer ID: ', self.custID)
        print('Customer Account Number: ', self.custAccNo)

#Driver Code
# name = input('Enter Customer Name: ')
# iden = input('Enter Customer Identification Number: ')
# acno = input('Enter Customer Account Number: ')
# customer = Customer(name, iden, acno)
# customer.display()


#Illustration 2
class Customer:
    def __init__(self, name, iden, acno):
        self.custName = name
        self.custID = iden
        self.custAccNo = acno
    def display(self):
        print('Customer Name: ', self.custName)
        print('Customer ID: ', self.custID)
        print('Customer Account Number: ', self.custAccNo)

class Account(Customer):
    def __init__(self, custName, custID, accNum, typeAcc, balAcc):
        super().__init__(custName, custID, accNum)
        self.typeAcc = typeAcc
        self.balAcc = balAcc
    def deposit(self):
        amount = int(input('Enter the amount to deposit: '))
        self.balAcc = amount + self.balAcc
    def withdraw(self):
        while 1:
            amount = int(input('Enter thee amount to withdraw: '))
            if self.balAcc - amount > 10000:
                self.balAcc = self.balAcc - amount
                break
            else:
                print("Insufficient Balance! Request declined")
    def printBalance(self):
        super().display()
        print('Account Balance is: ', self.balAcc)

#Driver Code
custName = input('Enter the name of the customer: ')
custID = input('Enter the identification number: ')
accNum = input('Enter the account number: ')
typeAcc = input('Enter the type of the account: ')
balAcc = int(input('Enter your account balance: '))
acc = Account(custName, custID, accNum, typeAcc, balAcc)
while 1:
    print('Enter 1 for Deposits.')
    print('Enter 2 for Withdrawal.')
    print('Enter 3 for Display Balance.')
    ch = int(input("Enter your choice: "))
    if ch == 1:
        acc.deposit()
    elif ch == 2:
        acc.withdraw()
    elif ch == 3:
        acc.printBalance()
    else:
        break