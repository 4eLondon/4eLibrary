#!/usr/bin/env python3
import ast

"""
 - - - Reading the private key - - -

 We read d and n back from the key file the encoder created.
 These two values are our private key and are all we need to decrypt.

 We dont need p, q, phi_n or e anymore. Those were only needed
 to generate d in the first place. Once we have d we are done with them.

 split(",") separates d and n on the comma we saved them with.
 map(int, ...) converts both from text back into numbers so we can do math.
"""

with open("key.txt", "r") as f:
    d, n = map(int, f.read().split(","))

"""
 - - - Reading the encrypted message - - -

 ast.literal_eval() reads the list of numbers back out of the text file
 as an actual Python list. Without it you'd just have a string that looks
 like a list but cant be looped over.
"""

with open("encryted.txt", "r") as f:
    encrypt = ast.literal_eval(f.read())

"""
 - - - Decryption - - -

 The reverse of encryption. Each encrypted number c gets raised to the
 power of d with n as the remainder. That hands us back m, the original
 ASCII number. chr() then converts that back into a readable character.

 FORMULA -> m = c^d mod n
"""

decrypt = []
for c in encrypt:
    m = pow(c, d, n)        # reverse the encryption math
    decrypt.append(chr(m))  # convert ascii number back to character

print("".join(decrypt))
