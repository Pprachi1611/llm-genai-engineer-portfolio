import secrets
import string

length = int(input("Enter password length: "))

if length < 4:
    print("Password length should be at least 4")
else:
    password = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation),
    ]

    all_chars = string.ascii_letters + string.digits + string.punctuation

    password += [secrets.choice(all_chars) for _ in range(length - 4)]

    secrets.SystemRandom().shuffle(password)

    print("Generated Password:", "".join(password))