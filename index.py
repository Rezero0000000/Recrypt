# Cipher
import os as os
os.system("cls")

print("=======--- [ Chose cipher ] ---=======\n")

print("[1]. Affine\n[2]. Base64\n[3]. Caesar\n[4]. Hill\n[5]. RandomAlfa\n[6]. Rot\n[7]. Transposition\n[8]. Vigenere\n")
cipher = int(input("Chose option: "))

os.system("cls")

print("=======--- [ Chose Option ] ---=======\n")

print("[1]. Encrypt\n[2]. Decrypt\n")
status = int(input("Chose option: "))

match cipher:
    case 1:
    case 2:
    case 3:
    case 4:
    case 5:
    case 6:
    case 7:
    case 8:
    case _:
        action-default
