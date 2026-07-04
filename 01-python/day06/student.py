class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks

    def calculate_grade(self):
        if(self.marks > 90):
            grade = "A"
        elif(self.marks > 75):
            grade = "B"
        elif(self.marks > 60):
            grade = "C"
        else:
            grade = "Fail"
        return grade

    def display(self,grade = "NA"):
        print("==============================")
        print("Student Report")
        print("==============================")
        print(f"Name            : {self.name}")
        print(f"Age             : {self.age}")
        print(f"Marks           : ₹{self.marks}")
        print(f"Grade           : {grade}")

student = Student("Anand", 43, 76)
student.display()
grade = student.calculate_grade()
student.display(grade=grade)
