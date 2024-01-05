rot13 = 'abcdefghijklmnopqrstuvwxyz'
rot18 = 'abcdefghijklmnopqrstuvwxyz0123456789'

def rotenc(plainText, key):
    global rot13
    global rot18

    cipherText = ""

    for char in plainText:
        if char == ' ':
            cipherText += " "

        elif key == "rot13":
            if char.isalpha():
                is_upper = char.isupper()
                char = char.lower()
                if char in rot13:
                    index = rot13.index(char)
                    if is_upper:
                        cipherText += rot13[index - 13].upper()
                    else:
                        cipherText += rot13[index - 13]
                else:
                    cipherText += char
            else:
                cipherText += char

        elif key == "rot18":
            if char.isalnum():
                if char.isdigit():
                    index = rot18.index(char)
                    cipherText += rot18[(index + 18) % 36]
                else:
                    is_upper = char.isupper()
                    char = char.lower()
                    if char in rot18:
                        index = rot18.index(char)
                        if is_upper:
                            cipherText += rot18[index - 18].upper()
                        else:
                            cipherText += rot18[index - 18]
            else:
                cipherText += char
        else:
            print("\n Wrong key sir")
            return False

    return cipherText

# Example 
#rotEnc("oyasumi oyasumi close your eyes and you leave this dream", 'rot13')
#rotEnc("blnfhzv blnfhzv pybfr lbhe rlrf naq lbh yrnir guvf qernz", 'rot13')

#rotEnc("oyasumi oyasumi close your eyes and you leave this dream", 'rot18')
#rotEnc("6gsac40 6gsac40 u36aw g6c9 wgwa s5v g6c 3wsdw bz0a v9ws4", 'rot18')

