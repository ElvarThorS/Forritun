MIN_LENGTH = 6
MAX_LENGTH = 20

password_amount = 0
valid_passwords = 0
invalid_passwords = 0

lowercase = False
uppercase = False
number = False

password = input("Enter a new password: ")
while password != "q":
    if len(password) <= MAX_LENGTH and len(password) >= MIN_LENGTH:
        for ch in password:
            #Checks if ch is a lowercase letter in the ascii table
            if ord(ch) >= 97 and ord(ch) <= 122:
                lowercase = True
            #Checks if ch is a uppercase letter in the ascii table
            elif ord(ch) >= 65 and ord(ch) <= 90:
                uppercase = True
            #Checks if ch is a number in the ascii table    
            elif ord(ch) >= 48 and ord(ch) <= 57:
                number = True
        if lowercase == True and uppercase == True and number == True:
            valid_passwords +=1
            print("Valid password of length {}".format(len(password)))
        elif number == False and uppercase == False:
            invalid_passwords +=1
            print("At least one upper case letter needed")
            print("At least one number needed")
        elif number == False and lowercase == False:
            invalid_passwords +=1
            print("At least one lower case letter needed")
            print("At least one number needed")
        elif lowercase == False and uppercase == False:
            invalid_passwords +=1
            print("At least one lower case letter needed")
            print("At least one upper case letter needed")
        elif lowercase == False:
            invalid_passwords +=1
            print("At least one lower case letter needed")
        elif uppercase == False:
            invalid_passwords +=1
            print("At least one upper case letter needed")
        elif number == False:
            invalid_passwords +=1
            print("At least one number needed")
    else:
        invalid_passwords +=1
        print("Invalid length")
    lowercase = False
    uppercase = False
    number = False
    password = input("Enter a new password: ")
password_amount = valid_passwords + invalid_passwords
print("You tried {} passwords, {} valid, {} invalid".format(password_amount,valid_passwords,invalid_passwords))