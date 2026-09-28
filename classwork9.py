#Write a menu-driven Python program using a class Student to perform the following operations:
# 1Add Student(roll no,name,marks)
# 2Update Marks
# 3Display All Student Details
# 4Search Student by Roll Number
# 5Delete Student
# 6Exit
# Store student records in a list and perform all operations using the student's roll number.

class Student:
    def __init__(self):
        self.roll=int(input("Roll number:"))
        self.name=input("Name:")
        self.marks=int(input("Marks:"))
    def upmark(self):
        self.marks=int(input("enter new Marks:"))
    def show(self):
        print("roll no: ",self.roll," ","Name: ",self.name," ","Marks: ",self.marks)

l=[]
while(1):
    print("1.Add Student")
    print("2.Update marks")
    print("3.Show student details")
    print("4.Search")
    print("5.Delete Student")
    print("6.Exit")
    choice=int(input("Enter choice:"))
    print()
    if choice==1:
        s=Student()
        l.append(s)
        print(l)
        print()
    elif choice==2:
        roll = int(input("Enter roll number: "))

        for s in l:
            if s.roll == roll:
                s.upmark()
                print("Marks updated successfully")
                break
        else:
            print("Student not found")
        print()
    elif choice==3:
        if len(l) == 0:
            print("No students found")
        else:
            for s in l:
                s.show()
        print()
    elif choice==4:
        roll = int(input("Enter roll number: "))

        for s in l:
            if s.roll == roll:
                s.show()
                break
        else:
            print("Student not found")
        print()
    elif choice==5:
        roll = int(input("Enter roll number: "))

        for s in l:
            if s.roll == roll:
                l.remove(s)
                print("Student deleted successfully")
                break
        print()
    elif choice==6:
        exit()