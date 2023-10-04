def encsar(plainText, key):
    cipherText = ""

    for char in plainText:
        if char.isalpha():
            shifted = ord(char) + key
    
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            
            cipherText += chr(shifted)
        
        else:
            cipherText += char

    return cipherText

def decsar(cipherText, key):
    plainText = ""
    
    for char in cipherText:
        if char.isalpha():
            shifted = ord(char) - key
         
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            plainText += chr(shifted)
        
        else:
            plainText += char

    return plainText

# Example 
#plainText = "Hello, World!"
#print("Plaintext:", plainText)
#print("Encrypted Text:", encsar(plainText, 3))
#print("Decrypted Text:", decsar("Khoor, Zruog!", 3))
