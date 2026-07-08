import requests
import json

class Employee:
    def __init__(self,id, name, email, company):
        self.id = id
        self.name = name
        self.email = email
        self.company = company

def printEmployeeReport(employee : Employee):
    print (f"""Employee Id : {employee.id} 
Employee Name : {employee.name}
Employee Email : {employee.email}
Employee Company : {employee.company}
""")
    
api_response = requests.get('https://jsonplaceholder.typicode.com/users')

users = json.loads(api_response.text)
employees = list()
for user in users:
    employees.append(Employee(user["id"],user["name"],user["email"],user["company"]["name"]))

for employee in employees:
    printEmployeeReport(employee)