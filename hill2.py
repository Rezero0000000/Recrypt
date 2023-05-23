alfabet = "abcdefghijklmnopqrstuvwxyz"

def alfaToInt (text):
    global alfabet
    integer = []

    for i in range(len(text)):
            for a in range(len(alfabet)):
                if (alfabet[a] == text[i]):
                    integer.append(a)
    return integer

def makeMatrix (key, text):
    mtrKey = []
    mtrText = []

    if ((len(key)/2 == 2) and (len(text) %2 == 0)):
        key = alfaToInt(key)
        text = alfaToInt(text)
        
        #print(text)
        #print(text[2:4])

        for i in range(int(len(text)/2)):
            mtrText.append([text[i:i+1], text[i:i+2 ]])

        mtrKey = [[key[0], key[1]], [key[2], key[3]]]
        
        return mtrKey, mtrText
    elif ((len(key)/3 == 3) and (len(text) %3 == 0)):
        key = alfaToInt(key)
        text = alfaToInt(text)


def hillEnc (key, plainText):
    key,plainText = makeMatrix(key, plainText)
    print(key,plainText) 

hillEnc('lidh', 'kete')
