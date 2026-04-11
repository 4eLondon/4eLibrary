#!/usr/bin/env python3
from sympy import randprime
import math

# ------------------------------------------------------ #
#                      Used items                        #
# ------------------------------------------------------ #
"""
 randprime - this comes from the sympy package and simply assigns a randomprime number. Install sympt via `pip install sympy`

 assert - ensures a statement is true else the program exits with an error

 math.gcd(num1,num2) - calculates the greatest common divisor between numbers

 ord(character) - this function is used to conver indiviual letters in their ascii/numerical values. Letter 'a' becomes '97' becomes in ascii '97' represents a common 'a'.

 pow(base, exponent, modulus) - this function calculates a our base to the power of our exponent eg. 6^4 or 6x6x6x6. The modulus value is optional and simply takes the remaineder of the first part and divides it by itself. mod is short for modulus same as remaineder, all are the same thing.

 append - adds data to a list

"""


# ------------------------------------------------------ #
#                      Code                       #
# ------------------------------------------------------ #
"""
 - - - Choose Two prime numbers - - -

 We begin by establising our prime numbers, these numbers are the building blocks of rsa encrytion.
 Large numbers are choosen due to the fact reverse enginnering them often offers the wrong outcomes.

 In the example below we randomly set a prime number at program runtime in the range 1000 to 9999. These numbers
 are large enough but the give a good enough margin to work in.

 assert ensures the variable itsnt still none and late those variables are converted to integers so math can be done.

"""
p = None
q = None

while q is None:
    result = randprime(1000, 9999)
    assert result is not None
    q = int(result)
    pass

while p is None:
    result = randprime(1000, 9999)
    assert result is not None
    p = int(result)
    pass

print("")
print(type(p))
print(type(q))
print("")

print(f"p = {p}  q = {q}")

"""
 - - - variable N - - -

 A variable N is equal to both prime numbers multiplied, N exists in both our public and privates to some degree and is visiable or all to see.

 N alone cannot help us figure out what p & q orginally were given that they are super long prime numbers. It is very important our
 prime number variables, p & q are infact looong prime number because if they are small it wont be a challenge to decode. For testing purposes
 we can have small numbers but real RSA relies on those large prime numbers.
"""

n = p * q
print(f"n = {n}")

"""
 - - - Compute Euler's Totient (φ) - - -

 Next we will need to calculate phi(φ) of n which is also know as Euler's Totient function. Euler's Totient states the number of integers in range [1 to n] that are reletively prime to n/share no common factors except 1.

 What this is basicaly saying is that if we pick a random number between 1 and n
 what are the odds that number n shares no factors with it.

 phi_n is the variable that links both private and public keys together and especially plays a key role in our private keys. phi_n is not to be snhared due to its connection with the private key.

 FORMULA -> phi_n = (p-1) * (q-1)

 EXAMPLE
        n = 6
          ->
            let say q = 2 and p = 3
              ->
                our formula states phi_n = (p-1) * (q-1)
                  ->
                    phi_n = (3-1) * (2-1)
                      ->
                        phi_n = (2) * (1)
                          ->
                            phi_n = 2
"""

phi_n = ( q-1) * (p-1)
print(f"phi_n = {phi_n}")


"""
 - - - Public exponent - - -

 Our next step is to create a public exponent variable e. This variable plays a role
 in acturally encrypting our messages.

 e raises the encryted messages to the power of itself.

 e must not share any common factors with the variable phi_n to ensure the
 messgage can acturally be decoded when sent and unlocked by a key.

 variables e and n combine to create our public key that can then be shared.

 the number 65537 is a famous and common choice for our e variable because it is well tested.
 65537 specifically avoids a lot of conflict with a lot of numbers outputted by phi_n.

 we can test if e has any factors with phi_n with a simple gdc function call. If the gdc of e and
 phi_n is equal to 1 then everything is fine else we will have an issue, that being e must absolutley not sure
 factors with phi_n.

 A common factor of 1 technically doesn't count as a real factor and thus 1 is the preferred outcome.
"""

e = 65537
assert math.gcd(e, phi_n) == 1, "Error - variable e shares factors with phi(n)"
print(f"public exponent = {e}")
print(f"public key = {e},{n}")

"""
 - - - Private exponent - - -
 This variable exist as the opposite/inverse to the public exponent. Both are two sides of the same coin, paired. While variable e was used to encrypt, this variable is used to then decrypt our messages. Due to their nature both the private and public variable cancel each other out.

 The private exponent, variable d, alongside variable n combine to create our private key. Never share the private key, only the public one.

 the process of inversing e to get veriable d is simple, we just raise e to the power of -1
"""

d = pow(e, -1, phi_n)
print(f"private exponent = {d}")
print(f"private key = {d},{n}")

"""
 - - - Messages encryption - - -

 Finally we can encode our message.

 first we create an empty array to hold our encryted messgage later.

 This step is done by taking our initial message and seperating it into indiviual letter/characters this is our variable m.
 Next we calculate variable x to the power of our public exponent for each letter, the  remaineder is then divideded by our variable n. This is our variable c.

 we complete this step by simply added each letter to our empty array and write our code into a file so it can be decrypted later.

"""
print("Enter your message (Ctrl+C to finish):")
lines = []
try:
    while True:
        lines.append(input())
except KeyboardInterrupt:
    pass

message = "\n".join(lines)

print (f"Your message was: {message}")

encrypt = []
for letter in message:
    m = ord(letter)
    c = pow(m, e, n)
    encrypt.append(c)

print(f"The encryted version of {message} is {encrypt}")
print(f"Your key is {d},{n} share it to others.")

with open("key.txt", "w") as f:
    print(f"{d},{n}", file=f)

with open("encryted.txt", "w") as f:
    print(f"{encrypt}", file=f)
