import hashlib
import random

def generate_key(passphrase):
    return hashlib.sha256(passphrase.encode()).digest()

def decrypt(encrypted_data, passphrase):
    key = generate_key(passphrase)
    decrypted_data = []
    random.seed(key[:4])

    for i, encrypted_char in enumerate(encrypted_data):
        shift_value = (random.randint(1, 100) + i + key[i % len(key)]) % 256
        decrypted_char = (encrypted_char - shift_value) % 256
        decrypted_data.append(chr(decrypted_char))

    return ''.join(decrypted_data)

def read_encrypted_data(file_name):
    with open(file_name, 'rb') as file:
        encrypted_data = list(file.read())
    return encrypted_data

def decode():
    passphrase = "my_secure_passphrase"
    encrypted_data = read_encrypted_data("encrypted_data.diec")
    decrypted_text = decrypt(encrypted_data, passphrase)
    return decrypted_text

if __name__ == "__main__":
    decrypted_text = decode()
    print(decrypted_text)
