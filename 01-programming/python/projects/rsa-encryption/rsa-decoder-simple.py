#!/usr/bin/env python3
import ast

# read private key
with open("key.txt", "r") as f:
    d, n = map(int, f.read().split(","))

# read encrypted message
with open("encryted.txt", "r") as f:
    encrypt = ast.literal_eval(f.read())

# decrypt
decrypt = []
for c in encrypt:
    m = pow(c, d, n)
    decrypt.append(chr(m))

print("".join(decrypt))
