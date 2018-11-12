import hashlib

# md5
m = hashlib.md5

print(m)    # <built-in function openssl_md5>


m.update('Hello World'.encode('utf-8'))