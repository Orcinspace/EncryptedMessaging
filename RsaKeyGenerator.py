from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend

key = rsa.generate_private_key(
    backend=crypto_default_backend(),
    public_exponent=65537,
    key_size=2048
)

private_key = key.private_bytes(
    encoding= serialization.Encoding.PEM,
    format= serialization.PrivateFormat.PKCS8,
    encryption_algorithm = serialization.NoEncryption()
    #encryption_algorithm = crypto_serialization.BestAvailableEncryption(b'mypassword')
)

private_key_file = open("MyPrivateKey.pem", "x")
private_key_file.write(private_key.decode("utf-8"))


public_key = key.public_key().public_bytes(
    encoding = serialization.Encoding.PEM,
    format = serialization.PublicFormat.SubjectPublicKeyInfo
)

public_key_file = open("MyPublicKey.pem", "x")
public_key_file.write(public_key.decode("utf-8"))