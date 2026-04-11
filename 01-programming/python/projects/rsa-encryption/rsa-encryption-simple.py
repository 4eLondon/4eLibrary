##!/usr/bin/env python3
from sympy import randprime
import math

# Selecting primes
p = None
q = None

while q is None:
    result = randprime(1000, 9999) # assign random prime number
    assert result is not None # ensure veriable is not None for math to work
    q = int(result) # convert to int
    pass

while p is None:
    result = randprime(1000, 9999)
    assert result is not None
    p = int(result)
    pass

# Variable N
n = p * q

# Compute Euler's Totient (φ)
phi_n = ( q-1) * (p-1)

# Public exponent
e = 65537 # 65537 because its a well used and trusted for RSA making it the default it is also prim itself
assert math.gcd(e, phi_n) == 1, "Error - variable e shares factors with phi(n)" # ensures phi_n doesnt share factors with e for decryption to work later

# Private exponent
d = pow(e, -1, phi_n) # inverse of e

# Encode message
print("Enter your message (Ctrl+C to finish):")
lines = []
try:
    while True:
        lines.append(input())
except KeyboardInterrupt:
    pass

message = "\n".join(lines)

encrypt = [] # empty array to store encryted message later

for letter in message: # repeat for every character and space
    m = ord(letter) # convert character to ascii numbers
    c = pow(m, e, n) # m to the power of e divided by remaineder
    encrypt.append(c) # add encryted letters to the array

with open("key.txt", "w") as f: # create new file/ overwrite existing file
    print(f"{d},{n}", file=f) # write data to file

with open("encryted.txt", "w") as f:
    print(f"{encrypt}", file=f)

