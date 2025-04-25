# Final-Exam_rKakhishvili_Task-2
Secure File Exchange Using RSA + AES


Secure File Exchange Using RSA + AES Alice creates file containing sensitive information named alice_message.txt. Generates AES-256 key and IV and enrypts the file named encrypted_file.bin with the IV prepended to the ciphertext. Bob’s public RSA key named public.pem is used to encrypt the AES key with OAEP padding and SHA-256 hash and saved as aes_key_encrypted.bin. Then Bob uses his private key named private.pem and decrypts the key from file aes_key_encrypted.bin. Bob retrieves the IV and ciphertext from encrypted_file.bin, decrypts them with the obtained AES key, and saves the results as decrypted_message.txt. AES-256 uses same key for encryption and decryptoion, is fast and can encrypt large data and is very secure when proper key is used. RSA usis private and public keys, is a slower then AES-256 and is generally used for small amount of data encryption, is also very secure.
