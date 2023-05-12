alfabet = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}

number = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}

def cipherAlfa (text):
    global alfabet 
    result = []

    for i in range(0, len(text)):
        result.append(alfabet[text[i]])

    return result

def vigEnc (plainText, key):
    global number

    key = cipherAlfa(key)
    keyIndex = 0
    plainText = cipherAlfa(plainText)
    result = []
    cipherText = ""

    for i in range(0, len(plainText)):
        result.append((plainText[i] + key[keyIndex]) % 26)
        keyIndex = keyIndex + 1
        
        if keyIndex > (len(key) - 1):
            keyIndex = 0

    for i in range(0, len(result)):
        cipherText = cipherText + number[result[i]]

def vigDec (cipherText, key):
    global number

    key = cipherAlfa(key)
    keyIndex = 0
    cipherText = cipherAlfa(cipherText)
    result = []
    plainText = ""
    resultNumber = 0 
    print(cipherText)
    for i in range (0, len(cipherText)):
        resultNumber = (cipherText[i] - key[keyIndex] % 26)

        if resultNumber < 0:
            resultNumber = ((cipherText[i] - key[keyIndex]) + 26) 
       
        result.append(resultNumber)
        keyIndex = keyIndex + 1

        if keyIndex > (len(key) - 1):
            keyIndex = 0

    for i in range(0, len(result)):
        plainText = plainText + number[result[i]]
    print(plainText)

vigEnc("hatihatidijalan", 'bakanohentai')
vigDec("iadiuoamqbjimax", 'bakanohentai')
 
#print(ord('B'))

