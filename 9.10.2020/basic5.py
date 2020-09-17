a_str = input("Input a string: ")
letter_count = 0
word_count = 0
for ch in a_str:
    if ord(ch) > 53 and ord(ch) < 173:
        letter_count +=1
    elif ch == " ":
        word_count +=1
word_count +=1
print('No. of letters: {}, no. of words: {}'.format(letter_count,word_count))
