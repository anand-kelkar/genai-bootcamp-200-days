# This program asks user to enter password and validate it's strength
# if password is weak , it asks to enter again

def validate_password_strength(password):
    global try_another_password
    word_greater_than_8 = len(password) > 8
    has_upper_char = sum(1 for char in password if char.isupper()) > 0
    has_lower_char = sum(1 for char in password if char.islower()) > 0
    has_digit = sum(1 for char in password if char.isdigit()) > 0
    if((word_greater_than_8 and has_upper_char and has_lower_char and has_digit)):
        print("Strong Password")
        try_another_password = False
    else:
        print("Weak Password, enter again or enter 1 to exit")

try_another_password = True
while try_another_password:
    password = input ("Enter Password to validate :")
    if(password == "1"):
        break
    validate_password_strength(password)