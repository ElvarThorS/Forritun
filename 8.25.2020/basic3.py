num1 = int(input("First number: ")) # Do not change this line
num2 = int(input("Second number: ")) # Do not change this line
num3 = int(input("Third number: ")) # Do not change this line

# Fill in the missing code below
if num1 < num2 and num1 < num3:
    min_int = num1
elif num2 < num1 and num2 < num3:
    min_int = num2
elif num3 < num1 and num3 < num2:
    min_int = num3
else: 
    min_int = num1
print("The minimum is: ", min_int) # Do not change this line