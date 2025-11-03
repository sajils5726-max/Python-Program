class employee:
    def __init__(self,empid,name,salary):
        self.empid = empid
        self.name = name
        self.salary = salary


    def display_employee_details(self):
        print("----Student Details----")
        print(f"Emp-id :{self.empid}")
        print(f"Name :{self.name}")
        print(f"salary :{self.salary}")
        

employee1=employee(321,"Ambadi",50000)
employee2=employee(453,"Arjun",31000)
employee1.display_employee_details()
employee1.display_employee_details()