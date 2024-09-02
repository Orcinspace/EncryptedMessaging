# EncryptedMessaging
Test project to illustrate how encrypted messaging might look

1. Generate public/private key pair by any method you trust. A simple generator is included, which outputs as .pem files. 
    Save your private key
    Give your public key to anyone you want to be able to receive encrypted messages from
2. Write some short text message in "MyMessageFile". 
3. To encrypted a message to send to someone, run running EncryptMessage.py using the public key of the intended recipient
4. To decrypt a received message, run DecryptMessage.py using your own private key.


Possible future extensions:
Write own RSA key generator implementation
Write own encryption and decryption implementations
Allow encryption of larger files (images, video ect.) by chunking