import base64
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

#Read public key of recipient
with open('MyPublicKey.pem', 'rb') as public_file:
    key_data = public_file.read()
    public_key = serialization.load_pem_public_key(key_data)

    with open('MyMessageFile', 'rb') as message_file:
        message = message_file.read()
        message_file.close()

        ciphertext_bytes = public_key.encrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        
        with open("MyCipherText.txt", "wb") as binary_file:
            # Write bytes to file
            encoded_text = base64.b64encode(ciphertext_bytes)
            binary_file.write(encoded_text)
            binary_file.close()




