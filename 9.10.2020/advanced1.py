# Keep these 2 lines
text_to_translate = input("Text to translate: ")
VOWELS = "aeiouyAEIOUY"
# ...add your code here
text_list = text_to_translate.split()
translation = ""
for word in text_list:
    if word[0] in VOWELS:
        word = word + "yay"
        translation = translation + word + " "
    elif word[0] not in VOWELS:
        while word[0] not in VOWELS:
            word = word[1:]+word[0]
        word =word +"ay"
        translation = translation + word +" "
# Keep this line
print("Translation:", translation)