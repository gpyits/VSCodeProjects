# Create functions for encrypting and decrypting a message using the Caesar cipher.
# Allow the user to specify the shift value (number of positions to shift each letter).
# Handle both encryption and decryption using the same function with appropriate adjustments.
# Encrypt and decrypt the given message using the specified shift value.
# a-z is 97 to 122

#encryption/decryption handler, shift single letter by one for specified number times
def shift(letter: str, offset: int, is_positive: bool) -> str:
    if offset==0:
        return letter
    else:
        if is_positive:
            return shift(chr(ord(letter)+1), offset-1, is_positive) if ord(letter)+1!=123 else shift(chr(97), offset-1, is_positive)
        else:
            return shift(chr(ord(letter)-1), offset+1, is_positive) if ord(letter)-1!=96 else shift(chr(122), offset+1, is_positive)

#handles result message assembly, shaves offset so it doesn't overflow past 25
def caesar_cypher(message: str, offset: int, decrypt: bool=False) -> str:
    result=''
    is_positive=True if offset>0 else False
    while abs(offset)>24: offset-=24 if is_positive else -24
    if decrypt==True: 
        is_positive=False
        offset=-offset
    return ''.join(shift(letter, offset, is_positive) for letter in message)

print(caesar_cypher('abcdefghijklmnopqrstuvwxyz', 1))
print(caesar_cypher('bcdefghijklmnopqrstuvwxyza', 1, decrypt=True))