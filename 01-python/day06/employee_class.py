# class employee to store employee data and calculate bonus
class Employee:
    def __init__(self,name,salary,experience):
        self.name = name
        self.salary = salary
        self.experience = experience

    def calculate_bonus(self):    
        if self.experience < 0:
            print("Invalid input, experience can not be a negative number")
        elif self.experience < 5 :
            bonus_percent = 5
            employee_status = "Junior Engineer"        
        elif self.experience <= 10 :
            bonus_percent = 10
            employee_status = "Senior Engineer" 
        elif self.experience < 20 :
            bonus_percent = 20
            employee_status = "Lead Engineer" 
        else:
            bonus_percent = 20
            employee_status = "Senior Enterprise Architect" 

        bonus = (self.salary * bonus_percent) / 100
        return bonus_percent,bonus,employee_status

    def display_employee(self,bonus_percent,bonus,employee_status):
        print("==============================")
        print("Employee Report")
        print("==============================")
        print(f"Name             : {self.name}")
        print(f"Salary           : ₹{self.salary}")
        print(f"Experience       : {self.experience} years")
        print(f"Bonus Percentage : {bonus_percent}%")
        print(f"Bonus Amount     : ₹{bonus}")
        print(f"Status           : {employee_status}")

employee = Employee("Anand",1200000,20)
bonus_percent,bonus,employee_status = employee.calculate_bonus()
employee.display_employee(bonus_percent,bonus,employee_status)
