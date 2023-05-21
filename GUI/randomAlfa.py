# Xnuvers007
import tkinter as tk
from tkinter import messagebox

alfabet = "abcdefghijklmnopqrstuvwxyz"
key = "qamocdbyruwskjnvtzfilpeghx"

def randomEnc(plainText):
    global alfabet
    global key

    cipherText = ""

    for i in range(0, len(plainText)):
        if plainText[i] == " ":
            cipherText = cipherText + " "
        else:
            for j in range(0, len(alfabet)):
                if plainText[i] == alfabet[j]:
                    cipherText = cipherText + key[j]
    return cipherText

def randomDec(cipherText):
    global alfabet 
    global key

    plainText = ""

    for i in range(0, len(cipherText)):
        if cipherText[i] == " ":
            plainText = plainText + " "
        else:
            for j in range(0, len(alfabet)):
                if cipherText[i] == key[j]:
                    plainText = plainText + alfabet[j]
    return plainText


def encrypt():
    plaintext = plain_text_entry.get()

    if plaintext:
        ciphertext = randomEnc(plaintext)
        cipher_text_entry.delete(0, tk.END)
        cipher_text_entry.insert(tk.END, ciphertext)
    else:
        messagebox.showerror("Error", "Silakan masukkan teks biasa.")


def decrypt():
    ciphertext = cipher_text_entry.get()

    if ciphertext:
        plaintext = randomDec(ciphertext)
        plain_text_entry.delete(0, tk.END)
        plain_text_entry.insert(tk.END, plaintext)
    else:
        messagebox.showerror("Error", "Silakan masukkan teks sandi.")


# Membuat jendela utama
window = tk.Tk()
window.title("Random Substitution Cipher")
window.geometry("400x200")

# Membuat label
plain_text_label = tk.Label(window, text="Teks Biasa:")
cipher_text_label = tk.Label(window, text="Teks Sandi:")

# Membuat kotak masukan teks
plain_text_entry = tk.Entry(window, width=30)
cipher_text_entry = tk.Entry(window, width=30)

# Membuat tombol
encrypt_button = tk.Button(window, text="Enkripsi", command=encrypt)
decrypt_button = tk.Button(window, text="Dekripsi", command=decrypt)

# Menempatkan label
plain_text_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
cipher_text_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

# Menempatkan kotak masukan teks
plain_text_entry.grid(row=0, column=1, padx=10, pady=5)
cipher_text_entry.grid(row=1, column=1, padx=10, pady=5)

# Menempatkan tombol
encrypt_button.grid(row=2, column=0, padx=10, pady=10)
decrypt_button.grid(row=2, column=1, padx=10, pady=10)

# Memulai loop peristiwa GUI
window.mainloop()
