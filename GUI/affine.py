# Xnuvers007

import tkinter as tk
from tkinter import messagebox

alfabet = "abcdefghijklmnopqrstuvwxyz"

def invers():
    a_inv = 0

    for i in range(26):
        flag = (3 * i) % 26
        if flag == 1:
            a_inv += i

    return a_inv


def affEnc(plainText, keyA, keyB):
    global alfabet
    cipherText = ""

    for i in range(0, len(plainText)):

        if plainText[i] == " ":
            cipherText = cipherText + " "

        for j in range(0, len(alfabet)):

            if plainText[i] == alfabet[j]:
                alfaIndex = ((j * keyA) + keyB) % 26
                cipherText = cipherText + alfabet[alfaIndex]

    return cipherText


def affDec(cipherText, keyA, keyB):
    global alfabet
    plainText = ""

    for i in range(0, len(cipherText)):

        if cipherText[i] == " ":
            plainText = plainText + " "

        for j in range(0, len(alfabet)):

            if cipherText[i] == alfabet[j]:
                alfaIndex = ((invers() * (j - keyB)) % 26)
                plainText = plainText + alfabet[alfaIndex]

    return plainText


def encrypt():
    plaintext = plain_text_entry.get()
    key_a = int(key_a_entry.get())
    key_b = int(key_b_entry.get())

    if plaintext and key_a and key_b:
        cipher_text = affEnc(plaintext, key_a, key_b)
        cipher_text_entry.delete(0, tk.END)
        cipher_text_entry.insert(tk.END, cipher_text)
    else:
        messagebox.showerror("Error", "Please enter all the required values.")


def decrypt():
    ciphertext = cipher_text_entry.get()
    key_a = int(key_a_entry.get())
    key_b = int(key_b_entry.get())

    if ciphertext and key_a and key_b:
        plain_text = affDec(ciphertext, key_a, key_b)
        plain_text_entry.delete(0, tk.END)
        plain_text_entry.insert(tk.END, plain_text)
    else:
        messagebox.showerror("Error", "Please enter all the required values.")


# Create the main window
window = tk.Tk()
window.title("Affine Cipher")
window.geometry("400x200")

# Create the labels
plain_text_label = tk.Label(window, text="Plain Text:")
key_a_label = tk.Label(window, text="Key A:")
key_b_label = tk.Label(window, text="Key B:")
cipher_text_label = tk.Label(window, text="Cipher Text:")

# Create the text entry fields
plain_text_entry = tk.Entry(window, width=30)
key_a_entry = tk.Entry(window, width=10)
key_b_entry = tk.Entry(window, width=10)
cipher_text_entry = tk.Entry(window, width=30)

# Create the buttons
encrypt_button = tk.Button(window, text="Encrypt", command=encrypt)
decrypt_button = tk.Button(window, text="Decrypt", command=decrypt)

# Position the labels
plain_text_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
key_a_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
key_b_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
cipher_text_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

# Position the text entry fields
plain_text_entry.grid(row=0, column=1, padx=10, pady=5)
key_a_entry.grid(row=1, column=1, padx=10, pady=5)
key_b_entry.grid(row=2, column=1, padx=10, pady=5)
cipher_text_entry.grid(row=3, column=1, padx=10, pady=5)

# Position the buttons
encrypt_button.grid(row=4, column=0, padx=10, pady=10)
decrypt_button.grid(row=4, column=1, padx=10, pady=10)

# Start the GUI event loop
window.mainloop()
