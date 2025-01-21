import hashlib
#Hashing is not reversible

def hash_text(text):
    hash_object = hashlib.sha256()
    hash_object.update(text.encode('utf-8'))

    return hash_object.hexdigest()

input_text = "Hello, World"
hashed_text = hash_text(input_text)

print(f"Original Text: {input_text}")
print(f"Hashed Text: {hashed_text}")