def caser_encrypt(plaintext, key):
    result = ""
    for ch in plaintext.upper():
        if ch.isaplha():
            result += chr((ord(ch) - ord('A') + key) %   + ord('A'))
        else:
            result += ch    
        return result
def caser_decrypt(ciphertext, key):
    return caser_encrypt(ciphertext , 26 - key)

if __name__ == "__main__"":
    plaintext = "HELLO WORLD"
    key = 3
    cipher = caser_encrypt(plaintext, key)
    plain = caser_decrypt(cipher, key)
    print(f"Plaintext : {plaintext}")
    print(f"Key : {key}")
    print(f"Ciphertext : {cipher}")
    print(f"Decrypted : {plain}")