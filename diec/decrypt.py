from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def generate_key(passphrase, salt):
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,
        salt=salt,
        iterations=100_000,
        backend=default_backend()
    )
    return kdf.derive(passphrase.encode())

def read_encrypted_data(file_name):
    with open(file_name, 'rb') as file:
        data = file.read()
    salt = data[:16]
    iv = data[16:28]
    tag = data[28:44]
    encrypted_data = data[44:]
    return salt, iv, tag, encrypted_data

def decrypt(encrypted_data, passphrase, salt, iv, tag):
    key = generate_key(passphrase, salt)
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    return decrypted_data.decode()

def decode_exp():
    passphrase = "my_secure_passphrase"
    salt, iv, tag, encrypted_data = read_encrypted_data("encrypted_data.diec")
    decrypted_text = decrypt(encrypted_data, passphrase, salt, iv, tag)
    return decrypted_text

if __name__ == "__main__":
    decrypted_text = decode_exp()
    print("Decryption successful. Decrypted text:")
    print(decrypted_text)
