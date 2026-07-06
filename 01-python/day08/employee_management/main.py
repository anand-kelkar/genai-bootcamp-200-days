from developer import Developer
from report import Report

developer = Developer("Anand",1200000,20)

bonus_percent,bonus,employee_status = developer.calculate_bonus()
print(f"Employee Status : {employee_status} , Bonus Percent {bonus_percent} , Bonus : {bonus}")

report = Report(developer)
report.display_report(bonus_percent,bonus,employee_status)