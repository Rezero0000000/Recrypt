# Xnuvers007
import tkinter as tk

alfabet = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}

number = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}

def cipherAlfa(text):
    global alfabet
    result = []

    for i in range(len(text)):
        result.append(alfabet[text[i]])

    return result


def vigEnc(plainText, key):
    global number

    key = cipherAlfa(key)
    keyIndex = 0
    plainText = cipherAlfa(plainText)
    result = []
    cipherText = ""

    for i in range(len(plainText)):
        result.append((plainText[i] + key[keyIndex]) % 26)
        keyIndex = (keyIndex + 1) % len(key)

    for i in range(len(result)):
        cipherText += number[result[i]]

    return cipherText


def vigDec(cipherText, key):
    global number

    key = cipherAlfa(key)
    keyIndex = 0
    cipherText = cipherAlfa(cipherText)
    result = []
    plainText = ""

    for i in range(len(cipherText)):
        result.append((cipherText[i] - key[keyIndex]) % 26)
        keyIndex = (keyIndex + 1) % len(key)

    for i in range(len(result)):
        plainText += number[result[i]]

    return plainText


def encrypt_text():
    plain_text = entry_plain_text.get()
    encryption_key = entry_encryption_key.get()
    encrypted_text = vigEnc(plain_text, encryption_key)
    label_encrypted_text["text"] = "Encrypted Text: " + encrypted_text


def decrypt_text():
    cipher_text = entry_cipher_text.get()
    decryption_key = entry_decryption_key.get()
    decrypted_text = vigDec(cipher_text, decryption_key)
    label_decrypted_text["text"] = "Decrypted Text: " + decrypted_text


# Create Tkinter window
window = tk.Tk()
window.title("Vigenere Cipher")

# Create labels
label_plain_text = tk.Label(window, text="Plain Text:")
label_plain_text.grid(row=0, column=0, pady=5)

label_encryption_key = tk.Label(window, text="Encryption Key:")
label_encryption_key.grid(row=1, column=0, pady=5)

label_cipher_text = tk.Label(window, text="Cipher Text:")
label_cipher_text.grid(row=2, column=0, pady=5)

label_decryption_key = tk.Label(window, text="Decryption Key:")
label_decryption_key.grid(row=3, column=0, pady=5)

label_encrypted_text = tk.Label(window, text="Encrypted Text:")
label_encrypted_text.grid(row=4, column=0, pady=5)

label_decrypted_text = tk.Label(window, text="Decrypted Text:")
label_decrypted_text.grid(row=5, column=0, pady=5)

# Create entry fields
entry_plain_text = tk.Entry(window)
entry_plain_text.grid(row=0, column=1, pady=5)

entry_encryption_key = tk.Entry(window)
entry_encryption_key.grid(row=1, column=1, pady=5)

entry_cipher_text = tk.Entry(window)
entry_cipher_text.grid(row=2, column=1, pady=5)

entry_decryption_key = tk.Entry(window)
entry_decryption_key.grid(row=3, column=1, pady=5)

# Create buttons
button_encrypt = tk.Button(window, text="Encrypt", command=encrypt_text)
button_encrypt.grid(row=6, column=0, pady=10)

button_decrypt = tk.Button(window, text="Decrypt", command=decrypt_text)
button_decrypt.grid(row=6, column=1, pady=10)

# Create output labels
label_encrypted_text_output = tk.Label(window, text="Encrypted Text: ")
label_encrypted_text_output.grid(row=7, column=0, columnspan=2, pady=5)

label_decrypted_text_output = tk.Label(window, text="Decrypted Text: ")
label_decrypted_text_output.grid(row=8, column=0, columnspan=2, pady=5)

# Run the Tkinter event loop
window.mainloop()
