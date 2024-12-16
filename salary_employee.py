class Employee:
    def __init__(self,name,salary,current_task):
        self.name = name
        self.salary = salary
        self.current_task = current_task

    def annual_salary_cal(self):
        annual_sal = self.salary*12
        print(f"{self.name}'s annaul salary is {annual_sal}")
        return annual_sal

class Developer(Employee):
    def __init__(self,name,salary,current_task,dept):
        super().__init__(name,salary,current_task)
        self.dept = dept
        

    def task(self,abt_task):
        print(f"{self.name} from {self.dept} department is allocated with a new task: {abt_task}")
        print(f"{self.name} is currently working on task :{self.current_task} ")

class project_Manager(Employee):
    def __init__(self,name,salary,current_task,projects):
        super().__init__(name,salary,current_task)
        self.projects=projects

    def assign_to_project(self,project_name):
        print(f"{self.name} is alloacted with a new project")
        print(f"The new project assigned to {self.name}  is:{project_name}")

if __name__ == "__main__":
    a = Developer(name="Radhika",salary=20000,current_task="project alpha",dept="Developer")
    b = project_Manager(name="Dishan", salary=25000,current_task="project beta",projects="app development")

    a.annual_salary_cal()
    a.task("developing an app")

    b.annual_salary_cal()
    b.assign_to_project("Python based Project")
