#This program generates table for a given mumber
number = input("Enter a number:")

# Table Generation logic using for loop
for multiplier in range(1,11):
    print(f"{number} x {multiplier} = {int(number) * int(multiplier)}")   
    
