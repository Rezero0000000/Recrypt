alfabet = 'abcdefghijklmnopqrstuvwxyz'

def checkKey (key, text):
    global alfabet
    mtrKey = []
    mtrText = []
    
    if (len(key) == 4):
        mtr2 = []

        #key Loop
        for i in range(4):
            for j in range (len(alfabet)):
                if (key[i] == alfabet[j]):
                    mtr2.append(j)

        mtrKey.append([mtr2[0], mtr2[1]])
        mtrKey.append([mtr2[2], mtr2[3]])

        #Text loop
        mtr2 = []
        for i in range (len(text)):
            for j in range (len(alfabet)):
                if (text[i] == alfabet[j]):
                    mtr2.append(j)

        for i in range (int(len(mtr2)/2)):
            mtrText.append([mtr2[i], mtr2[i+1]])

        return mtrText, mtrKey

    elif (len(key) == 9):
        mtr3 = []
        
        #key loop
        for i in range(9):
            for j in range (len(alfabet)):
                if (key[i] == alfabet[j]):
                    mtr3.append(j)

        mtrText.append([mtr3[0], mtr3[1], mtr3[2]])
        mtrText.append([mtr3[3], mtr3[4], mtr3[5]])
        mtrText.append([mtr3[6], mtr3[7], mtr3[8]])

        #Text loop
        return mtrText,text

    else:
        print ("wrong key")
        return False

def hillDec (plainText, key):
    cipherText = ""
    result = []
    keyArr = []

    if (checkKey(key, plainText) == False):
        return False

    plainText, keyArr = checkKey(key, plainText)
    print(keyArr)
    print(plainText)

hillDec("helolo", "baka")
    
    
