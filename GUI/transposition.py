# Xnuvers007
import tkinter as tk

def enctrans(plainText, key):
    while len(plainText) % key > 0:
        plainText = plainText + "#"

    n = len(plainText) // key
    cipherText = ""

    for i in range(key):
        for j in range(n):
            cipherText = cipherText + plainText[i + j * key]

    return cipherText


def dectrans(cipherText, key):
    while len(cipherText) % key > 0:
        cipherText = cipherText + "#"

    key = len(cipherText) // key
    n = len(cipherText) // key

    plainText = ""

    for i in range(key):
        for j in range(n):
            if cipherText[i + j * key] == "#":
                cipherText = cipherText + ""
            else:
                plainText = plainText + cipherText[i + j * key]

    return plainText


def encrypt_button_click():
    plain_text = entry_plain_text.get()
    key = int(entry_key.get())
    encrypted_text = enctrans(plain_text, key)
    label_encrypted_text.config(text="Encrypted Text: " + encrypted_text)


def decrypt_button_click():
    cipher_text = entry_cipher_text.get()
    key = int(entry_key.get())
    decrypted_text = dectrans(cipher_text, key)
    label_decrypted_text.config(text="Decrypted Text: " + decrypted_text)


# Create the main window
window = tk.Tk()
window.title("Transposition Cipher")
window.geometry("400x300")

# Create input elements
label_plain_text = tk.Label(window, text="Plain Text:")
label_plain_text.pack()
entry_plain_text = tk.Entry(window)
entry_plain_text.pack()

label_key = tk.Label(window, text="Key:")
label_key.pack()
entry_key = tk.Entry(window)
entry_key.pack()

label_cipher_text = tk.Label(window, text="Cipher Text:")
label_cipher_text.pack()
entry_cipher_text = tk.Entry(window)
entry_cipher_text.pack()

# Create buttons
encrypt_button = tk.Button(window, text="Encrypt", command=encrypt_button_click)
encrypt_button.pack()

decrypt_button = tk.Button(window, text="Decrypt", command=decrypt_button_click)
decrypt_button.pack()

# Create output labels
label_encrypted_text = tk.Label(window, text="Encrypted Text:")
label_encrypted_text.pack()

label_decrypted_text = tk.Label(window, text="Decrypted Text:")
label_decrypted_text.pack()

# Run the main window loop
window.mainloop()
