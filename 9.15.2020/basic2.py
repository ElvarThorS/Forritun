# Your function definition goes here
def digit_counter(str):
    digits = 0
    for ch in str:
        if ord(ch) >= 48 and ord(ch) <= 57:
            digits += 1
        else:
            pass
    return digits

input_str = input("Enter a string: ")

# Call the function here
digit_count = digit_counter(input_str)

print("No. of digits:", digit_count)