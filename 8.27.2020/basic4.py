n = int(input("Input an int: ")) # Do not change this line
counter = 1
# Fill in the missing code below
while counter <= n:
    if n % counter == 0:
        print(counter)
    counter +=1