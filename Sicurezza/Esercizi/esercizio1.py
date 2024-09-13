# Sapendo che la chiave di cifra è: XXXXIsASecretKey
# (non conoscete i primi 4 caratteri della chiave)
# e che il messaggio cifrato è: OgJuOYJZT0FDb47DBOkNgA==
# NB: la parte ignota delle chiave contiene esclusivamente maiuscole e minuscole
from encrypt import *

#bogo
# import random
# while True:
#     add=''
#     cycles=0
#     key = "IsASecretKey"
#     for i in range(4):
#         add+=random.sample(random.choice(['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']), 1)[0]
#     try:
#         key=add+key
#         text = "OgJuOYJZT0FDb47DBOkNgA=="
#         decrypted_text = decrypt(text, key)
#         print(f'key found: {key}')
#         print("Decrypted Text:", decrypted_text)
#         if add=='This':
#             print(f'Hooray!\nCycles: {cycles}')
#             break
#         else:
#             cycles+=1
#     except:
#         continue

#real 65-90 97-122
from itertools import combinations
while True:
    caps={i:n for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' for n in range(25)}
    print(caps);break
    letters='abcdefghijklmnopqrstuvwxyz'
    cycles=0
    add=''
    key = "IsASecretKey"
    try:
        key=add+key
        text = "OgJuOYJZT0FDb47DBOkNgA=="
        decrypted_text = decrypt(text, key)
        print(f'key found: {key}')
        print("Decrypted Text:", decrypted_text)
        if add=='This':
            print(f'Hooray!\nCycles: {cycles}')
            break
        else:
            cycles+=1
    except:
        continue