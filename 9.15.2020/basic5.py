# palindrome function definition goes here
def palindrome(sentance):
    new_sentance = ""
    for ch in sentance:
        if ord(ch) >= 33 and ord(ch) <= 47 or ch == " ":
            new_sentance += ""
        else:
            new_sentance += str(ch)
    new_sentance = new_sentance.lower()
    if new_sentance[::-1] == new_sentance:
        return True
    else:
        return False
in_str = input("Enter a string: ")
if palindrome(in_str) == True:
    print('"{}" is a palindrome.'.format(in_str))
else:
    print('"{}" is not a palindrome.'.format(in_str))
# call the function and print out the appropriate message