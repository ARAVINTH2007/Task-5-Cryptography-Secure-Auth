"""AES-256-GCM authenticated encryption demo."""

import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

KEY_SIZE = 32    # 256 bits
NONCE_SIZE = 12  # 96 bits, recommended for GCM


def generate_key() -> bytes:
    return AESGCM.generate_key(bit_length=256)


def encrypt(
    key: bytes,
    plaintext: bytes,
    associated_data: bytes | None = None
) -> tuple[bytes, bytes]:

    if len(key) != KEY_SIZE:
        raise ValueError("AES-256 requires a 32-byte key")

    nonce = os.urandom(NONCE_SIZE)

    ciphertext = AESGCM(key).encrypt(
        nonce,
        plaintext,
        associated_data
    )

    return nonce, ciphertext


def decrypt(
    key: bytes,
    nonce: bytes,
    ciphertext: bytes,
    associated_data: bytes | None = None
) -> bytes:

    if len(key) != KEY_SIZE:
        raise ValueError("AES-256 requires a 32-byte key")

    return AESGCM(key).decrypt(
        nonce,
        ciphertext,
        associated_data
    )


if __name__ == "__main__":

    key = generate_key()

    nonce, ciphertext = encrypt(
        key,
        b"Rabtech Task 5 - secret message"
    )

    recovered = decrypt(
        key,
        nonce,
        ciphertext
    )

    print("AES-256-GCM demo")
    print("Random nonce:", nonce.hex())
    print("Ciphertext:", ciphertext.hex())
    print("Decrypted:", recovered.decode())
