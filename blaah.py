class EmployeeManagement:
    def __init__(self):
        self.employees=[]
    def create(self,id,name,position):
        for emp in self.employees:
           if emp["id"]==id:
                print(f"employee with {id} already exists")
                return 
        self.employees.append({"id":id,"name":name,"position":position})
        print("Employee created successfully")

    def read(self):
        return self.employees

    def update(self,id,name,position):
        flag=False
        for emp in self.employees:
            if(emp["id"]==id):
                emp["name"]=name
                emp["position"]
                print("Employee Updated Successfully")
                flag=True
                return emp
        if(flag!=True):
            print("Employee Not Found")
    
    def remove(self,id):
        for emp in self.employees:
           if emp["id"]==id:
                self.employees.remove(emp)
                print("Employe Removed Successfully")
                return 
empmng=EmployeeManagement()
empmng.create(2,"Mark","Dev")
empmng.create(3,"John","QA")

empmng.update(2,"Smith","Project Manager")
empmng.remove(3)
print(empmng.read())