alfabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def invers(keyA):
    a_inv = 0

    for i in range(52): 
        flag = (keyA * i) % 52
        if flag == 1:
            a_inv += i

    return a_inv

def affenc(plainText, keyA, keyB):
    global alfabet
    cipherText = ""

    for i in range(0, len(plainText)):

        if plainText[i] == " ":
            cipherText = cipherText + " "

        for j in range(0, len(alfabet)):

            if plainText[i] == alfabet[j]:
                alfaIndex = ((j * keyA) + keyB) % 52
                cipherText = cipherText + alfabet[alfaIndex]

    return cipherText

def affdec(cipherText, keyA, keyB):
    global alfabet
    plainText = ""

    for i in range(0, len(cipherText)):

        if cipherText[i] == " ":
            plainText = plainText + " "

        for j in range(0, len(alfabet)):

            if cipherText[i] == alfabet[j]:
                alfaIndex = ((invers(keyA) * (j - keyB)) % 52)
                plainText = plainText + alfabet[alfaIndex]

    return plainText

