max_days = int(input("Input max number of days: "))
target = int(input("Input dollar target: "))

# Fill in the missing code
dollars = 0
days_when_amount_acquired = 0
for i in range(0,max_days):
    if days_when_amount_acquired >= max_days and dollars < target:
        days_when_amount_acquired = 0
        break
    elif dollars < target:
        dollars += 2**i
        days_when_amount_acquired +=1
    else: 
        break
    
print('Days needed:',days_when_amount_acquired)
