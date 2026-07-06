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

