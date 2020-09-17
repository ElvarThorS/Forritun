a_str = input("Input a float: ")
a_float = round(float(a_str),2)
if ".0" in str(a_float):
    print("     ",str(a_float)+"0")
else:
    print("     ",a_float)