# Cipher
import os as os
os.system("cls")

print("=======--- [ Welcome ] ---=======\n")
print("[1]. Encrypt\n[2]. Decrypt\n")

status = int(input("Chose option: "))
cipherList = {
    1: "affine", 
    2: "base64", 
    3: "caesar", 
    4: "hill",
    5: "randomAlfa", 
    6: "rot",
    7: "transposition",
    8: "vignere"
}

def getCipher ():
    global cipherList
    os.system("cls")

    print("=======--- [ Chose cipher ] ---=======\n")
    print("[1]. Affine\n[2]. Base64\n[3]. Caesar\n[4]. Hill\n[5]. RandomAlfa\n[6]. Rot\n[7]. Transposition\n[8]. Vigenere\n")

    status = int(input("Chose option: "))
    isCipher = (
            (status == 1) or (status == 2) or 
            (status == 3) or (status == 5) or
            (status == 4) or (status == 6) or
            (status == 7) or (status == 8)
        )
   
    if (isCipher):
        return cipherList[status]
    else:
        print("wrong input")




if (status == 1):
    cipher = getCipher()
    print(cipher)
elif (status == 2):
    print('2')
else:
    print("Wrong Option")
