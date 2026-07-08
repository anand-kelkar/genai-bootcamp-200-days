import json
employee = {
    "name": "Anand",
    "experience": 20,
    "skills": [
        "BizTalk",
        "MuleSoft",
        "Python"
    ]
}

str_employee = json.dumps(employee, indent= 2)
print(str_employee)

dict_employee = json.loads(str_employee)
print(dict_employee)
print(type(dict_employee))