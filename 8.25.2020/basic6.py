year = int(input("Input a year: ")) # Do not change this line

# Fill in the missing code below

print(year%4==0 and((year%100!=0)or(year%400==0)))