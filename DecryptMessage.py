import base64
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

#Read own private key
with open('MyPrivateKey.pem', 'rb') as private_file:
    key_data = private_file.read()
    private_key = serialization.load_pem_private_key(key_data, password=None)

    with open('MyCipherText.txt', 'rb') as ciphertext_file:
        read_bytes = ciphertext_file.read()
        decoded_bytes = base64.b64decode(read_bytes)

        plaintext = private_key.decrypt(
            decoded_bytes,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )