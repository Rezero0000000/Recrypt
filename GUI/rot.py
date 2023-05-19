# Xnuvers007
import tkinter as tk
from tkinter import messagebox

rot13 = 'abcdefghijklmnopqrstuvwxyz'
rot18 = 'abcdefghijklmnopqrstuvwxyz0123456789'

def rotEnc(plainText, key):
    global rot13
    global rot18

    cipherText = ""

    for i in range(0, len(plainText)):
        if plainText[i] == ' ':
            cipherText = cipherText + " "
        elif key == "rot13":
            for j in range(0, len(rot13)):
                if plainText[i] == rot13[j]:
                    if j < 13 and j >= 0:
                        cipherText = cipherText + rot13[j + 13]
                    elif j > 13 and j <= 25:
                        cipherText = cipherText + rot13[j - 13]
                    elif j == 13:
                        cipherText = cipherText + "a"
        elif key == "rot18":
            for j in range(0, len(rot18)):
                if plainText[i] == rot18[j]:
                    if j < 18 and j >= 0:
                        cipherText = cipherText + rot18[j + 18]
                    elif j > 18 and j <= 35:
                        cipherText = cipherText + rot18[j - 18]
                    else:
                        cipherText = cipherText + "a"
        else:
            print("Kunci yang dimasukkan salah.")

    return cipherText


def encrypt_rot13():
    plaintext = plain_text_entry.get()

    if plaintext:
        ciphertext = rotEnc(plaintext, "rot13")
        cipher_text_entry.delete(0, tk.END)
        cipher_text_entry.insert(tk.END, ciphertext)
    else:
        messagebox.showerror("Error", "Silakan masukkan teks biasa.")


def decrypt_rot13():
    ciphertext = cipher_text_entry.get()

    if ciphertext:
        plaintext = rotEnc(ciphertext, "rot13")
        plain_text_entry.delete(0, tk.END)
        plain_text_entry.insert(tk.END, plaintext)
    else:
        messagebox.showerror("Error", "Silakan masukkan teks sandi.")


def encrypt_rot18():
    plaintext = plain_text_entry.get()

    if plaintext:
        ciphertext = rotEnc(plaintext, "rot18")
        cipher_text_entry.delete(0, tk.END)
        cipher_text_entry.insert(tk.END, ciphertext)
    else:
        messagebox.showerror("Error", "Silakan masukkan teks biasa.")


def decrypt_rot18():
    ciphertext = cipher_text_entry.get()

    if ciphertext:
        plaintext = rotEnc(ciphertext, "rot18")
        plain_text_entry.delete(0, tk.END)
        plain_text_entry.insert(tk.END, plaintext)
    else:
        messagebox.showerror("Error", "Silakan masukkan teks sandi.")


# Membuat jendela utama
window = tk.Tk()
window.title("ROT13 & ROT18 Cipher")
window.geometry("400x250")

# Membuat label
plain_text_label = tk.Label(window, text="Teks Biasa:")
cipher_text_label = tk.Label(window, text="Teks Sandi:")

# Membuat kotak masukan teks
plain_text_entry = tk.Entry(window, width=30)
cipher_text_entry = tk.Entry(window, width=30)

# Membuat tombol
encrypt_rot13_button = tk.Button(window, text="Enkripsi ROT13", command=encrypt_rot13)
decrypt_rot13_button = tk.Button(window, text="Dekripsi ROT13", command=decrypt_rot13)
encrypt_rot18_button = tk.Button(window, text="Enkripsi ROT18", command=encrypt_rot18)
decrypt_rot18_button = tk.Button(window, text="Dekripsi ROT18", command=decrypt_rot18)

# Menempatkan elemen-elemen dalam jendela
plain_text_label.pack()
plain_text_entry.pack()
encrypt_rot13_button.pack()
decrypt_rot13_button.pack()

cipher_text_label.pack()
cipher_text_entry.pack()
encrypt_rot18_button.pack()
decrypt_rot18_button.pack()

# Menjalankan jendela utama
window.mainloop()
