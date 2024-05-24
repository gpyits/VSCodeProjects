import pandas, random, re

#while ord(word[-1]) in list(range(32, 47))+list(range(57, 64)): word=word[:-1]

#remove duplicates
#remove words larger or smaller than 5
#remove words with numbers or punctuation in it
#I'll have to move the words to another file
with open('/home/studente418/VSCodeProjects/Tools/oldwords.txt', 'a+') as file:
    file.seek(0)
    lines=file.readlines()
    for word in lines:
        if len(word)!=5:
            lines.remove(word)
        