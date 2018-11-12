import hashlib

# mad5
hash = hashlib.md5()

print(hash)     # <md5 HASH object @ 0x10539baf8>

hash.update('Hello World'.encode('utf-8'))

print(hash.hexdigest())     # b10a8db164e0754105b7a99be72e3fe5

hash.update('Asaki'.encode('utf-8'))

print(hash.hexdigest())     # a271199cecbafdb4de72cf90b116cd66


# 两者之间的关系：
m2 = hashlib.md5()
m2.update('Hello WorldAsaki'.encode('utf-8'))
print(m2.hexdigest())   # a271199cecbafdb4de72cf90b116cd66


# sha
sha = hashlib.sha256()

sha.update('Hello World'.encode('utf-8'))

print(sha.hexdigest())  # a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e

# 不可逆
