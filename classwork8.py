#1.Create a class named Circle with an attribute radius. Use a constructor to initialize the radius by accepting input from the user. Define the following methods:
# getarea() – to calculate and display the area of the circle.
# getperimeter() – to calculate and display the perimeter (circumference) of the circle.
# Create an object of the Circle class and call both methods to display the results.

# class Circle:
#     def __init__(self):
#         self.radius=int(input("Enter radius:"))
#     def getarea(self):
#         self.area=3.14*self.radius**2
#         print("Area:",self.area)
#     def getperimeter(self):
#         self.perimeter=2*3.14*self.radius
#         print("Perimeter:",self.perimeter)
# a=Circle()
# a.getarea()
# a.getperimeter()


# 2.Create a class named Account with attributes acctnumber, acctname, and balance. Initialize these values using a constructor by taking input from the user. Define the following methods:
#
# withdraw() – to withdraw an amount from the account and update the balance.
# deposit() – to deposit an amount into the account and update the balance.
# showbalance() – to display the current balance of the account.
#
# Create an object of the class and call the methods to perform withdrawal and deposit operations and display the updated balance.
# class Account:
#     def __init__(self):
#         self.acname = input("Enter AC Name:")
#         self.acno = int(input("Enter AC No:"))
#         self.balance= int(input("Enter Balance"))
#
#     def withdraw(self):
#         x=int(input("Enter the amount to withdraw:"))
#         if x>self.balance:
#             print("Insufficient Balance")
#         else:
#             self.balance = self.balance - x
#             self.showbalance()
#
#     def deposit(self):
#         y=int(input("Enter the amount to deposit:"))
#         self.balance = self.balance + y
#         self.showbalance()
#
#     def showbalance(self):
#         print("Balance:",self.balance)
#
# a=Account()
# a.withdraw()
# a.deposit()
# a.showbalance()