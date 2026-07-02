# Employee report generation code that takes inputs like name , salary and experience from user
# and calculate the bonus for the employee
def get_employee_details():
    employee_name = input("Employee Name :")
    employee_salary = int(input("Salary :"))
    years_of_experience = int(input("Years of Experience :"))
    return employee_name,employee_salary,years_of_experience

def calculate_bonus():
    global bonus
    global bonus_percent
    global employee_status
    if years_of_experience < 0:
        print("Invalid input, experience can not be a negative number")
    elif years_of_experience < 5 :
        bonus_percent = 5
        employee_status = "Junior Engineer"        
    elif years_of_experience <= 10 :
        bonus_percent = 10
        employee_status = "Senior Engineer" 
    elif years_of_experience < 20 :
        bonus_percent = 20
        employee_status = "Lead Engineer" 
    else:
        bonus_percent = 20
        employee_status = "Senior Enterprise Architect" 

    bonus = (employee_salary * bonus_percent) / 100

def display_report():
    print("==============================")
    print("Employee Report")
    print("==============================")
    print(f"Name             : {employee_name}")
    print(f"Salary           : ₹{employee_salary}")
    print(f"Experience       : {years_of_experience} years")
    print(f"Bonus Percentage : {bonus_percent}%")
    print(f"Bonus Amount     : ₹{bonus}")
    print(f"Status           : {employee_status}")



employee_details = get_employee_details()
employee_name = employee_details[0]
employee_salary = employee_details[1]
years_of_experience = employee_details[2]
bonus = 0
bonus_percent = 0
employee_status = ""
calculate_bonus()
display_report()

