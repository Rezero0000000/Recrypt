def vigenc(plainText, key):
    cipherText = ""
    key = key.lower()

    for i in range(len(plainText)):
        if plainText[i].isalpha():
           
            plain_char = plainText[i].lower()
            key_char = key[i % len(key)]
            
            shift = (ord(plain_char) + ord(key_char) - 2 * ord('a')) % 26
            cipher_char = chr(shift + ord('a'))

            if plainText[i].isupper():
                cipher_char = cipher_char.upper()
            cipherText += cipher_char

        else:
            cipherText += plainText[i]

    return cipherText

def vigdec(cipherText, key):
    plainText = ""
    key = key.lower()

    for i in range(len(cipherText)):
        if cipherText[i].isalpha():
            
            cipher_char = cipherText[i].lower()
            key_char = key[i % len(key)]
            
            shift = (ord(cipher_char) - ord(key_char)) % 26
            plain_char = chr(shift + ord('a'))

            if cipherText[i].isupper():
                plain_char = plain_char.upper()
            plainText += plain_char

        else:
            plainText += cipherText[i]

    return plainText

# Example
#plainText = "Hello, World! 123"
#key = "key"

#encrypted = vigEnc(plainText, key)
#decrypted = vigDec(encrypted, key)

#print("Plaintext:", plainText)
#print("Encrypted Text:", encrypted)
#print("Decrypted Text:", decrypted)

