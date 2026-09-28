#create an abstract class shape with abstract methods get_area and get_perimeter
#create two subclasses
#rectangle and square
#each class should calculate area and perimeter differently

# from abc import ABC,abstractmethod
#
# class Shape(ABC):
#
#     @abstractmethod
#     def get_area(self):
#         pass
#
#     @abstractmethod
#     def get_perimeter(self):
#         pass
#
# class Rectangle(Shape):
#     def __init__(self):
#         self.length=int(input("Enter length"))
#         self.breadth=int(input("Enter breadth"))
#     def get_area(self):
#         print("Area",self.length*self.breadth)
#     def get_perimeter(self):
#         print("Perimeter",2*(self.length*self.breadth))
# r=Rectangle()
# r.get_area()
# r.get_perimeter()
#
#
# class Square(Shape):
#     def __init__(self):
#         self.side=int(input("Enter side"))
#     def get_area(self):
#         print("Area",self.side**2)
#     def get_perimeter(self):
#         print("Perimeter",4*self.side)
# s=Square()
# s.get_area()
# s.get_perimeter()

#Create an abstract class Employee with an abstract method calculate_salary()
#create two subclasses
#FullTimeEmployee
#PartTimeEmployee
#Each class should calculate salary differently


from abc import ABC,abstractmethod

class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass
    def __init__(self):
        self.empid = int(input("Enter Employee id:"))
        self.name = input("Enter Name:")
        self.age = int(input("Enter Age:"))


class FullTimeEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.monthlysalary=int(input("Enter Monthly Salary:"))
    def calculate_salary(self):
        print("Monthly Salary:",self.monthlysalary)

f=FullTimeEmployee()
f.calculate_salary()


class PartTimeEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.hours=int(input("Enter Total Working Hours:"))
        self.rate=int(input("Enter Rate Per Hour:"))
    def calculate_salary(self):
        print("Salary Per Day:",self.hours*self.rate)

p=PartTimeEmployee()
p.calculate_salary()








