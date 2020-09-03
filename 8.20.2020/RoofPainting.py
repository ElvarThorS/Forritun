import math
length_cm = 50
degrees_str = input("Roof's angle in degrees: ")
# Convert input to integer
degrees_int = int(degrees_str)
# Convert degrees to radians in order to use the trigonometric functions in the math module
radians = degrees_int * math.pi/180
# Calculate the the height of the triangle
tan = math.tan(radians)
height_cm = tan * length_cm
print("To make the platform level, the height must be", round(height_cm, 1), "cm")
