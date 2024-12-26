import click
from encrypt import encrypt, save_encrypted_data
from decrypt import decrypt, read_encrypted_data

@click.group()
def cli():
    pass

@cli.command("encode")
@click.argument("text", type=str)
@click.option(
    "--passphrase", prompt=True, hide_input=True, confirmation_prompt=True, 
    help="Passphrase used for encryption."
)
@click.option(
    "--output", default="encrypted_data.diec", show_default=True, 
    help="File path to save the encrypted data."
)
def encode_text(text, passphrase, output):
    try:
        salt, iv, tag, encrypted_data = encrypt(text, passphrase)
        save_encrypted_data(output, salt, iv, tag, encrypted_data)
        click.echo(f"Encryption successful! Encrypted data saved to '{output}'.")
    except Exception as e:
        click.secho(f"Error during encryption: {e}", fg="red")

@cli.command("decode")
@click.option(
    "--passphrase", prompt=True, hide_input=True, help="Passphrase used for decryption."
)
@click.option(
    "--input", default="encrypted_data.diec", show_default=True, 
    help="File path of the encrypted data to be decrypted."
)
def decode_text(passphrase, input):
    try:
        salt, iv, tag, encrypted_data = read_encrypted_data(input)
        decrypted_text = decrypt(encrypted_data, passphrase, salt, iv, tag)
        click.secho("Decryption successful!", fg="green")
        click.echo(f"Decoded text: {decrypted_text}")
    except FileNotFoundError:
        click.secho(f"Error: File '{input}' not found.", fg="red")
    except Exception as e:
        click.secho(f"Error during decryption: {e}", fg="red")

def main():
    cli()

if __name__ == "__main__":
    main()
