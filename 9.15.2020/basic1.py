# The function definition goes here
def every_other(str):
    counter = 0
    new_str = ""
    for ch in str:
        if counter % 2 == 0:
            new_str += ch
            counter +=1
        else:
            counter +=1
    return new_str
input_str = input("Enter a string: ")


# You call the function here
new_string = every_other(str(input_str))
print("Every other character: {}".format(new_string))