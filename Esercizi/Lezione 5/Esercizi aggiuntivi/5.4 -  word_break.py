# Given a string and a dictionary of words, determine whether the string can be segmented into a space-separated sequence of one or more dictionary words. 
# Each word in the dictionary must be a contiguous substring of the input string.

def word_break(input_string: str, word_dictionary: dict) -> bool:
    #exclusively takes words that might have gotten used to form input string, then sorts them into a list based on where they were found in it
    #which is useful so it can look for permutations instead of combinations
    useful_words=sorted([word for word in set(word_dictionary.values()) if word in input_string], key=lambda x: input_string.index(x))
    #list of every possible substring that can use the useful words if and only if they are forming a part of input_string
    useful_substrings=[]
    #first loop to reset substring for each word, remove first word from each cycle and collect the substring
    for i in range(len(useful_words)):
        substring=''
        #second loop to cycle through the other words and form the substring
        for word in useful_words[i:]:
            if substring+word in input_string:
                substring+=word
            else:
                continue
        useful_substrings.append(substring)
    return input_string in useful_substrings

print(word_break('ciaocomestaibene', {1: 'ciao', 7:'ci', 2:'come', 8:'mesta', 4:'stai', 5:'tutto', 6:'bene'}))