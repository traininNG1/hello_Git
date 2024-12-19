class Student:
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark
        
        
    def avgMark_cal(self):
        return sum(self.mark.values())/len(self.mark) 
        
stud=[   
    Student("Meenu",{"Science":82, "Maths":90, "Social Science":78}),
    Student("Alfi",{"Science":65, "Maths":78, "Social Science":74}),
    Student("Romeo",{"Science":88, "Maths":65, "Social Science":90}),
]     
sorted = sorted(stud, key = lambda student : student.avgMark_cal(),reverse=True)

for s in sorted:
    print(f"NAME:{s.name}, Average Mark:{s.avgMark_cal()}")
