# Create functions for encrypting and decrypting a message using the Caesar cipher.
# Allow the user to specify the shift value (number of positions to shift each letter).
# Handle both encryption and decryption using the same function with appropriate adjustments.
# Encrypt and decrypt the given message using the specified shift value.
# a-z is 97 to 122

#try making a recursive one like rotate.py?
def caesar_cypher(message: str, offset: int, decrypt: bool=False) -> str:
    result=''
    is_positive=True if offset>0 else False
    while abs(offset)>24: offset-=24 if is_positive else -24
    if decrypt:
        if is_positive:
            for letter in message:
                result+=chr((ord(letter)-offset)) if 97<=ord(letter)-offset<=122 else chr((123-offset))
            return result
        else:
            for letter in message:
                result+=chr((ord(letter)-offset)) if 97<=ord(letter)-offset<=122 else chr((96-offset))
            return result
    else:
        if is_positive:
            for letter in message:
                result+=chr((ord(letter)+offset)) if 97<=ord(letter)+offset<=122 else chr((96+offset))
            return result
        else:
            for letter in message:
                result+=chr((ord(letter)+offset)) if 97<=ord(letter)+offset<=122 else chr((123+offset))
            return result

print(caesar_cypher('abcdefghijklmnopqrstuvwxyz', -1))
print(caesar_cypher('bcdefghijklmnopqrstuvwxyza', -1, decrypt=True))