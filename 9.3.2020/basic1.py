#Algorithm:
#1 make a loop and put input into a variable 
#2 loop around and compare the inputs and delete the lower input
#3 repeat until negative number is input
#4 print highest number and end program
num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
max_int = 0
while num_int >= 0:
    temp = num_int
    if temp > max_int:
        max_int = temp
        num_int = int(input("Input a number: "))
    else:
        num_int = int(input("Input a number: "))
    

print("The maximum is", max_int)    # Do not change this line
