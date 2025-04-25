# Step 1: Generate RSA Key Pair for Bob

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Bob's private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Save private key
with open("private.pem", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))

# Save public key
public_key = private_key.public_key()
with open("public.pem", "wb") as f:
    f.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))

print("✔️ RSA keys for Bob generated: private.pem, public.pem")
