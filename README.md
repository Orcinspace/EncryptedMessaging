# EncryptedMessaging
Test project to illustrate how encrypted messaging might look

1. Generate public/private key pair by any method you trust. A simple generator is included, which outputs as .pem files
2. Write some short message in "MyMessageFile". This could in principle also be some image or video file
3. To encrypted a message to send to someone, run running EncryptMessage.py using the public key of the intended recipient
4. To decrypt a received message, run DecryptMessage.py using your own private key.