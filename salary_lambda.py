from functools import reduce

class Employee:
    def __init__ (self,name,gender,salary):
        self.name = name
        self.gender = gender
        self.salary = salary

    def display(self):
        print(f"Name:{self.name} \n Gender:{self.gender} \n Salary:{self.salary}")

employee_list=[
    Employee("Sruthi","F",60000),
    Employee("varun","M",65000),
    Employee("Divya","F",45000),
    Employee("karthi","M",42000),
    Employee("Rekha","F",61000),
    Employee("Neeraj","M",25000),
]


        #Salary >50k
more_salary = list(filter(lambda emp : emp.salary >= 50000,employee_list))
print("Employers with salary greater than 50,000 are:")
for emp in more_salary:
        emp.display()

        #10% salary increment
increment = list(map(lambda emp : Employee(emp.name, emp.gender, emp.salary*1.1),employee_list))
print("Employer's salary after 10% increment is :")
for emp in increment:
        emp.display()

        #female salary total
female_employees = filter(lambda emp : emp.gender == "F",employee_list)
female_salary = map(lambda emp : emp.salary, female_employees)
total_sal = reduce(lambda total,emp : total + emp, female_salary)
print("Total salary of female employers are :",total_sal)

