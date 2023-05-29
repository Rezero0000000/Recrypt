# Cipher
import os as os
os.system("cls")

print("=======--- [ Chose cipher ] ---=======\n")

print("[1]. Affine\n[2]. Base64\n[3]. Caesar\n[4]. Hill\n[5]. RandomAlfa\n[6]. Rot\n[7]. Transposition\n[8]. Vigenere\n")
cipher = int(input("Chose option: "))

def getAction ():
    os.system("cls")

    print("=======--- [ Chose Option ] ---=======\n")

    print("[1]. Encrypt\n[2]. Decrypt\n")
    status = int(input("Chose option: "))

    if ((status != 1) and (status != 2)):        
        print("Wrong input:(")
        return False
    return status

match cipher:
    case 1:
        action = getAction()
        if (action == 1):
            
    case 2:
        action = getAction()
        print(action)
    case 3:
        action = getAction()
        print(action)
    case 4:   
        action = getAction()
        print(action)
    case 5: 
        action = getAction()
        print(action)
    case 6:  
        action = getAction()
        print(action)
    case 7:
        action = getAction()
        print(action)
    case 8:   
        action = getAction()
        print(action)
    case _:
        print("Wrong input :(")


