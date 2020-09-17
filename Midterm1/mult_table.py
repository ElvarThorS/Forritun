number_to_multiply = int(input("Input number to multiply: ")) # Do not change this line
how_often = int(input("Input how often to multiply: ")) # Do not change this line
diplay_number = 0
for x in range(1,how_often+1):
    display_number = number_to_multiply * x
    print(display_number)
