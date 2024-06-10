with open('Tools/Spelling Bee/dictionary_en.txt', 'r') as f:
    lines=f.readlines()
    f.seek(0)

with open('Tools/Spelling Bee/dictionary_en.txt', 'w') as f:
    for line in lines:
        if len(line.strip('\n'))>3:
            f.write(line.title())
        