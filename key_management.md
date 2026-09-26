# Secure Secret & Key Management

## 1. Secure Storage Best Practices

- Never hard-code production secrets or private keys in source code.
- Never commit passwords, API keys, tokens, or private keys to GitHub.
- Store secrets outside the Git repository.
- Use a dedicated Secret Manager or Key Management Service (KMS) when available.
- Use least-privilege access controls.
- Keep development, testing, and production secrets separate.
- Protect private keys using secure operating-system permissions or managed key storage.
- Never print passwords, private keys, API tokens, or encryption keys in application logs.

## 2. Key Rotation

A secure key-rotation process should include:

1. Define an appropriate key lifetime based on the application's security requirements.
2. Generate a new cryptographically secure key.
3. Store the new key securely.
4. Maintain key versions when required.
5. Re-encrypt data with the new key where appropriate.
6. Deploy and test the new key.
7. Revoke or retire the old key after migration.
8. Record key-rotation events for auditing.

## 3. Algorithm Guidance

### AES-256-GCM

AES-256-GCM provides authenticated encryption, giving both confidentiality and integrity.

A unique random nonce must be used for every encryption operation with the same AES-GCM key.

### RSA-2048

RSA-2048 can be used for this educational digital-signature exercise.

RSA-PSS with SHA-256 is used for signatures.

The RSA private key must remain secret, while the public key can be shared.

### HMAC-SHA-256

HMAC-SHA-256 provides message authentication and integrity using a secret key.

The HMAC key should be randomly generated and stored securely.

### bcrypt

bcrypt is designed for password hashing.

It automatically uses a salt and supports a configurable work factor.

Passwords should be hashed rather than encrypted.

## 4. Incident Response

If a secret or private key is exposed:

1. Treat the credential as compromised.
2. Revoke or rotate the affected credential.
3. Investigate possible unauthorized access.
4. Review relevant logs.
5. Replace affected secrets.
6. Restore from trusted backups if necessary.
7. Document the incident and corrective actions.

## 5. Git Security

The repository must not contain:

- Real passwords
- Private RSA keys
- API keys
- Access tokens
- `.env` files containing secrets
- Production encryption keys

Use `.gitignore` to prevent accidental commits of sensitive files.
