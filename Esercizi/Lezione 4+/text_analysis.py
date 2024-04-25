# Create a function that reads a text file and counts the number of occurrences of each word.
# The function should print a report showing the most frequent words and their number of occurrences.
# You can use a for loop to iterate over the words in the text and a dictionary to store the occurrences.
# Implement error handling to handle missing files or other input issues.

def text_analyzer(file: str):
    with open(file, 'r') as file:
        words={}
        for line in file.readlines():
            for word in line.split():
                word=word.lower()
                #assuming no writing errors, removes common punctuation
                while ord(word[-1]) in [i for i in range(32, 47)]+[i for i in range(57, 64)]: word=word[:-1]
                #counts words
                if word in words:
                    words[word]+=1
                else: 
                    words[word]=1
        print(words)

text_analyzer('yourfile.txt')