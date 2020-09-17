email_address = input("Email address: ")
print("Checking...")

# ...and the rest is up to you
att = 0
spaces = ""
dot = 0
for ch in email_address:
    
    if ch == "@" and email_address[0] == "@":
        print(" ",email_address)
        print("^--this bit is missing")
        break
    elif ch == "@" and email_address[-1] == "@":
        print(email_address)
        print(spaces,"^--this bit is missing")
        break
    elif ch == "@" and att == 0:
        att +=1
        spaces = spaces + " "
    elif ch == "@" and att != 0:
        print(email_address)
        print(spaces,"^--there's an extra @ symbol here")
        break
    elif ord(ch) > 47 and ord(ch) < 123:
        spaces = spaces + " "
        dot = 0
    elif ch == "@" and email_address[-1] == "@":
        print(email_address)
        spaces = spaces + " "
        print("^--this bit is missing")
        break
    elif ch == "." and email_address[0] == ".":
        print(email_address)
        print("^--there's a dot here that probably shouldn't")
        break
    elif ch == "@" and dot == 1:
        print(email_address)
        print(spaces,"^--there's a dot here that probably shouldn't")
    elif ch == "." and dot == 0:
        spaces = spaces + " "
        dot +=1
    elif ch == "." and dot == 1:
        print(email_address)
        print("^--there are consecutive dots here")
        break
    elif ch == email_address[-1] and att == 0:
        print(email_address)
        print("@ symbol is missing")
    
    