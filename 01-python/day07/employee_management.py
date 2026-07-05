# Employee report generation code that takes inputs like name , salary and experience from user
# and calculate the bonus for the employee

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

    def prepare_employee_report(self,bonus_percent,bonus,employee_status):
        lines_to_write =["==============================\n",
                        "Employee Report\n",
                        "==============================\n",
                        f"Name             : {self.name}\n",
                        f"Salary           : ₹{self.salary}\n",
                        f"Experience       : {self.experience} years\n",
                        f"Bonus Percentage : {bonus_percent}%\n",
                        f"Bonus Amount     : ₹{bonus}\n",
                        f"Status           : {employee_status}\n"
                        ]
        return lines_to_write

    def save_report(self,bonus_percent,bonus,employee_status):
        report_data = self.prepare_employee_report(bonus_percent,bonus,employee_status)
        with open("01-python\\day06\\employee_report.txt","w",encoding="utf-8") as file:
            file.writelines(report_data)

    def display_report(self,bonus_percent,bonus,employee_status):
            report_data = self.prepare_employee_report(bonus_percent,bonus,employee_status)
            for line in report_data:
                print(line)


class Manager(Employee):
    def __init__(self, name, salary, experience,team_size,department):
        super().__init__(name, salary, experience)
        self.team_size= team_size
        self.department= department

    def approve_leave(self):
        print("Leave approved")

    def calculate_bonus(self):            
            bonus_percent = 30
            employee_status = "Manager" 
            bonus = (self.salary * bonus_percent) / 100
            return bonus_percent,bonus,employee_status

class Developer(Employee):
    def write_code(self):
        print("Writing code")

    def calculate_bonus(self):            
        bonus_percent = 20
        employee_status = "Developer" 
        bonus = (self.salary * bonus_percent) / 100
        return bonus_percent,bonus,employee_status

class HR(Employee):
    def onboard_new_associate(self):
        print("Collecting documents for new associate onboarding")

    def calculate_bonus(self):            
            bonus_percent = 15
            employee_status = "HR" 
            bonus = (self.salary * bonus_percent) / 100
            return bonus_percent,bonus,employee_status