# max_of_three function definition goes here
def max_of_three(int1,int2,int3):
    if int1 > int2 and int1 > int3:
        maximum =  int1
    elif int2 > int1 and int2 > int3:
        maximum =  int2
    elif int3 > int1 and int3 > int2:
        maximum =  int3
    return maximum

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))

# Call the function here
maximum = max_of_three(first,second,third)
print("Maximum:", maximum)