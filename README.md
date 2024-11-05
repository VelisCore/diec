<div align="center">
  
# diec

[![License](https://img.shields.io/badge/License-MIT-blue)](https://github.com/Eldritchyl/diec#license)  [![PyPi](https://img.shields.io/badge/PyPi%20Link-FFFF00)](https://pypi.org/project/diec/)  <a href="https://github.com/D-I-Projects/diec/blob/master/CONTRIBUTING.md"> <img src="https://img.shields.io/github/contributors-anon/D-I-Projects/diec" alt="Contributors badge" /></a>  [![Downloads](https://static.pepy.tech/badge/diec)](https://pepy.tech/project/diec)

```pip install diec``` 

</div>

A tool that encodes text and gives out a key that you can decode with this program too!

Our official test UI : [diec-test-gui](https://github.com/Eldritchyl/diec-test-gui)

## Installation

```bash
pip install diec
```

# Example

<hr>

## encode()

```python
from diec.encoder import encode

encode("I love python and I love to learn new things here too! <3")
```
### Output

The Key you created : <a href="https://github.com/Eldritchyl/diec/blob/main/diec_example/key.diec">key.diec</a>

The encoded text : <a href="https://github.com/Eldritchyl/diec/blob/main/diec_example/encoded.diec">encoded.diec</a>

**Both of them will appear in your current directory**

<hr>

## decode()

```python
from diec.decoder import decode

decode() # The key.diec and encoded.diec files have to be in the same directory as the file that runs this command.
```
### Output
```bash
I love python and I love to learn new things here too! <3
```
<hr>

## CLI Tutorial

The Diec CLI (Command Line Interface) allows you to easily encode and decode text via the terminal.

### Installation

Make sure Diec is installed:

```bash
pip install diec
```

### Using the CLI

After installation, you can use the following commands:

1. **Encode Text**:

   To encode a text, use the `encode_cli` command. Provide the desired text in quotes:

   ```bash
   python -m diec encode-cli "Your text here"
   ```

   **Example**:

   ```bash
   python -m diec encode-cli "I love Python and learning new things! <3"
   ```

   After running this command, a key file (`key.diec`) and an encoded file (`encoded.diec`) will be created in your current directory.

2. **Decode Text**:

   To decode an encoded text, use the `decode_cli` command:

   ```bash
   python -m diec decode-cli
   ```

   Make sure that the `key.diec` and `encoded.diec` files are in the same directory as the script you run.

---
