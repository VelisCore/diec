
<div align="center">

# **diec** 🔐

[![License](https://img.shields.io/badge/License-MIT-blue)](https://github.com/VelisCore/diec#license)  
[![PyPi](https://img.shields.io/badge/PyPi%20Link-FFFF00)](https://pypi.org/project/diec/)  
[![Contributors](https://img.shields.io/github/contributors-anon/VelisCore/diec)](https://github.com/VelisCore/diec/graphs/contributors)  
[![Downloads](https://static.pepy.tech/badge/diec)](https://pepy.tech/project/diec)

**Encrypt and decrypt text securely with your own passphrase.**

An easy-to-use command-line tool for encoding and decoding sensitive data. Securely encrypt your messages into unreadable formats, then decrypt them using the same key.

**Official test UI:**  
[diec-test-gui](https://github.com/VelisCore/diec-test-gui)

</div>

---

## **📥 Installation**

To install **diec**, you can use `pip`:

```bash
pip install diec
```

This will install the latest stable version of **diec**. Ensure that you have Python 3.9 or higher installed.

**Dependencies**:
- **argon2**: For passphrase hashing and key derivation.
- **binaryconvert**: For binary conversion utilities.

If you're using a virtual environment (recommended), make sure to activate it before running the `pip install` command.

---

## **🔐 Secure Your Data with diec**

### **How diec Works**

The **diec** tool is designed to encrypt and decrypt text using a passphrase. When you encrypt text, **diec** converts it into an unreadable format. Later, you can use the same passphrase to decrypt it back into its original form. This makes **diec** a perfect solution for encrypting sensitive information that needs to be shared or stored securely.

### **Encrypt Text**

Encrypt your plain text with a passphrase to ensure it is safely stored or shared.

```bash
python -m diec encode "This is the text to encode" --passphrase "your_passphrase"
```

**Command Options**:
- **`text`**: The plaintext message you want to encrypt.
- **`--passphrase`**: The secret passphrase used for encryption (you will be prompted for this if not provided directly).
- **`--output`**: (Optional) Specify the output file to save the encrypted data. By default, the encrypted data will be stored in a file named `encrypted_data.diec`.

Once encrypted, the file will contain the salted, IV-based, and encrypted data in a secure format.

### **Decrypt Text**

To decrypt an encrypted file, simply use the same passphrase that was used during the encryption process.

```bash
python -m diec decode --passphrase "your_passphrase"
```

**Command Options**:
- **`--passphrase`**: The passphrase used to decrypt the data.
- **`--input`**: (Optional) Specify the input file that contains the encrypted data. By default, it looks for `encrypted_data.diec`.

### **Encryption and Decryption Flow**

1. **Encryption**: 
   - A salt is randomly generated and combined with the passphrase to create a secure key using **PBKDF2**.
   - The text is encrypted with **AES-GCM** mode to ensure confidentiality, integrity, and authenticity.
   - The encrypted data, along with the salt and initialization vector (IV), is saved to the specified file.

2. **Decryption**:
   - The encrypted file is read, and the salt and IV are extracted.
   - The passphrase is used to regenerate the cryptographic key using **PBKDF2**.
   - The encrypted text is then decrypted, and the original message is recovered.

---

## **⚙️ Command Line Usage**

The **diec** command-line interface (CLI) provides two main commands for encoding and decoding:

### **`encode`**: Encrypt Text

This command is used to encrypt the provided text.

```bash
python -m diec encode <text> --passphrase <passphrase> --output <output_file>
```

**Parameters**:
- **`<text>`**: The plaintext message you want to encrypt.
- **`<passphrase>`**: The passphrase used to secure the data.
- **`--output`**: (Optional) Specify the output file to save the encrypted data. Defaults to `encrypted_data.diec`.

Example:
```bash
python -m diec encode "Sensitive information here" --passphrase "your_secret_passphrase" --output "encrypted_message.diec"
```

### **`decode`**: Decrypt Text

Use this command to decrypt the previously encrypted file.

```bash
python -m diec decode --passphrase <passphrase> --input <input_file>
```

**Parameters**:
- **`<passphrase>`**: The passphrase used to decrypt the data.
- **`--input`**: (Optional) Specify the file that contains the encrypted data. Defaults to `encrypted_data.diec`.

Example:
```bash
python -m diec decode --passphrase "your_secret_passphrase" --input "encrypted_message.diec"
```

---

## **💡 Key Features**

- **Strong Encryption**: Uses modern cryptography (AES-GCM and PBKDF2) for secure and reliable data protection.
- **No Dependencies on External Services**: Everything happens locally on your machine.
- **Customizable Output**: You can choose where to save the encrypted files, ensuring flexibility in storage.
- **Cross-Platform Compatibility**: Works seamlessly across Linux, macOS, and Windows.
- **Interactive Passphrase Prompt**: For added security, the passphrase is entered interactively to avoid hardcoding.
- **Decryption Guarantee**: The decryption process ensures that the original data can always be recovered with the correct passphrase.

---

## **📖 Example Use Cases**

### **Use Case 1: Encrypting and Sharing Sensitive Information**

Imagine you need to send sensitive information, like a password or secret key, to someone securely. With **diec**, you can encrypt the information into a file, and share the file along with the passphrase securely (e.g., via another communication channel). The recipient can use **diec** to decrypt the information using the same passphrase.

### **Use Case 2: Storing Sensitive Data Safely**

If you need to store sensitive data locally (such as API keys, passwords, etc.), **diec** allows you to encrypt the data before saving it to a file. This ensures that even if the file is compromised, the data remains protected as long as the passphrase is kept secure.

---

## **📅 Release Notes**

### **v3.2**

- **Added passphrase confirmation**: To ensure users don’t accidentally enter incorrect passphrases during encryption and decryption.
- **Improved error handling**: Enhanced error messages to make it easier to identify issues during encryption/decryption.
- **CLI usability improvements**: More clear prompts and options, better documentation.

---

## **🔒 License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## **👨‍💻 Author**

**Eldritchy**  
[GitHub: @Eldritchyl](https://github.com/Eldritchyl)  
[Email: eldrity.help@gmail.com](mailto:eldritchy.help@gmail.com)

---

## **📦 Installation Requirements**

- **Python 3.9** or higher
- **argon2**: For secure password hashing and key derivation.
- **binaryconvert**: For binary conversion utilities.
