## RSA Encryption

## Setup

You will need Python and one package. Install it with:

```
pip install sympy
```

Then run the encoder:

```
python rsa-encryption-simple.py
```

And the decoder:

```
python rsa-decryption-simple.py
```

The encoder will produce two files:
- `encrypted.txt` — the encrypted message
- `key.txt` — your private key, used to decrypt

---

## What is RSA

RSA is a way of encrypting a message so that only the intended person can read it.

It works by using two keys — a public key and a private key. They are a mathematically linked pair. What one locks, only the other can unlock.

- The **public key** is shared openly. Anyone can use it to encrypt a message to you.
- The **private key** is kept secret. Only you have it and only it can decrypt messages sent to you.

The reason this works is that the keys are built from two large prime numbers. Finding those original prime numbers from the public key alone is computationally hard — it would take an impractical amount of time even for modern computers when the primes are large enough.

---

## How the keys are built

Two random prime numbers are chosen, called `p` and `q`.

They are multiplied together to make `n`. This is public.

```
n = p * q
```

From `p` and `q` we calculate `phi_n`:

```
phi_n = (p - 1) * (q - 1)
```

This number links the two keys together and is kept private.

The public exponent `e` is set to `65537`. This is a well trusted standard choice for RSA. Together `e` and `n` form the **public key**.

```
public key = (e, n)
```

The private exponent `d` is the mathematical inverse of `e`. Together `d` and `n` form the **private key**.

```
private key = (d, n)
```

---

## Encryption

Each character in the message is converted to its ASCII number. That number is then run through this formula:

```
c = m^e mod n
```

Where `m` is the ASCII number of the character, `e` is the public exponent, `n` is our big number, and `c` is the resulting encrypted number. The `mod` just means take the remainder after division.

The result is a list of numbers that looks nothing like the original message.

---

## Decryption

Each encrypted number is run through the reverse formula using the private key:

```
m = c^d mod n
```

This hands back the original ASCII number. That number is then converted back to a character. Do that for every number in the list and you have the original message back.

---

## Why it is secure

Anyone can see `n` and `e`. But to decrypt they would need `d`. To get `d` they would need `phi_n`. To get `phi_n` they would need `p` and `q`. And to get `p` and `q` they would need to factor `n` back into its two original primes — which for large enough primes is effectively impossible in a reasonable amount of time.

That gap between what is easy to do and what is hard to undo is what makes RSA work. RSA Encryption
