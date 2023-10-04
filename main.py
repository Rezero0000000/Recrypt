from affine import affenc, affdec
from caesar import encsar, decsar
#from rot import rotecn
from transposition import enctrans, dectrans
from vignere import vigenc, vigdec

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
 
    option = int(input(" Your option : "))
    
    if option == 1:
        cipherList()
        break
    elif option == 2:
        cipherList()
        break
    else:
        break
