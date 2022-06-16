file = open("DBLP.text", 'r')

data = list (file.read())
for word in data:
    if not word.isalpha():
        print word
