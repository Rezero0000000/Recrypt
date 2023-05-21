import os as os

os.system("cls")
print("=======--- [ Welcome ] ---=======\n")
print("[1]. Encrypt\n[2]. Decrypt\n")
status = int(input("Chose option: "))

def method ():
    os.system("cls")

    print("=======--- [ Chose cipher ] ---=======\n")
    print("[1]. Affine\n[2]. Base64\n[3]. Caesar\n[4]. Hill\n[5]. RandomAlfa\n[6]. Rot\n[7]. Transposition\[8]. Vigenere\n")
    status = int(input("Chose option: "))

    return status


if (status == 1):
    cipher = method()
    print(cipher)
elif (status == 2):
    print('2')
else:
    print("Wrong Option")
