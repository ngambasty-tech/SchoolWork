def affine_decrypt(ciphertext, b):
    """
    Decrypt a ciphertext encrypted with the affine function y = 3x + b (mod 26).
    The inverse of 3 modulo 26 is 9 because 3 * 9 = 27 ≡ 1 (mod 26).
    Decryption: x = 9 * (y - b) mod 26.
    """
    plaintext = []
    for ch in ciphertext:
        if ch.isalpha():
            # Convert letter to number (a=0, b=1, ..., z=25)
            y = ord(ch) - ord('a')
            # Apply decryption formula
            x = (9 * (y - b)) % 26
            # Convert back to letter
            plaintext.append(chr(x + ord('a')))
        else:
            # Keep non‑letters unchanged (just in case)
            plaintext.append(ch)
    return ''.join(plaintext)

def main():
    # Given ciphertext
    ciphertext = "tcabtiqmfheqqmrmvmtmaq"
    
    print("Trying all possible b values (0 to 25):\n")
    for b in range(26):
        decrypted = affine_decrypt(ciphertext, b)
        print(f"b = {b:2d}: {decrypted}")
    
    print("\nThe meaningful English plaintext appears when b = 14:")
    print(affine_decrypt(ciphertext, 14))

if __name__ == "__main__":
    main()