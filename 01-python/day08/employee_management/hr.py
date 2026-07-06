from employee import Employee

class HR(Employee):
    def onboard_new_associate(self):
        print("Collecting documents for new associate onboarding")

    def calculate_bonus(self):            
            bonus_percent = 15
            employee_status = "HR" 
            bonus = (self.salary * bonus_percent) / 100
            return bonus_percent,bonus,employee_status