# Your function definition goes here
def valid_date(in_date):
    num_count= 0
    period_count = 0
    for ch in in_date:
        if ch.isdigit():
            num_count +=1
        elif ch == ".":
            period_count +=1
        else:
            return False
    else:
        if num_count + period_count != 8:
            return False
    day = in_date.split(".")[0]
    month = in_date.split(".")[1]
    year = in_date.split(".")[2]

    if len(day) !=2 or len(month) !=2 or len(year) != 2:
        return False
    if int(day) > 31 or int(day) <1:
        return False
    if int(month) > 12 or int(month) <1:
        return False
    if int(year) > 99 or int(year) <0:
        return False
    return True
date_str = input("Enter a date: ")
if valid_date(date_str):
    print("Date is valid")
else:
    print("Date is invalid")  