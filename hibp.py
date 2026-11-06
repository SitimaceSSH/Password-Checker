import hashlib
import requests


def get_hash(password):
    password_bytes = password.encode()
    sha1_hash = hashlib.sha1(password_bytes)
    encoded_password = sha1_hash.hexdigest()
    encoded_password = encoded_password.upper()
    return encoded_password


def count_leaks(prefix, suffix):
    response = requests.get(f'https://api.pwnedpasswords.com/range/{prefix}', timeout=5)
    response.raise_for_status()
    lines = response.text.splitlines()
    for line in lines:
        parts = line.split(':')
        if parts[0] == suffix:
            return int(parts[1])
    return 0
