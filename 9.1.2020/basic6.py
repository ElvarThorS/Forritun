length = int(input("Input the length of series: "))
sum = 0
for i in range(2,length*2+1,2):
    if i % 4 == 0:
        reverse = i * -1
        sum +=reverse
        print(reverse)
    else:
        sum +=i
        print(i)
print("Sum: ",sum)