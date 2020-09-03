n = int(input("Input a natural number: ")) # Do not change this line
counter = 1
# Fill in the missing code below
while counter <= n:
    if n ==1:
        prime = False
        break
    elif n % 2 == 0 and n !=2:
        prime=False
        break
    elif n % counter == 0 and counter == n or counter == 1:
        prime = True
        counter +=1
    else:
        counter +=1
    
# Do not changes the lines below
if prime:
    print("Prime")
else:
    print("Not prime")