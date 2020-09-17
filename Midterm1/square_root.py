import math

start_int = int(input("Input starting integer: "))
square_int = start_int
while square_int >=2:
    square_int = math.sqrt(square_int)
    print(round(square_int,4))