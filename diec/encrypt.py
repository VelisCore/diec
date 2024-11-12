import hashlib
import random
import os

def generate_key(passphrase):
    return hashlib.sha256(passphrase.encode()).digest()

def encrypt(data, passphrase):
    key = generate_key(passphrase)
    encrypted_data = []
    
    random.seed(key[:4])  

    for i, char in enumerate(data):
        shift_value = (random.randint(1, 100) + i + key[i % len(key)]) % 256
        encrypted_char = (ord(char) + shift_value) % 256
        encrypted_data.append(encrypted_char)

    return encrypted_data

def save_encrypted_data(file_name, encrypted_data):
    with open(file_name, 'wb') as file:
        file.write(bytes(encrypted_data))

def encode(passphrase, text):
    encrypted_data = encrypt(text, passphrase)
    save_encrypted_data("encrypted_data.diec", encrypted_data)
    print("Encryption successful. Encrypted data saved to 'encrypted_data.diec'.")

encode(passphrase="my_secure_passphrase", text="This is some text that needs to be encrypted.")