class Employee:
    def __init__(self,emp_id,name,position,salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        print(f"ID:{self.emp_id},Name:{self.name},position:{self.salary}")

class Employee_Management_ssm:
    def __init__(self):
        self.emp = []

    def add_employee(self,emp_id,name,position,salary):
        
    
        self.emp.append({"emp_id":emp_id,"name":name,"position":position,"salary":salary})
        print(f"Employee{name} added successfully")
        # to remove
    def remove_employee(self,emp_id):
        for employee in self.emp:
            if employee.emp_id == emp_id:
                self.emp.remove(employee)
                print(f"Employee ID {emp_id} removed successfully ")

    def display_employees(self):
        for employee in self.emp:
            print("The list of employees are:",employee)

        #updating details using emp_id
    def update_employee(self,emp_id,name,position,salary):
        for employee in self.emp:
            if employee["emp_id"]==emp_id:
                print(f"Employee with ID: {emp_id},Name:{name}, Position:{position}, Salary:{salary} updated successfully")
                #correction required
                
                return
            
        print(f"{emp_id} Not found")

a = Employee_Management_ssm().add_employee("STI20","Albi","b analyst",30000)
b = Employee_Management_ssm().add_employee("STI25","Jeeva","Testing",25000)
c = Employee_Management_ssm().add_employee("STI26","Ancy","developer",32000)

#performing tasks
d=Employee_Management_ssm().display_employees()
e=Employee_Management_ssm().remove_employee("STI26")
f=Employee_Management_ssm().update_employee("STI20","Albi","b analyst",35000)
g=Employee_Management_ssm().display_employees()
            


    









    


        