a_str = input("Input a string: ")
upper = 0
lower = 0
for ch in a_str:
    if ord(ch) >= 97 and ord(ch) < 123: 
        lower +=1
    elif ord(ch) < 97 and ord(ch) > 64:
        upper +=1
print(lower)
print(upper)