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
 [4] Transposition cipher
 [5]. Vignere cipher
          """)

    option = int(input(" Choose cipher: "))
    return option

while True:
    print(icon)
    print(" [1]. Encryption\n [2]. Decryption\n")
 
    try:
        option = int(input("Your option: "))
        if option == 1 or option == 2:
            cipherList()
            break
        else:
            print("Invalid option. Please enter 1 or 2.")
    except ValueError:
        print("\n- Invalid input. Please enter a valid integer. -")
        break
