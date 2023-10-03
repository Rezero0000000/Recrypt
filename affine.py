def invers():
    a_inv = 0

    for i in range(26):
        flag = (3 * i) % 26
        if flag == 1:
            a_inv += i

    return a_inv

def affEnc(plainText, keyA, keyB):
    cipherText = ""

    for char in plainText:

        if char == " ":
            cipherText += " "

        elif char.isalpha():

            is_upper = char.isupper()
            char = char.lower()
            ascii_val = ord(char) - ord('a')
            alfaIndex = ((ascii_val * keyA) + keyB) % 26
            cipherChar = chr(alfaIndex + ord('a'))

            if is_upper:
                cipherChar = cipherChar.upper()
            cipherText += cipherChar

    return cipherText

def affDec(cipherText, keyA, keyB):
    plainText = ""

    for char in cipherText:

        if char == " ":
            plainText += " "

        elif char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            ascii_val = ord(char) - ord('a')
            alfaIndex = ((invers() * (ascii_val - keyB)) % 26)
            plainChar = chr(alfaIndex + ord('a'))

            if is_upper:
                plainChar = plainChar.upper()
            plainText += plainChar

    return plainText

plainText = "Hello, World! 123"
keyA = 5
keyB = 7

encrypted = affEnc(plainText, keyA, keyB)
decrypted = affDec(encrypted, keyA, keyB)

print("Pesan Asli:", plainText)
print("Pesan Terenkripsi:", encrypted)
print("Pesan Terdekripsi:", decrypted)
