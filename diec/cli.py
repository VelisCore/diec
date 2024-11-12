import click
from encrypt import encrypt
from decrypt import decrypt

@click.group()
def cli():
    pass

@cli.command()
@click.argument('text', type=str)
@click.option('--passphrase', prompt=True, help="Passphrase used for encoding.")
def encode_text(text, passphrase):
    print(f"Encoding text: {text}")
    encrypt(text, passphrase)

@cli.command()
@click.option('--passphrase', prompt=True, help="Passphrase used for decoding.")
def decode_text(passphrase):
    decoded_text = decrypt(passphrase) 
    print(f"Decoded text: {decoded_text}")

cli.add_command(encode_text)
cli.add_command(decode_text)

if __name__ == "__main__":
    cli()
