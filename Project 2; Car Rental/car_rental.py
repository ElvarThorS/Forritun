import math

print("Welcome to car rentals!")
loop  = True
budget_charge = 40
daily_charge = 60
while loop == True:
    answer1 = str(input("Would you like to continue (y/n)? "))
    if answer1 == "y":
        answer2 = str(input("Customer code (b or d): "))
        if answer2 == "b":
            days = int(input("Number of days: "))
            odometer_start  = int(input("Odometer reading at the start: "))
            odometer_end  = int(input("Odometer reading at the end: "))
            miles_driven = round(int(odometer_end - odometer_start),0)
            print("Miles driven:",miles_driven)
            amount_due = math.floor(float((budget_charge*days) + miles_driven * 0.25)*10)/10
            print("Amount due:",amount_due)
        elif answer2 == "d":
            days = int(input("Number of days: "))
            odometer_start  = int(input("Odometer reading at the start: "))
            odometer_end  = int(input("Odometer reading at the end: "))
            miles_driven = round(int(odometer_end - odometer_start),0)
            print("Miles driven: ",miles_driven)
            if miles_driven <100:
                amount_due = math.floor(float(daily_charge*days)*10)/10
                print("Amount due:",amount_due)
            elif miles_driven >=100:
                amount_due = math.floor(float((daily_charge*days)+(miles_driven-100*days)*0.25)*10)/10
                print("Amount due:",amount_due)
    elif answer1 == "n":
        loop = False