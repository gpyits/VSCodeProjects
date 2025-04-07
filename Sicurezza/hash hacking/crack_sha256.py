import hashlib
import itertools
from itertools import combinations
from itertools import product

# data="ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb"

# for c in range(0x21, 0x7E):
#     toCheck = chr(c).encode()
#     hashed_password = hashlib.sha256(toCheck).hexdigest()
#     if hashed_password == data:
#         print(f"Password found: {chr(c)}")
#         break

data="d04b98f48e8f8bcc15c6ae5ac050801cd6dcfd428fb5f9e65c4e16e7807340fa"

charset = "".join(chr(i) for i in range(0x21, 0x7e))
for length in range(4, 5):
    for attempt in itertools.product(charset, repeat=length):
        toCheck = ''.join(attempt).encode()
        # print("".join(attempt))
        hashed_password = hashlib.sha256(toCheck).hexdigest()
        if hashed_password == data:
            print(f"Password found: {''.join(attempt)}")
            exit()

