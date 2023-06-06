alfabet = "abcdefghijklmnopqrstuvwxyz"
key = "qamocdbyruwskjnvtzfilpeghx"

def randomEnc (plainText):
    global alfabet
    global key

    cipherText = ""

    for i in range(0, len(plainText)):
        if plainText[i] == " ":
            cipherText = cipherText + " "
        else:
            for j in range(0, len(alfabet)):
                if plainText[i] == alfabet[j]:
                    cipherText = cipherText + key[j]
    return cipherText

def randomDec (cipherText):
    global alfabet 
    global key

    plainText = ""

    for i in range(0, len(cipherText)):
        if cipherText[i] == " ":
            plainText = plainText + " "
        else:
            for j in range(0, len(alfabet)):
                if cipherText[i] == key[j]:
                    plainText = plainText + alfabet[j]
    return plainText

