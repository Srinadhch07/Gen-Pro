class Student:
    def __init__(self,name,grade="A"):
        self.name=name
        self.grade=grade 
    def show(self):
        print(f"{self.name} - Grade: {self.grade}")
stu1=Student("Alice")
stu2=Student("Bob","B")

stu1.show()
stu2.show()