#Algorithm
#1 make loop that loops n time
#2 make variables and get the sum of them 
n = int(input("Enter the length of the sequence: ")) # Do not change this line
count = 0
sequence1 = 1
sequence2 = 2
sequence3 = 3

while count < n:
    if sequence1 < sequence2:
        print(sequence1)
        sequence1 = sequence3 + sequence2
        count +=1
    elif sequence2 < sequence3:
        print(sequence2)
        sequence2 = sequence1 + sequence3
        count +=1
    elif sequence3 < sequence1:
        print(sequence2)
        sequence2 = sequence1 + sequence3
        count +=1
        