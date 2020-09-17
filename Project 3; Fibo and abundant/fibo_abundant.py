#Algrím:
#Fibonacci;
#Ef slegið er inn f, spurt er um hversu löng runan á að vera.
#Setjum innsláttinn inn í for lykkju og keyrum length+1 sinnum.
#Síðan er fibonacci prentað út.
#Til þess þurfum við breyturnar f0, f1 og f2 (Úr strjálli stærðfræði)
#Þá þurfum við fyrst að hafa f0 = 0, f1 = 1 og f2 = f0 + f1
#Ef f0 er minna eða jafnt og f2 þá gerum við f0 = f1 + f2
#Ef f1 er minna en f0 þá gerum við f1 = f2 + f0
#Ef f2 er minna en f1 þá gerum við f2 = f0 + f1
#Abundant;
#Ef slegið er inn a, spurt er um max_num, eða hæstu töluna sem á að skoða.
#Setjum innsláttinn inn í for lykkju og keyrum max_num sinnum.
#Setjum aðra for lykkju fyrir innan for lykkjuna og keyrum í current_num sem er talan sem ytri for lykkjan er í.
#Ef current_num % x == 0 þá er x sett inn í breytuna "num_sum"
#Ef num_sum > current_num þá prentast current_num
#Both:
#Afrita og lími kóðann sem var í fibonacci og abundant partinum í þessari röð fyrir neðan if setninguna.
choice = input("Input f|a|b (fibonacci, abundant or both): ")
if choice == "f":
    f0 = int(0)
    f1 = int(1)
    f2 = f0 + f1
    length = int(input("Input the length of the sequence: "))
    print("Fibonacci Sequence:")
    print("-------------------")
    for x in range(1,length+1):
        if x == 1:
            print(f0)
        elif x == 2:
            print(f1)
        elif x == 3:
            print(f2)
        elif f0 <= f2:
            f0 = f1 + f2
            print(f0)
        elif f1 < f0:
            f1 = f2 + f0
            print(f1)
        elif f2 < f1:
            f2 = f0 + f1
            print(f2)
elif choice == "a":
    max_num = int(input("Input the max number to check: "))
    print("Abundant numbers:")
    print("-----------------")
    for current_num in range(1,max_num+1):
        num_sum = 0
        for x in range(1,current_num):
            if current_num % x == 0:
                num_sum += x
        if num_sum > current_num:
            print(current_num)

elif choice == "b":
    f0 = int(0)
    f1 = int(1)
    f2 = f0 + f1
    length = int(input("Input the length of the sequence: "))
    print("Fibonacci Sequence:")
    print("-------------------")
    for x in range(1,length+1):
        if x == 1:
            print(f0)
        elif x == 2:
            print(f1)
        elif x == 3:
            print(f2)
        elif f0 <= f2:
            f0 = f1 + f2
            print(f0)
        elif f1 < f0:
            f1 = f2 + f0
            print(f1)
        elif f2 < f1:
            f2 = f0 + f1
            print(f2)
    max_num = int(input("Input the max number to check: "))
    print("Abundant numbers:")
    print("-----------------")
    for current_num in range(1,max_num+1):
        num_sum = 0
        for x in range(1,current_num):
            if current_num % x == 0:
                num_sum += x
        if num_sum > current_num:
            print(current_num)