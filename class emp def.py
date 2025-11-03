class employee:
    def __init__(self,empid,name,salary):
        self.empid = empid
        self.name = name
        self.salary = salary


    def display_employee_details(self):
        print("----Student Details----")
        print("Empid :",self.empid)
        print("Name :",self.name)
        print("salary :",self.salary)
        

emp1=employee(321,"Ambadi",50000)
emp2=employee(453,"Arjun",31000)

emp1.display_employee_details()
emp2.display_employee_details()