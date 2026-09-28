class Company:
    def __init__(self):
        self.name=input("Enter Company Name: ")
        self.loc=input("Enter Company Location: ")
    def display_company(self):
        print("Company Name:",self.name)
        print("Company Location:",self.loc)
class Employee(Company):
    def __init__(self):
        super().__init__()
        self.empid=int(input("Enter Employee ID: "))
        self.empname=input("Enter Employee Name: ")
        self.salary=int(input("Enter Employee Salary: "))
    def display_details(self):
        super().display_company()
        print("Employee ID:",self.empid)
        print("Employee Name:",self.empname)
        print("Salary:",self.salary)
    def update_salary(self):
        self.salary=int(input("Enter Employee Salary: "))
e=Employee()
e.display_details()
e.update_salary()
e.display_details()