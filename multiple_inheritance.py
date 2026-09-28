class Hospital:
    def __init__(self):
        self.hos_name=input("Enter Hospital Name:")
        self.loc=input("Enter Location:")
        self.phone=input("Enter Phone No:")
    def display_hospital(self):
        print("Hospital Name:",self.hos_name)
        print("Location:",self.loc)
        print("Phone No:",self.phone)
class Department:
    def __init__(self):
        self.dept_name=input("Enter Department:")
        self.doc_name=input("Enter Doctor Name:")
    def display_department(self):
        print("Department Name:",self.dept_name)
        print("Doctor Name:",self.doc_name)
class Patient(Hospital,Department):
    def __init__(self):
        Hospital.__init__(self)
        Department.__init__(self)
        self.patient_name=input("Enter Patient Name:")
        self.age=int(input("Enter Patient Age:"))
        self.gender=input("Enter Patient Gender:")
        self.phone=int(input("Enter Phone Number"))
        self.add_date=input("Enter Addmission Date")
        self.bed_no=int(input("Enter Bed Number:"))
        self.discharge_date=""
    def set_discharge(self):
        self.discharge_date=input("Discharge")
    def full_summary(self):
        Hospital.display_hospital(self)
        Department.display_department(self)
        print("Patient Name:",self.patient_name)
        print("Age:",self.age)
        print("gender:",self.gender)
        print("Phone Number:",self.phone)
        print("Admission Date:",self.add_date)
        print("Bed no",self.bed_no)
        if(self.discharge_date==""):
            print("not yet discharged")
        else:
            print(self.discharge_date)
p=Patient()
p.set_discharge()
p.full_summary()



