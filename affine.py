alfabet = "abcdefghijklmnopqrstuvwxyz"

def invers ():
    a_inv = 0

    for i in range(26):
        flag = (3 * i)%26
        if flag == 1:
            a_inv += i

    return a_inv

def affEnc (plainText, keyA, keyB):
    global alfabet
    cipherText = ""
    
    for i in range(0, len(plainText)):

        if plainText[i] == " ":
            cipherText = cipherText + " "

        for j in range(0, len(alfabet)):

            if plainText[i] == alfabet[j]:
                alfaIndex = ((j*keyA) + keyB) % 26
                cipherText = cipherText + alfabet[alfaIndex]

    return cipherText

def affDec (cipherText, keyA, keyB):
    global alfabet
    plainText = ""

    for i in range(0, len(cipherText)):

        if cipherText[i] == " ":
            plainText = plainText + " "

        for j in range(0, len(alfabet)):
          
            if cipherText[i] == alfabet[j]:
                alfaIndex = ((invers() * (j  - keyB)) % 26)
                plainText = plainText + alfabet[alfaIndex]

    return plainText
