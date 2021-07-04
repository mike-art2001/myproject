import hashlib

h = hashlib.md5(b'hashing strings')
print("the equivalent byte of hash is:", end="")
print('sha512',hashlib.sha512(b'hashing string').hexdigest())
print("sha256",hashlib.sha256(b'hashing string').hexdigest())
print("blake2b",hashlib.blake2b(b'hashing string').hexdigest())
print(h.hexdigest())















