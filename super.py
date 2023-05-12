from caesar import encsar, decsar
from transposition import enctrans, dectrans

def superEnc (plainText, keyC, keyT):
    return enctrans(encsar(plainText, keyC), keyT)

def superDec (cipherText, keyC, keyT):
    return dectrans(decsar(cipherText, keyC), keyT)

print(superEnc("hello World", 3, 3));
print(superDec("kozohrrgo u#",3,3));

