#static
# class Person:
#     def __init__(self,n,a):
#         self.name=n
#         self.age=a
#     def show(self):
#         print(self.name,self.age)
# p1=Person("arun",23)
# p1.show()
# p2=Person("amal",23)
# p2.show()

#dynamic
# class Person:
#     def __init__(self):
#         self.name=input("enter name:")
#         self.age=int(input("enter age"))
#     def show(self):
#         print(self.name,self.age)
# p1=Person()
# p1.show()
# p2=Person()
# p2.show()

# #define a class named employee with attributes empid,name,salary,designation and methods getsalary() and showpersonaldetails()
# class Employee:
#     def __init__(self):
#         self.id=int(input("Enter Employee ID:"))
#         self.name=input("Enter Name:")
#         self.age=int(input("Enter Age:"))
#         self.salary=int(input("Enter Salary:"))
#         self.designation=input("Enter Designation:")
#     def getsalary(self):
#         print(self.salary)
#     def showpersonaldetails(self):
#         print(self.name,self.age)
# p1=Employee()
# p1.getsalary()
# p1.showpersonaldetails()

#define a class named student with attributes rollno,name,mark1,mark2,mark3, and method display() to display roll number and total mark of a student create a student object and call the methods
# class Student:
#     def __init__(self):
#         self.no=int(input("Enter Roll no:"))
#         self.name=input("Enter Name:")
#         self.mark1=int(input("Enter Mark1:"))
#         self.mark2=int(input("Enter Mark2:"))
#         self.mark3=int(input("Enter Mark3:"))
#     def display(self):
#         total = self.mark1 + self.mark2 + self.mark3
#         print("Roll Number:",self.no,"Total MArk:",total)
# p1=Student()
# p1.display()

#create a class named book with attributes title,author,price,pages,language and methods
#gettitle(),getauthor(),getprice(),settitle(),setauthor(),setprice()
#create a book object and call the methods
#b=Book()
#b.gettitle()#title
#b.settitle()#updates the title of book object

# class Book:
#     def __init__(self):
#         self.title = input("Enter Title:")
#         self.author = input("Enter Author:")
#         self.price = int(input("Enter Price:"))
#         self.pages = int(input("Enter Pages:"))
#         self.language = input("Enter Language:")
#
#     def gettitle(self):
#         print("Title:", self.title)
#
#     def getauthor(self):
#         print("Author:", self.author)
#
#     def getprice(self):
#         print("Price:", self.price)
#
#     def settitle(self):
#         self.title = input("Enter New Title:")
#         self.gettitle()
#
#     def setauthor(self):
#         self.author = input("Enter New Author:")
#         self.getauthor()
#
#     def setprice(self):
#         self.price = int(input("Enter New Price:"))
#         self.getprice()
#
# b = Book()
#
# b.gettitle()
# b.getauthor()
# b.getprice()
#
# b.settitle()
# b.setauthor()
# b.setprice()

# create a class named account with attributes ac name,ac no,balance and methods withdraw(),deposit(),showbalance() create an account object and call the methods
class Account:
    def __init__(self):
        self.acname = input("Enter AC Name:")
        self.acno = int(input("Enter AC No:"))
        self.balance= int(input("Enter Balance"))

    def withdraw(self):
        x=int(input("Enter the amount to withdraw:"))
        if x>self.balance:
            print("Insufficient Balance")
        else:
            self.balance = self.balance - x
            self.showbalance()

    def deposit(self):
        y=int(input("Enter the amount to deposit:"))
        self.balance = self.balance + y
        self.showbalance()

    def showbalance(self):
        print("Balance:",self.balance)
#
# a=Account()
# a.withdraw()
# a.deposit()
# a.showbalance()

a1=Account()
a2=Account()
l=[a1,a2]
for i in l:
    print(i.acname)
    i.showbalance()


