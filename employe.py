class Employee:
    def __init__(self,emp_id,name,position,salary):
        self.name = name
        self.position = position
        self.salary = salary
    def __str__(self):
        print(f"ID:{self.emp_id},Name:{self.name},position:{self.salary}")
    
Employee1 = ("STI21","Albi","b analyst",25000)
Employee2 = ("STI22","Jithin","developer",32000)
Employee3 = ("STI23","Harshan","Trainee",15000)
print(Employee1)
print(Employee2)
print(Employee3)


        