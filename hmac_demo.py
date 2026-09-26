"""HMAC-SHA-256 demonstration."""

import hmac
import hashlib
import secrets


def create_hmac(key: bytes, message: bytes) -> bytes:
    return hmac.new(
        key,
        message,
        hashlib.sha256
    ).digest()


def verify_hmac(
    key: bytes,
    message: bytes,
    tag: bytes
) -> bool:

    expected = create_hmac(key, message)

    return hmac.compare_digest(
        expected,
        tag
    )


if __name__ == "__main__":

    key = secrets.token_bytes(32)

    message = b"Authenticated message"

    tag = create_hmac(
        key,
        message
    )

    print("HMAC-SHA-256 demo")

    print(
        "Valid:",
        verify_hmac(key, message, tag)
    )

    print(
        "Tampered:",
        verify_hmac(
            key,
            b"Tampered message",
            tag
        )
    )
