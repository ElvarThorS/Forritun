age = int(input("Input age: ")) # Do not change this line
if age >=65:
    ticket_price = float(40) * 0.60
    print(ticket_price)
elif age < 20 and age > 5:
    ticket_price = float(40) * 0.80
    print(ticket_price)
elif age <= 5:
    ticket_price = float(0)
    print(ticket_price)
else: 
    ticket_price = float(40)
    print(ticket_price)