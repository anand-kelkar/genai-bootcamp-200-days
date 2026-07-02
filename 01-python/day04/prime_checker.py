# program to identify if given number is prime or not
number =int(input("Enter a number:"))

def prime_check(number):
    is_prime_number = True
    factor_list =[1]
    if(number < 1):
        print(f"Number {number} is not a prime number")
        return
    for sequence in range(2, number):
        if(number % sequence == 0):
            factor_list.append(sequence)
            is_prime_number = False
    factor_list.append(number)
    if(is_prime_number):
        print(f"Number {number} is  a prime number")
    else:
        print(f"Number {number} is not a prime number, it has factors {factor_list}")

prime_check(number)

