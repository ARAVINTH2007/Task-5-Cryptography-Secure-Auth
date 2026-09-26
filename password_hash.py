"""bcrypt password hashing demo."""

import bcrypt

WORK_FACTOR = 12


def hash_password(password: str) -> str:
    if not password:
        raise ValueError("Password must not be empty")

    hashed = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt(rounds=WORK_FACTOR)
    )

    return hashed.decode("utf-8")


def verify_password(password: str, stored_hash: str) -> bool:
    return bcrypt.checkpw(
        password.encode("utf-8"),
        stored_hash.encode("utf-8")
    )


if __name__ == "__main__":

    password = "Example-only-password"

    stored_hash = hash_password(password)

    print("bcrypt password hashing demo")
    print("Stored hash:", stored_hash)

    print(
        "Correct password:",
        verify_password(password, stored_hash)
    )

    print(
        "Wrong password:",
        verify_password("Wrong-password", stored_hash)
    )
  
