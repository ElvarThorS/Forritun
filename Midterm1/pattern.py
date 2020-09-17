max_integer = int(input("Input max integer: "))
counter = 0
while counter <= max_integer and max_integer > 0:
    for x in range(1,counter+1):
        print(x,end=" ")
    print()
    counter +=1
