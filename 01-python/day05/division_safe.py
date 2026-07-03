# code to demonstrate exceptin handling , catch divide by zero exception
number1 = int(input("Enter First Number : "))
number2 = int(input("Enter Second Number : "))

try:
    result = number1/number2
    print(f"Division of number 1 and number 2 is {result}")
except:
    print("Cannot divide by zero.")