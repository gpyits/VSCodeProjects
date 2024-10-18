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

sPriv =                                             #'-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEA1K9CLmUpYQIOl2Iw20EyVHwDWSGCE+FFvKD54ek9oi0nW6N7\n+dJyfMEJblu5DNMepERcAHZW81pxD7Tsfo+x2dZHZwr2RTmeCoU+7HB3N8B4QKAr\nS6WtnU3Fg4BK9tEkh3Px70BOwuIDpwnEemXNNmWFuulVk8zaWrqGCqm5P2Ct9Si+\nmcmEf44vTEItWQfyFQQR3oi1vhWz7+uPN42bLzGCCoqvZUNpgY8QfO4sbWy8gOJX\nJX7kNuonpeHyL+UMkzxc1GF1j8DNFQANS3qBu7V/+/icMY//2AFHAnseEcHQxaHv\nRpkLCk3skIMM+1SBboNdwhxAgCAsAHcE57XnTQIDAQABAoIBAEj5EQYGI5prMEJ0\nqDqyNeiS3Ds6qfzUMC82NEZ01nbMc1KX1zOyJyHywZ+hzO4/iaXm5oIqGE9K2rv+\n4Z3TA7ywLrOGKVU7HaSSbzKErALvANN7oR9FazorsvcZj577x0LKX1otgFiRX5ty\nWH1+bFiboLSu1nPtt4WltdP2w96gVstws4OsFs+2P4RYkPo9sVAMZ6h8rtZK/aNU\nJuIyUkkgDwWWMqyHvlIiZqU9J80EWtQBXITPdix+ui7aFaadzxysc7K0oJqEn2D8\nOHMpZBmyIuhnuwmdr2RCGXtGI9uV/CQpPUF2NEJAAY5TtkyNUzFk9SEm3w87A8LI\nckrmU2kCgYEA2Yozs7QoKuni97ATd4+vezf7bQVMzTuunPyXXaN+5Nuhnpx0QyW3\ntiRLleCFtOFTUVkNSzZoifBNT9umMu7mpN2ibbzMjtwI34sEkXRSk6KRbd+k24Wz\njAVWohM8weodxzamEPvnS+Dqm2X/hHYLiuPigfDTHtn9gjAKexOQLh8CgYEA+klP\nLVIQcBstrHr14nOWT9ygi0pw8lW1KvYhx3HX9+MB5Qz7zVR9NZvH8b8LB+2Y9ByD\ndOxVGERTT9Bgz3sQDgOR3oZ9QFVYxj4vvyegQPHiGZiBhq8tYyf3vtqHBy5tjXBp\nQr5qjIoWhFk+4BzeChHbJKgYYQnpVzU5IoeoJRMCgYAw1mb/DA4MfE+ZHa1xJQ/X\nUN0gP5Vbae+sjMSKoB7n0Cr7idJMFNamjIVvk2VRE1j6JUznusJDXXBt4jjwrFOZ\nZayGiGFAHUPcs8AFy6CSRmfxy8ieA+koITau0jTMr/uZcrpbi8IEde0VkBOKMFot\nBzYdx+wNvBC+vnxL3zt6LwKBgH61/JLKOC45ZD8tJSzXLeMSpGjAcDwPrh+o6mMJ\nvLfvwnbOwvAp9RXd3zUBbjk+TbBQezEHsPEPLkp7CXghKnid0Ayjc+fNDZuXwh55\nlkUq8DfbIMAqEcVgZ6nFApVdKPNxVKkIs/KgulOYxx85HiRk89g0Ddua4/pVpK5Z\nlYPnAoGBAI0ISI0U3ypiSoIgULk5MY4Z2n8JGgq2rZ4jEwI4znT3ijHWu5TAG6h+\nAZVSF04NUxO/a9Oi6pinTaX4ywMnRn3JzX3SwvzHfZ0RG3lYHmvzZRPRU4g2huFG\nEEwvBLzX2JMMFlw/T6aPykw3h3uh7f9ztuilY0fcf5DH+eiRiOsl\n-----END RSA PRIVATE KEY-----'
sPub =                                              #'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1K9CLmUpYQIOl2Iw20Ey\nVHwDWSGCE+FFvKD54ek9oi0nW6N7+dJyfMEJblu5DNMepERcAHZW81pxD7Tsfo+x\n2dZHZwr2RTmeCoU+7HB3N8B4QKArS6WtnU3Fg4BK9tEkh3Px70BOwuIDpwnEemXN\nNmWFuulVk8zaWrqGCqm5P2Ct9Si+mcmEf44vTEItWQfyFQQR3oi1vhWz7+uPN42b\nLzGCCoqvZUNpgY8QfO4sbWy8gOJXJX7kNuonpeHyL+UMkzxc1GF1j8DNFQANS3qB\nu7V/+/icMY//2AFHAnseEcHQxaHvRpkLCk3skIMM+1SBboNdwhxAgCAsAHcE57Xn\nTQIDAQAB\n-----END PUBLIC KEY-----'

Priv = '-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEA...\n-----END RSA PRIVATE KEY-----'
Pub  = '-----BEGIN RSA PRIVATE KEY-----\nMIIBIjANBgkqhkiG...\n-----END RSA PRIVATE KEY-----'

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