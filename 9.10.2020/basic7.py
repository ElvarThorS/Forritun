my_int = int(input('Give me an int >= 0: '))
# Fill in the missing code
bin_str = ""
quotient_check = 1
number = my_int
while quotient_check != 0:
    quotient, remainder  = divmod(number,2)
    if quotient == 0:
        bin_str =  str(remainder) + bin_str
        quotient_check = 0
    elif quotient != 0:
        bin_str = str(remainder) + bin_str
        number = quotient
    
print("The binary of {} is {}".format(my_int,bin_str))