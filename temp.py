with open('Tools/dictionary_it.txt', 'r') as f:
    lines=f.readlines()
    f.seek(0)

with open('Tools/dictionary_it.txt', 'w') as f:
    for line in lines:
        if len(line.strip('\n'))==5:
            f.write(line.upper())