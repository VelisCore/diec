from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def generate_key(passphrase, salt):
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,
        salt=salt,
        iterations=100_000,
        backend=default_backend()
    )
    return kdf.derive(passphrase.encode())

def encrypt(data, passphrase):
    salt = os.urandom(16)
    key = generate_key(passphrase, salt)
    iv = os.urandom(12)

    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(data.encode()) + encryptor.finalize()

    return salt, iv, encryptor.tag, encrypted_data

def save_encrypted_data(file_name, salt, iv, tag, encrypted_data):
    with open(file_name, 'wb') as file:
        file.write(salt + iv + tag + encrypted_data)

def encode_exp():
    passphrase = "my_secure_passphrase"
    text = "This is some text that needs to be encrypted."
    salt, iv, tag, encrypted_data = encrypt(text, passphrase)
    save_encrypted_data("encrypted_data.diec", salt, iv, tag, encrypted_data)
    print("Encryption successful. Encrypted data saved to 'encrypted_data.diec'.")

if __name__ == "__main__":
    encode_exp()