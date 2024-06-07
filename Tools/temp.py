s='aaaabb'
letter_count = {char: s.count(char) for char in set(s)}
print(letter_count)
for k in letter_count:
    print(k)