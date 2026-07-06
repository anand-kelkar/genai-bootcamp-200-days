from employee import Employee

class Report:

        def __init__(self, child_class):
             if isinstance(child_class, Employee):                  
                  self.employee_details = child_class
                
        def prepare_employee_report(self,bonus_percent,bonus,employee_status):               
                lines_to_write =["==============================\n",
                        "Employee Report\n",
                        "==============================\n",
                        f"Name             : {self.employee_details.name}\n",
                        f"Salary           : ₹{self.employee_details.salary}\n",
                        f"Experience       : {self.employee_details.experience} years\n",
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
