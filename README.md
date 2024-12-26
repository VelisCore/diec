
<div align="center">
  
# diec

[![License](https://img.shields.io/badge/License-MIT-blue)](https://github.com/VelisCore/diec#license)  [![PyPi](https://img.shields.io/badge/PyPi%20Link-FFFF00)](https://pypi.org/project/diec/)  <a href="https://github.com/VelisCore/diec/blob/master/CONTRIBUTING.md"> <img src="https://img.shields.io/github/contributors-anon/VelisCore/diec" alt="Contributors badge" /></a>  [![Downloads](https://static.pepy.tech/badge/diec)](https://pepy.tech/project/diec)

```bash
pip install diec
``` 

</div>

**diec** is a powerful and user-friendly command-line tool for securely encrypting and decrypting text using AES-GCM encryption. Store sensitive information in a secure format and retrieve it when needed using a passphrase.

---

## Installation

Install **diec** via pip:

```bash
pip install diec
```

---

## Features

- **Secure Encryption**: Uses AES-GCM with a passphrase-derived key for secure data encryption.
- **Simple Decryption**: Easily decrypt your data with the same passphrase.
- **Customizable**: Save and load encrypted files with customizable file paths.

---

## Usage

Run the CLI tool via Python:

```bash
python cli.py [COMMAND] [OPTIONS]
```

### 1. Encrypt Text (`encode` command)

Encrypt your text with a passphrase and save it to a file:

```bash
python cli.py encode "Your sensitive text here" --passphrase "your_secure_passphrase" --output "output_file.diec"
```

- **Arguments**:
  - `text`: The text to encrypt (required).
- **Options**:
  - `--passphrase`: Passphrase to secure your data (required; hidden input).
  - `--output`: File path to save the encrypted data (default: `encrypted_data.diec`).

---

### 2. Decrypt Text (`decode` command)

Decrypt your previously encrypted file with a passphrase:

```bash
python cli.py decode --passphrase "your_secure_passphrase" --input "output_file.diec"
```

- **Options**:
  - `--passphrase`: Passphrase used during encryption (required; hidden input).
  - `--input`: File path to the encrypted data (default: `encrypted_data.diec`).

---

## License

MIT License. See [LICENSE](LICENSE) for details.

---

Author: **Eldritchy**  
Email: [eldritchy.help@gmail.com](mailto:eldritchy.help@gmail.com)  
GitHub: [https://github.com/Eldritchyl](https://github.com/VelisCore)