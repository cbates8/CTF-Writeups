## Challenge: Semihonest
## Category: Crypto

### Prompt:
> OT is secure I hope you will not break it Don't be malicious
> Remote running at chals.damctf.xyz 30332

[semihonestclient.py](https://github.com/cbates8/CTF-Writeups/blob/main/damCTF%202020/Crypto%20-%20Semihonest/ORIGINAL_semihonestclient.py)

### Solution:
The given Python script implemented a Diffie-Hellman key exchange and one-time pad decryption.

My code to generate Diffie-Hellman keys:

```python
# TODO: Generate Diffie-Hellman keys
def gen_key(g, p, B):
    a = random.randint(1, p-1)
    A = pow(g, a, p)
    KA = pow(B, a, p)
    return (KA, A)

```

My code to decrypt using one-time pad:

```python
# TODO: Decrypt multiplication one-time pad
def otp_decrypt(key, p, ctext):
    k = key % p
    keyInverse = invert(key, p) #Using invert() from gmpy2 to find modular inverse
    return (ctext * keyInverse) % p
```

Afer XORing the two ciphertexts output by the server, I got the flag `dam{w0w_1_gues5_h0n3sty_15nt_1mp0rt4nT_T0_y0u}`

### Flag:
dam{w0w_1_gues5_h0n3sty_15nt_1mp0rt4nT_T0_y0u}
