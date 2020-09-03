# These lines you can keep as is
print("Think of a number between 1 and 100 (inclusive)")
print("I am going to guess what it is")
input("Press enter when you are ready to play")

# Here you might want to initialize some variables
lowest = 1
highest = 100
counter = 0
# Then start a while loop
while lowest <= highest:
    guess = (lowest + highest)//2 
    # These lines you can keep as is
    print("Is the number", guess, "?")
    print("Type one of the following letters and press enter:")
    print("h: if the guess is too (h)igh")
    print("l: if the guess is too (l)ow")
    print("c: if the guess is (c)orrect")
    print("q: to (q)uit the game")
    cmd = input()
    if cmd == "l":
        counter +=1
        lowest = guess +1
    elif cmd == "h":
        counter +=1
        highest = guess -1
    elif cmd == "c":
        print("I AM VICTORIOUS")
        break
    elif cmd == "q":
        print("Quitter")
        break
    
    else:
        print("Invalid")
else:
    print("Tsk, tsk, don't try to cheat me")
    
    # Now it's up to you to check the command and take appropriate action


