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
        print(f"Employee {name} added successfully")
        # to remove
    def remove_employee(self,emp_id):
        for i in self.emp:
            if i["emp_id"] == emp_id:
                self.emp.remove(i)
                print(f"Employee ID {emp_id} removed successfully ")
    
    def display_employees(self):
        for employee in self.emp:
            print(f"ID: {employee['emp_id']}, Name: {employee['name']}, Position: {employee['position']}, Salary: {employee['salary']}")

        #updating details using emp_id
    def update_employee(self,emp_id,name,position,salary):
        for i in self.emp:
            if i["emp_id"]==emp_id:
                if name:
                    i["name"] = name
                if position:
                    i["position"] = position
                if salary:
                    i["salary"] = salary
                print(f"Employee with ID: {emp_id},Name:{name}, Position:{position}, Salary:{salary} updated successfully")
                
                return
            
        print(f"{emp_id} Not found")
nw = Employee_Management_ssm()
nw.add_employee("STI20","Albi","b analyst",30000)
nw.add_employee("STI25","Jeeva","Testing",25000)
nw.add_employee("STI27","Ancy","developer",32000)

#performing tasks
nw.display_employees()
nw.remove_employee("STI20")
nw.update_employee("STI25","Jeeva","Testing",salary=35000)
nw.display_employees()
            


    









    


        