# program to Calculate bonus based on emplyee experience

employee_name = input("Employee Name :")
employee_salary = int(input("Salary :"))
years_of_experience = int(input("Years of Experience :"))
bonus = 0

def calculate_bonus():
    global bonus
    if years_of_experience < 0:
        print("Invalid input, experience can not be a negative number")
    elif years_of_experience < 5 :
        bonus = (employee_salary * 5) / 100
    elif years_of_experience <= 10 :
        bonus = (employee_salary * 10) / 100
    else:
        bonus = (employee_salary * 20) / 100

calculate_bonus()

print(f"Bonus = ₹ {bonus}")

    
