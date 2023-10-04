from affine import affenc, affdec
from caesar import encsar, decsar
from rot import rotenc
from transposition import enctrans, dectrans
from vigenere import vigenc, vigdec

import os

icon = """


  ____                            _   
 |  _ \ ___  ___ _ __ _   _ _ __ | |_ 
 | |_) / _ \/ __| '__| | | | '_ \| __|
 |  _ <  __/ (__| |  | |_| | |_) | |_ 
 |_| \_\___|\___|_|   \__, | .__/ \__|
                      |___/|_|      

 ------- [ Created by Schwatz] -------
 
"""

def cipherList () :
    os.system('cls')
    print(icon)
    print(""" 
 [1]. Affine cipher 
 [2]. Caesar ciphern 
 [3]. Rot cipher 
 [4]. Transposition cipher
 [5]. Vignere cipher
          """)

    option = int(input(" Choose cipher: "))
    if option < 0 or option > 5:
        print(" salah tod")
        return False 
    return option

while True:
    os.system("cls")
    print(icon)
    print(" [1]. Encryption\n [2]. Decryption\n")
 
    try:
        option = int(input(" Your option: "))
        if option == 1 or option == 2:
            cipherType = cipherList() 
            if cipherType == False:
                break

            text = input("\n Enter the text: ")
            
            if cipherType == 1: 
                keyA = int(input(" key A: "))
                keyB = int(input(" key B: "))

                if option == 1: 
                    encryptedText = affenc(text, keyA, keyB)
                    print("\n Encrypted text: ", encryptedText)

                elif option == 2:  
                    decryptedText = affdec(text, keyA, keyB)
                    print("\n Decrypted text: ", decryptedText)
                    
            elif cipherType == 2: 
                key = int(input(" Key: "))
                
                if option == 1:
                    encryptedText = encsar(text, key)
                    print("\n Encrypted text: ", encryptedText)

                elif option == 2: 
                    decryptedText = decsar(text, key)
                    print("\n Decrypted text: ", decryptedText)

            elif cipherType == 3: 
                key = str(input("\n Key [rot13/rot18]: "))
                
                if option == 1 or option == 2:
                    encryptedText = rotenc(text, key)
                    if (encryptedText == False):
                        break

                    print("\n Encrypted text: ", encryptedText)

            elif cipherType == 4: 
                key = int(input(" Key: "))
                
                if option == 1:
                    encryptedText = enctrans(text, key)
                    print("\n Encrypted text: ", encryptedText)

                elif option == 2: 
                    decryptedText = dectrans(text, key)
                    print("\n Decrypted text: ", decryptedText)
            
            elif cipherType == 5: 
                key = str(input(" Key: "))
                
                if option == 1:
                    encryptedText = vigenc(text, key)
                    print("\n Encrypted text: ", encryptedText)

                elif option == 2: 
                    decryptedText = vigdec(text, key)
                    print("\n Decrypted text: ", decryptedText)
            
            break
        else:
            print(" Invalid option. Please enter 1 or 2.")

    except ValueError:
        print("\n - Invalid input. Please enter a valid integer. -")
        break
