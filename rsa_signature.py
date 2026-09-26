"""RSA-2048 key generation and digital signature verification demo."""

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa


def generate_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    public_key = private_key.public_key()

    return private_key, public_key


def sign(private_key, message: bytes) -> bytes:
    return private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )


def verify(public_key, message: bytes, signature: bytes) -> bool:
    try:
        public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        return True

    except Exception:
        return False


if __name__ == "__main__":

    private_key, public_key = generate_key_pair()

    message = b"Rabtech Task 5 signed message"

    signature = sign(private_key, message)

    print("RSA-2048 signature demo")
    print("Signature valid:", verify(public_key, message, signature))

    print(
        "Tampered message valid:",
        verify(public_key, b"Tampered message", signature)
    )

    # Demonstration of PEM serialization.
    private_pem = private_key.private_bytes(
        serialization.Encoding.PEM,
        serialization.PrivateFormat.PKCS8,
        serialization.NoEncryption()
    )

    public_pem = public_key.public_bytes(
        serialization.Encoding.PEM,
        serialization.PublicFormat.SubjectPublicKeyInfo
    )

    print("Private key generated:", len(private_pem), "bytes")
    print("Public key generated:", len(public_pem), "bytes")
