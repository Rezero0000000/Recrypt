# Xnuvers007
import tkinter as tk
from tkinter import messagebox

alfabet = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
number = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}

def encsar(plainText, key):
    global alfabet
    global number

    cipherText = ""
    plainText = plainText.lower()
    result = ""

    for i in range(0, len(plainText)):
        if plainText[i] == " ":
            cipherText = " "
        else:
            cipherText = number[(alfabet[plainText[i]] + key) % 26]

        result = result + cipherText
    return result


def decsar(cipherText, key):
    global alfabet
    global number

    plainText = ""
    plainText = plainText.lower()
    result = ""

    for i in range(0, len(cipherText)):
        if cipherText[i] == " ":
            plainText = " "
        elif cipherText[i] == "#":
            plainText = "#"
        else:
            plainText = number[(alfabet[cipherText[i]] - key) % 26]
        result = result + plainText
    return result


def encrypt():
    plaintext = plain_text_entry.get()
    key = int(key_entry.get())

    if plaintext and key:
        ciphertext = encsar(plaintext, key)
        cipher_text_entry.delete(0, tk.END)
        cipher_text_entry.insert(tk.END, ciphertext)
    else:
        messagebox.showerror("Error", "Silakan masukkan teks biasa dan kunci.")


def decrypt():
    ciphertext = cipher_text_entry.get()
    key = int(key_entry.get())

    if ciphertext and key:
        plaintext = decsar(ciphertext, key)
        plain_text_entry.delete(0, tk.END)
        plain_text_entry.insert(tk.END, plaintext)
    else:
        messagebox.showerror("Error", "Silakan masukkan teks sandi dan kunci.")


# Membuat jendela utama
window = tk.Tk()
window.title("Caesar Cipher")
window.geometry("400x200")

# Membuat label
plain_text_label = tk.Label(window, text="Teks Biasa:")
key_label = tk.Label(window, text="Kunci:")
cipher_text_label = tk.Label(window, text="Teks Sandi:")

# Membuat kotak masukan teks
plain_text_entry = tk.Entry(window, width=30)
key_entry = tk.Entry(window, width=10)
cipher_text_entry = tk.Entry(window, width=30)

# Membuat tombol
encrypt_button = tk.Button(window, text="Enkripsi", command=encrypt)
decrypt_button = tk.Button(window, text="Dekripsi", command=decrypt)

# Menempatkan label
plain_text_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
key_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
cipher_text_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

# Menempatkan kotak masukan teks
plain_text_entry.grid(row=0, column=1, padx=10, pady=5)
key_entry.grid(row=1, column=1, padx=10, pady=5)
cipher_text_entry.grid(row=2, column=1, padx=10, pady=5)

# Menempatkan tombol
encrypt_button.grid(row=3, column=0, padx=10, pady=10)
decrypt_button.grid(row=3, column=1, padx=10, pady=10)

# Memulai loop peristiwa GUI
window.mainloop()
