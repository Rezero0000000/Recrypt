def enctrans (plainText, key):
    while len(plainText)%key > 0:
        plainText = plainText + "#"

    n = len(plainText)//key
    cipherText = ""

    for i in range(key):
        for j in range(n):
            cipherText = cipherText + plainText[i+j*key]
            
    return cipherText

def dectrans (cipherText, key):
    while len(cipherText)%key > 0:
        cipherText = cipherText + "#" 

    key = len(cipherText)//key
    n = len(cipherText)//key

    plainText = ""

    for i in range(key):
        for j in range(n):
            if cipherText[i+j*key] == "#":
                cipherText = cipherText + ""
            else:
                plainText = plainText + cipherText[i+j*key]

    return plainText


