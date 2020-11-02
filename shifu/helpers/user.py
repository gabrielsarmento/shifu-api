from bcrypt import hashpw, gensalt


def encrypt_password(user: dict) -> dict:
    password = user.pop('password')
    hash_password = hashpw(password.encode(), gensalt()).decode()
    user['password'] = hash_password
    return user
