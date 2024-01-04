# Porridge Password Storage and Verification

This Python script, "porridge-store_verify.py", provides a simple command-line interface for storing and verifying passwords using the Porridge library.

## Usage

### Storing a Password

To store a password, use the following command:

```bash
python porridge-store_verify.py store [password] [key] [secret]
```
- [password]: Password to be stored.
- [key]: Key for the password.
- [secret]: Secret for the password.

# Verifying a Stored Password
To verify a stored password, use the following command:

```bash
python porridge-store_verify.py verify [password] [key] [secret]
```
- [password]: Password to be verified.
- [key]: Key for the stored password.
- [secret]: Secret for the stored password.

# Example
## Storing a Password
```bash
python porridge-store_verify.py store mypassword mykey mysecret
```
## Verifying a Stored Password
```bash
python porridge-store_verify.py verify mypassword mykey mysecret
```
# Dependencies
Porridge: The Porridge library for password storage and verification.
```bash
pip install porridge
```
# Notes
The stored passwords are saved in the "pseudo_db.file" file.
Make sure to handle the "pseudo_db.file" file securely to prevent unauthorized access.
