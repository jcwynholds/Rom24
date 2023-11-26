#!/usr/bin/env python3

import crypt
import sys

def main():
    name = sys.argv[1]
    password = sys.argv[2]
    crypt_str = crypt.crypt(word=password, salt=name)
    print(f"name {name} password {password} crypt_str {crypt_str}")

if __name__ == "__main__":
    main()
