# Gabriel Crozier Budget Calculator
from cryptography.fernet import Fernet

print('\033c')

key1 = Fernet.generate_key()
with open("secret.key", "wb") as key_file:
    key_file.write(key1)



with open("secret.key", "rb") as key_file:
    key = key_file.read()
f = Fernet(key)

message = "Sensitive data to encrypt"
encrypted_message = f.encrypt(message.encode())

print("Original message:", message)
print("Encrypted message:", encrypted_message)


with open("secret.key", "rb") as key_file:
    key = key_file.read()
f = Fernet(key)
decrypted_message = f.decrypt(encrypted_message).decode()

print("Decrypted message:", decrypted_message)