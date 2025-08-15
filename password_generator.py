#!/usr/bin/env python3
"""
password_generator.py — Generate secure passwords.
Usage:
  python3 password_generator.py                # 16-char default
  python3 password_generator.py 24 5           # 5 passwords of length 24
"""
import sys, secrets, string

ALPHABET = string.ascii_letters + string.digits + string.punctuation

def gen_password(length=16):
    return "".join(secrets.choice(ALPHABET) for _ in range(length))

def main():
    if len(sys.argv) == 1:
        print(gen_password())
    elif len(sys.argv) == 3:
        length = int(sys.argv[1])
        count  = int(sys.argv[2])
        for _ in range(count):
            print(gen_password(length))
    else:
        print("Usage: python3 password_generator.py [length count]")
        sys.exit(1)

if __name__ == "__main__":
    main()
