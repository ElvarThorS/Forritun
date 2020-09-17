dog_age = int(input("Input dog's age: ")) # Do not change this line
human_age = 0
if dog_age > 0 and dog_age  <= 16:
    if dog_age == 1:
        human_age = 15
        print("Human age: ",human_age)
    elif dog_age > 1:
        human_age = 16
        human_age = human_age + dog_age * 4
        print("Human age: ",human_age)
else:
    print("Invalid age")