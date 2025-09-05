import string

def shift_char(c, shift, direction="forward", alphabet=None):
    """Shift character c within the given alphabet"""
    if alphabet is None:
        if c.islower():
            alphabet = string.ascii_lowercase
        elif c.isupper():
            alphabet = string.ascii_uppercase
        else:
            return c  # non-letters unchanged

    if c not in alphabet:
        return c  #ignores all that don't meet criteria

    L = len(alphabet)
    idx = alphabet.index(c)
    if direction == "forward":
        new_idx = (idx + shift) % L
    else:  # backward
        new_idx = (idx - shift) % L
    return alphabet[new_idx]


LOWER_FIRST  = string.ascii_lowercase[:13]   # 'a'..'m'
LOWER_SECOND = string.ascii_lowercase[13:]   # 'n'..'z'
UPPER_FIRST  = string.ascii_uppercase[:13]   # 'A'..'M'
UPPER_SECOND = string.ascii_uppercase[13:]   # 'N'..'Z'

#Encryption 

def encrypt(text, shift1, shift2):
    encrypted = []
    for c in text:
        if c.islower():
            if 'a' <= c <= 'm':  # first half
                encrypted.append(shift_char(c, shift1 * shift2, "forward", alphabet=LOWER_FIRST))
            elif 'n' <= c <= 'z':  # second half
                encrypted.append(shift_char(c, shift1 + shift2, "backward", alphabet=LOWER_SECOND))
            else:
                encrypted.append(c)
        elif c.isupper():
            if 'A' <= c <= 'M':  # first half
                encrypted.append(shift_char(c, shift1, "backward", alphabet=UPPER_FIRST))
            elif 'N' <= c <= 'Z':  # second half
                encrypted.append(shift_char(c, shift2**2, "forward", alphabet=UPPER_SECOND))
            else:
                encrypted.append(c)
        else:
            encrypted.append(c)  # unchanged
    return "".join(encrypted)

#Decryption

def decrypt(text, shift1, shift2):
    decrypted = []
    for c in text:
        if c.islower():
            if 'a' <= c <= 'm':  # first half stays first half
                decrypted.append(shift_char(c, shift1 * shift2, "backward", alphabet=LOWER_FIRST))
            elif 'n' <= c <= 'z':  # second half stays second half
                decrypted.append(shift_char(c, shift1 + shift2, "forward", alphabet=LOWER_SECOND))
            else:
                decrypted.append(c)
        elif c.isupper():
            if 'A' <= c <= 'M':  # first half
                decrypted.append(shift_char(c, shift1, "forward", alphabet=UPPER_FIRST))
            elif 'N' <= c <= 'Z':  # second half
                decrypted.append(shift_char(c, shift2**2, "backward", alphabet=UPPER_SECOND))
            else:
                decrypted.append(c)
        else:
            decrypted.append(c)  # unchanged
    return "".join(decrypted)

#File functions
def encrypt_file(shift1, shift2):
    with open("raw_text.txt", "r", encoding="utf-8") as infile:
        raw = infile.read()
    encrypted = encrypt(raw, shift1, shift2)
    with open("encrypted_text.txt", "w", encoding="utf-8") as outfile:
        outfile.write(encrypted)


def decrypt_file(shift1, shift2):
    with open("encrypted_text.txt", "r", encoding="utf-8") as infile:
        encrypted = infile.read()
    decrypted = decrypt(encrypted, shift1, shift2)
    with open("decrypted_text.txt", "w", encoding="utf-8") as outfile:
        outfile.write(decrypted)


def verify():
    with open("raw_text.txt", "r", encoding="utf-8") as f1, \
         open("decrypted_text.txt", "r", encoding="utf-8") as f2:
        if f1.read() == f2.read():
            print("✅ Decryption successful: Original and decrypted match!")
        else:
            print("❌ Decryption failed: Files do not match.")

#User interface
if __name__ == "__main__":
    shift1 = int(input("Enter shift1: "))
    shift2 = int(input("Enter shift2: "))

    encrypt_file(shift1, shift2)
    decrypt_file(shift1, shift2)
    verify()
