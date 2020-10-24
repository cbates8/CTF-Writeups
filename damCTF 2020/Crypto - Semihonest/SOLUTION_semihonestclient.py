#!/usr/bin/env python3

import secrets
import socket
import sys
import random
from gmpy2 import invert


""" Client """

CHUNK = 10000

def get_rand(p):
    return secrets.randbelow(p-1) + 1

def to_bytes(p):
    return (int (p)).to_bytes((p.bit_length() + 7) // 8, "big")

# TODO: Generate Diffie-Hellman keys
def gen_key(g, p, B):
    """
    Choose random a in [1, p-2]
    find A: g ^ a mod p
    find KA: B ^ a mod p
    output: A, KA
    """
    a = random.randint(1, p-1)
    A = pow(g, a, p)
    KA = pow(B, a, p)
    return (KA, A)
    #raise NotImplementedError("Key generation not implemented!")

# TODO: Decrypt multiplication one-time pad
def otp_decrypt(key, p, ctext):
    """
    output: ctext * key^-1 mod p
    Hint: You will need to compute modular inverse
    """
    k = key % p
    '''for i in range(1, p):
        if(((k*i) % p) == 1):
            keyInverse = i
            break'''
    keyInverse = invert(key, p)
    return (ctext * keyInverse) % p
    #raise NotImplementedError("Decryption not implemented!")


def run_client(*con):
    def receive_ints(s):
        received = s.recv(CHUNK).decode()
        print("Server:", received)
        try:
            parsed = [int(x) for x in received.strip("\n").split(",")]
        except ValueError:
            print("Client exiting")
            exit(1)
        return parsed

    keys = [0, 0]
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(con)
        print(s.recv(CHUNK).decode())

        choice_bit = input("Choose desired secret share (0/1): ")
        try:
            choice_bit = int(choice_bit)
            if choice_bit % 2 != choice_bit:
                raise ValueError()
        except ValueError:
            print("Please enter 0 or 1 for your choice")
            return 1

        # Receive D-H parameters from the server
        generator, modulus, server_pkey = receive_ints(s)

        # Generate our D-H public key and shared key
        pkey, ka_key = gen_key(generator, modulus, server_pkey)
        pkey2, ka_key2 = gen_key(generator, modulus, server_pkey) #generated another key for the 2nd half of ct - Casey

        # The server will encrypt each plaintext with our keys
        keys[choice_bit] = pkey
        keys[1 - choice_bit] = pkey2 #add our 2nd key to list to be sent to the server - Casey
        formatted_keys = ','.join(str(key) for key in keys).encode()

        # Send keys to server
        s.send(formatted_keys)

        # Receive both ciphertexts from server encrypted with respective keys
        ctexts = receive_ints(s)

    # Decrypt the one ciphertext we can decrypt (as determined earlier by choice_bit)
    ptext1 = otp_decrypt(ka_key, modulus, ctexts[choice_bit])
    ptext2 = otp_decrypt(ka_key2, modulus, ctexts[1 - choice_bit]) #Decrypt the other CT because its local and we can - Casey
    print("Decrypted text1:")
    #print(to_bytes(ptext1))
    print(ptext1) #print decrypted plaintext as an (I think) integer - Casey
    print("Decrypted text2:")
    #print(to_bytes(ptext2))
    print(ptext2) #print decrypted plaintext as an (I think) integer - Casey

    #xor both halves of the text as instructed by server - Casey
    flag = []
    for x, y in zip(ptext1, ptext2):
        flag.append(x ^ y)
    print("".join(flag))

    return 0

def main(argv):
    if len(argv) != 3:
        print(f"usage: ./{sys.argv[0]} host port")
        return 1

    host, port = argv[1:]
    return run_client(host, int(port))

if __name__ == "__main__":
    sys.exit(main(sys.argv))
