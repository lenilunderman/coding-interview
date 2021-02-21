#The " in " Syntax - is used to determine if a letter or a substring exists in a string.
game = "Popular Nintendo Game: Mario Kart"
print("p" in game)

# iterate an string
str = "love"
for s in str:
    print(s)
    
# check the lenght of an string or lsit
word1 = "cavalo"
words = ["bala", "pera"]
print(len(word1)) # return the number of letter in word
print(len(words)) # return the number of items

# strip method - clean an white space in python
text1 = '   apples and oranges   '
text1.strip()
print(text1)

# split , split the text on the instance u chose.
info = 'Game is on!'
print(info.split())

# finds a position index of something on the string
find100 = "the number is 200 , 100 or 50"
print(find100.find("or"))

# join method, great to join things together.
words_list = ["piece"," of ", "cake"]
word_senct = ("").join(words_list)
print(word_senct)
print(type(word_senct))
