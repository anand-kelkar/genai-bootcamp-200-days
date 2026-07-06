from employee import Employee

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
