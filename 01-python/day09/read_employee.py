import json

with open("01-python\\day09\\employee.json") as file:
    employee_details = json.load(file)


print(f"Employee Name : {employee_details["name"]}")
print(f"Salary        : {employee_details["salary"]}")
print(f"Department    : {employee_details["department"]}")