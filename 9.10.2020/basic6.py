name = input("Input a name: ")
counter = 0
initial = ""
first_name = ""
for ch in name:
    if ch == ",":
        counter +=1
    elif counter == 1 and ch == " ":
        counter +=2
    elif counter == 3:
        initial = str(ch).upper()+"."
        break
    elif counter == 0:
        first_name = first_name+str(ch)
print(initial+" "+first_name.title())