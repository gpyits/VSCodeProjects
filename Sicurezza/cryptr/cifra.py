from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# Per importare una chiave pubblica
# keyDER = base64.b64decode(pubkey)
# seq = base64.asn1.DerSequence()
# seq.decode(keyDER)
# keyPub = RSA.construct((seq[0], seq[1]))

# Per iniziare generiamo una coppia di chiavi e le stampiamo
# Generating RSA Key Pair
# Una volta stampate, non serve più
key_pair = RSA.generate(2048)
print(key_pair.export_key())
public_key = key_pair.publickey()
print(public_key.export_key())
exit(0)

sPriv = "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEA1lxZu5fo5fyZiBVCc+Hu4PpT0tMAMRbw4BlBYaYJHL1ptaDQ\naSxmc9FfnTyg3oUXE/Lj6FErItCPLD+Ps55YHatM4w4CEJ0XjpVsJ/RF2GBU2Dbk\n2VgiplX47JUPgYkdYYoqDp/sEczSvHakYzch0JWErq6ZEBfiYKgpGP2zzkI/NpzV\nz4/SiTN7CZdokuvdTc7cZusNcX9cBnEVMTjKDALSRJHo7xZzFmssglRUX1j7ebMt\nvH+JwAjkQ81+WwtilRLRIYAjTRCItHHVFpec6lbiWSWtAHpZuBIGOGemqD1yYajG\nsxjsodosC1K/0pHH+X55cSLIrQ1SkMqCd5DokwIDAQABAoIBACedybexy4k1tepA\ng5eHGe7aVMOR22c3Ji1EfaDeXrDBENhQcDP/0K928oTMv65gSnOVYCl/VsmIYe17\nkcNQcFiLYBpWbGtFnSTs2KBJtN7YbtXGz2SbtUuod+jBY6w8+wEb18n8JFTl1cye\n4KK1fbpe57ag7gjbYSsb6PyFZsWngg5cNRkrcXvIKZ9pnq47g8RRr9vHEjKBLwf2\nHCyS13EKM9YzFgL06RU0kdKDKIzFooFHz+34KWtdjIlKgF5et6FpwPXmmBVZENYz\ne0mMhcYZfe19XgkBS5Ic8b5MWTuGIk1VOJCm/JicokU0e2CQGP8pCQpKfrNxuGxJ\noGl9nwECgYEA5uBVBqer2XGCvGELYZp/3xjBostDlKwqoEryAQxJOzmJVzssCc7h\nrkfScTA2fiwtD4P+agJ3wIGrKasFom9g+rx422kmOfJiD+bGyHqSl4LawPNczSDr\nb12vnRcDYc2Gy6sOWaZlNQ7SvLXywkvzzfc9ZniX3KoNCx4hkjweLbkCgYEA7a/v\nIjvU3jlN4gHB1nHzOLcicR9lke6EYkKolkkkOoi3miP3tLnYh7iqKxuQlUV4tAOx\nBN9lpKVc4rH+xxqxCtg75X6zkjC5Ka96qJJiteCRWbnAg8Ei8LTV/FaGmpW9H16E\nqHHTkFqyUoyxeotyfOYkfnDb5PQcxffbvBZKTqsCgYB6H2uaS5LBQCOxVXvZswm0\njrnOTMqAl9ksVLhSCZeq9jJJrAkNXxtNPrx4FtKcRu3G6UDn/kotz+kj70zZsSSR\nPKSJGsOXnzhzxNSdMwjbj+H6ckBCWQlwLRQ5efTWBQsqLF842KVsPV0HaQ7x648Z\nAZC+5Uce9+xSVyvW2Gn2MQKBgQDKZwc8H7clhabMzrJB6sczhL/PlOzpWDNjeWAW\nmjI/piyzFe3Z+GhrKtW937s/YelnYb1caOAlVKvEX86VviUFFx3qT/qaguMqnEPX\nSNDGEHW18nf9unoGf/e46fW1rc1e6R4OUt/WDWXM5gI8WIMl2NU61uBqF3ZpHqf/\ngvvEAQKBgDIbB+R+KQvG0ripXS2x6o4CTma37/Q/J58O6RkRXXg2A5tf5QFqhgQg\n4yweaee3CfMDuA+g2hMWG5VAboP01BkCGRMc1r1B2UFYsj1v/nZQo+vpJG5sylCV\nU8p/RSMXuLKrHOd8rjS1JyZW466ch6JqFI2kllWEh+sz9ZIJgkxw\n-----END RSA PRIVATE KEY-----"
sPub = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtcjn5ua+pVdIHQaTCQin\nofFb7sHgDFmtamBlIAfofMyaH1tk5l3x5KHZhRatBiygDlSL8ts5DfUB1yrgNFYS\nr4h8GuHywNr9DF1tpgt3GwtXuOInF8gbrxCDBCOiPqqwzPa0lK+NIlQxxibhf8jC\nzUjZ8IPATXeW619TDWcSNxH5ER7z+MRM0gq9oYVhneKtN7XbHjv9ne7OK5aS8gCm\noHfWkx7AnMM3Ns2P44om8gDH/SPOmh1VSpfK1wqwyTHfKZDtgq84ChgqxfhzB09S\nCmnewOQJsY0yIks69AElftKhfOSYZw4MY5XOzm+sMapNpRCL8RUYzIk6J+bx0Y8Q\nHwIDAQAB\n-----END PUBLIC KEY-----"
# sPub = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3AqNkw+4Pnd0fKkYQRKk\nr8BDrUDVxD75cHizbkfKE4CnWGEWfP7Yi25nBp10qCyOdBfr1LD7DGXJpGJA4L1t\neUOzbT2ztEZGPuur532z/bQdcIteIIipO4fGzsCiSkeXVu+W/rLWHGuHgss2ULxe\nAx8mzbSc1UqdV4z1wmERprqNLLZZIRAewYkdBIhQ57IvxX+DXeQTPkPPO4jZTmWV\ncf7/JpmDrDiOWbl/fg/UPNxzxvO3C2MA3FEr1ZmvUgqKX1M3XZS6FKvJCvnNQdYx\nPVRe3Ra6KOdA6vdfCOCoGFH8CjwAI9Aquz8AM951Sk3tQp8TGXeQOx2H2vemohmA\nbQIDAQAB\n-----END PUBLIC KEY-----"

# Ora dobbiamo ricreare le chiavi a partire da queste due stringhe
key_pair = RSA.import_key(sPriv)
public_key = RSA.import_key(sPub)


# Function to encrypt message
def encrypt_message(message, pub_key):
    cipher = PKCS1_OAEP.new(pub_key)
    encrypted_message = cipher.encrypt(message.encode("utf-8"))
    return base64.b64encode(encrypted_message).decode("utf-8")


# Function to decrypt message
def decrypt_message(encrypted_message, priv_key):
    cipher = PKCS1_OAEP.new(priv_key)
    decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted_message.decode("utf-8")


# Example usage
# message = ""
encrypted_message = "vvPzq3OcIWfIdI+aDEOAX3oMam9odn/iBIGdX0BV+GAw1FwX+zqu4WNGXgbka4m/7bCG14ZHL6jlwgrX2ImvXuBgo6GGeuDDAm7CPbRylOsVL0n2fTSeBLgpgevTxFOUdHsJcnNKUZ6P/dGC/cfZHcfukCUgWdGvxWN3CW2wFf8hI98+mI9jFlU2ZKgAYtYrLbuS3g0J0/i8soI+vOiCatcd+FYEuYv+NEN/HI4n/9S2g6DtdYrun1tsyGxnN+J3EwjFiwQWnCHVX1ev0oU5LPjNPv4cW6vVCmjZ6AoatwhDe1A7Wdb/vYxa+MlOlkzgH45lIknLu5rjur/r/jqQUA=="
encrypted_message = encrypt_message(message, public_key)
decrypted_message = decrypt_message(encrypted_message, key_pair)

# print("Original Message:", message)
# print("Encrypted Message:", encrypted_message)
# print("Decrypted Message:", decrypted_message)