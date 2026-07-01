years_of_experience = int(input("Years of Experience:"))

if years_of_experience < 0 :
    print("Invalid Input, Experience can not be a negative number");
elif years_of_experience < 5:
    print("Junior Engineer");
elif years_of_experience >= 5 and years_of_experience <= 10:
    print("Senior Engineer");
elif years_of_experience > 10 and years_of_experience <= 20:
    print("Lead Engineer");
else:
    print("Enterprise Architect");



