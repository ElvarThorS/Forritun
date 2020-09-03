rating = int(input("Input elo rating: ")) # Do not change this line
loop = True
# Fill in the missing code below
while loop ==True:
    if rating <=0:
        loop = False
    elif rating >=2700:
        print("Super grandmaster") # Do not change this line
        rating = int(input("Input elo rating: "))
    elif rating >=2500:
        print("Grandmaster") # Do not change this line
        rating = int(input("Input elo rating: "))
    elif rating >=2400:
        print("International") # Do not change this line
        rating = int(input("Input elo rating: "))
    elif rating <2400 and rating >1000:
        print("Amateur") # Do not change this line
        rating = int(input("Input elo rating: "))
    elif rating <1000 and rating >0:
        print("Invalid") # Do not change this line
        rating = int(input("Input elo rating: "))
    
