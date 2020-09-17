# is_prime function definition goes here
def is_prime(number):
    for x in range(2, number):
        if number % x == 0:
            return False
        else:
            pass
    if number % number == 0 and number % 1 == 0:
        return True
    
    
max_num = int(input("Input an integer greater than 1: "))
for x in range (2, max_num+1):
    if is_prime(x) == True:
        print("{} is a prime".format(x))
    else:
        print("{} is not a prime".format(x))
# Call the function here repeatadly from 2 to max_num and print out the appropriate message