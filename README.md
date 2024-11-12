
<div align="center">
  
# diec

[![License](https://img.shields.io/badge/License-MIT-blue)](https://github.com/Eldritchyl/diec#license)  [![PyPi](https://img.shields.io/badge/PyPi%20Link-FFFF00)](https://pypi.org/project/diec/)  <a href="https://github.com/D-I-Projects/diec/blob/master/CONTRIBUTING.md"> <img src="https://img.shields.io/github/contributors-anon/D-I-Projects/diec" alt="Contributors badge" /></a>  [![Downloads](https://static.pepy.tech/badge/diec)](https://pepy.tech/project/diec)

```pip install diec``` 

</div>

A tool for encoding and decoding text with a passphrase. Encrypt text into a secure format and decrypt it later using the same key.

Official test UI: [diec-test-gui](https://github.com/Eldritchyl/diec-test-gui)

## Installation

```bash
pip install diec
```

## Usage

### Encrypt Text

To encode text, use the `encode-text` command:

```bash
python cli.py encode-text "This is the text to encode" --passphrase "your_passphrase"
```

This will encrypt the provided text using the given passphrase.

### Decrypt Text

To decode previously encrypted text, use the `decode-text` command:

```bash
python cli.py decode-text --passphrase "your_passphrase"
```

This will decrypt the text and print the original message, using the same passphrase used during encryption.

## CLI Commands

### `encode-text`

Encodes the provided text with a passphrase.

```bash
python cli.py encode-text <text> --passphrase <passphrase>
```

### `decode-text`

Decodes the previously encoded text using the provided passphrase.

```bash
python cli.py decode-text --passphrase <passphrase>
```

## License

MIT License. See [LICENSE](LICENSE) for details.

---

Author: **Eldritchy**  
Email: [eldritchy.help@gmail.com](mailto:eldritchy.help@gmail.com)  
GitHub: [https://github.com/Eldritchyl](https://github.com/Eldritchyl)