from employee import Employee


class Developer(Employee):
    def write_code(self):
        print("Writing code")

    def calculate_bonus(self):            
        bonus_percent = 20
        employee_status = "Developer" 
        bonus = (self.salary * bonus_percent) / 100
        return bonus_percent,bonus,employee_status
