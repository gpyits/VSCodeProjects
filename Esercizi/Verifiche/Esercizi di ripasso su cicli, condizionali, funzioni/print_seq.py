# Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
# a) 1, 2, 3, 4, 5, 6, 7
# b) 3, 8, 13, 18, 23
# c) 20, 14, 8, 2, -4, -10
# d) 19, 27, 35, 43, 51

def print_seq(): 

    print("Sequenza a):")
    for n in [1, 2, 3, 4, 5, 6, 7]:
        print(n)

    print("Sequenza b):")
    for n in [3, 8, 13, 18, 23]:
        print(n)

    print("Sequenza c):")
    for n in [20, 14, 8, 2, -4, -10]:
        print(n)

    print("Sequenza d):")
    for n in [19, 27, 35, 43, 51]:
        print(n)
    
    return

print_seq()