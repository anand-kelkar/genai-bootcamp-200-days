user_name = input("Enter your full name:")

print(f"Original Name : {user_name}")
print(f"Name in Upper Case : {user_name.upper()}")
print(f"Name in Lower Case : {user_name.lower()}")
print(f"Total no of character in name : {len(user_name)}")
print(f"First character of the name : {user_name[0]}")
print(f"Last character of the name : {user_name[-1]}")

# below code counts number of vowels in given string (name)
vowel_count = 0
for char in (user_name.lower()):
    if(char in "aeiou"):
        vowel_count = vowel_count + 1

print(f"No of vowel in name : {vowel_count}")