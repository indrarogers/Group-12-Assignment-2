import string

# ---------------- Encryption / Decryption helpers ----------------
def shift_char(c, shift, direction="forward"):
    """Shift a character by 'shift' steps in given direction."""
    if c.islower():
        alphabet = string.ascii_lowercase
    elif c.isupper():
        alphabet = string.ascii_uppercase
    else:
        return c  # non-letters unchanged

    idx = alphabet.index(c)
    if direction == "forward":
        new_idx = (idx + shift) % 26
    else:  # backward
        new_idx = (idx - shift) % 26
    return alphabet[new_idx]


def encrypt(text, shift1, shift2):
    encrypted = []
    for c in text:
        if c.islower():
            if c <= "m":  # first half
                encrypted.append(shift_char(c, shift1 * shift2, "forward"))
            else:  # second half
                encrypted.append(shift_char(c, shift1 + shift2, "backward"))
        elif c.isupper():
            if c <= "M":  # first half
                encrypted.append(shift_char(c, shift1, "backward"))
            else:  # second half
                encrypted.append(shift_char(c, shift2**2, "forward"))
        else:
            encrypted.append(c)  # unchanged
    return "".join(encrypted)


def decrypt(text, shift1, shift2):
    decrypted = []
    for c in text:
        if c.islower():
            if c <= "m":  # first half
                decrypted.append(shift_char(c, shift1 * shift2, "backward"))
            else:  # second half
                decrypted.append(shift_char(c, shift1 + shift2, "forward"))
        elif c.isupper():
            if c <= "M":  # first half
                decrypted.append(shift_char(c, shift1, "forward"))
            else:  # second half
                decrypted.append(shift_char(c, shift2**2, "backward"))
        else:
            decrypted.append(c)  # unchanged
    return "".join(decrypted)

# ---------------- File functions ----------------
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

# ---------------- Main program ----------------
if __name__ == "__main__":
    shift1 = int(input("Enter shift1: "))
    shift2 = int(input("Enter shift2: "))

    encrypt_file(shift1, shift2)
    decrypt_file(shift1, shift2)
    verify()
