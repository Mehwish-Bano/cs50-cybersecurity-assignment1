import hashlib

password = "mypassword"

# convert to bytes
encoded = password.encode()

# create hash
hash_object = hashlib.sha256(encoded)
hashed_password = hash_object.hexdigest()

print("Original Password:", password)
print("Hashed Password:", hashed_password)
