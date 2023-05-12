rot13 = 'abcdefghijklmnopqrstuvwxyz'
rot18 = 'abcdefghijklmnopqrstuvwxyz0123456789'

def rotEnc (plainText, key):
    global rot13
    global rot18

    cipherText = ""

    for i in range(0, len(plainText)):
        if plainText[i] == ' ':
            cipherText = cipherText + " "
        elif key == "rot13":
            for j in range(0, len(rot13)):

                if plainText[i] == rot13[j]:
                    if j < 13 and j >= 0:
                        cipherText = cipherText + rot13[j + 13]
                    elif j > 13 and j <= 25:
                        cipherText = cipherText + rot13[j - 13]
                    elif j == 13:
                        cipherText = cipherText + "a"
        elif key == "rot18":
            for j in range (0, len(rot18)):

                if plainText[i] == rot18[j]:
                    if j < 18 and j >= 0:
                        cipherText = cipherText + rot18[j + 18]
                    elif j > 18 and j <= 35:
                        cipherText = cipherText + rot18[j - 18]
                    else:
                        cipherText = cipherText + "a"
        else:
            print("woi salah kampret")
                        
    print(cipherText, '\n')

rotEnc("oyasumi oyasumi close your eyes and you leave this dream", 'rot13')
rotEnc("blnfhzv blnfhzv pybfr lbhe rlrf naq lbh yrnir guvf qernz","rot13")

rotEnc("oyasumi oyasumi close your eyes and you leave this dream", 'rot18')
rotEnc("6gsac40 6gsac40 u36aw g6c9 wgwa s5v g6c 3wsdw bz0a v9ws4", 'rot18')
















