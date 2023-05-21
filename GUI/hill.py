# Xnuvers007

import tkinter as tk
import numpy as np

def char_to_num(char):
    return ord(char) - 65

def num_to_char(num):
    # Convert a number to a character
    if isinstance(num, np.ndarray):
        return "".join([chr(n + 65) for n in num.flatten()])
    else:
        return chr(num + 65)


def matrix_mod_inverse(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inverse = pow(det, -1, modulus)

    # Find matrix of cofactors
    adj_matrix = np.round(det_inverse * np.linalg.inv(matrix)).astype(int)
    inv_matrix = (adj_matrix * det) % modulus

    return inv_matrix

def hill_cipher_encrypt():
    plaintext = entry_plaintext.get()
    key = entry_key.get()

    plaintext = plaintext.replace(" ", "").upper()
    plaintext_len = len(plaintext)
    key_size = int(np.sqrt(len(key)))
    ciphertext = ""

    # Padding the plaintext if necessary
    if plaintext_len % key_size != 0:
        plaintext += "X" * (key_size - (plaintext_len % key_size))
        plaintext_len = len(plaintext)

    # Generate the ciphertext
    key_matrix = np.array([char_to_num(char) for char in key]).reshape(key_size, key_size)
    for i in range(0, plaintext_len, key_size):
        plain_vector = np.array([char_to_num(char) for char in plaintext[i:i+key_size]]).reshape(key_size, 1)
        cipher_vector = np.dot(key_matrix, plain_vector) % 26
        ciphertext += "".join([num_to_char(num) for num in cipher_vector])

    label_ciphertext["text"] = "Ciphertext: " + ciphertext


def hill_cipher_decrypt():
    ciphertext = entry_ciphertext.get()
    key = entry_key.get()

    ciphertext = ciphertext.replace(" ", "").upper()
    ciphertext_len = len(ciphertext)
    key_size = int(np.sqrt(len(key)))
    plaintext = ""

    # Generate the plaintext
    key_matrix = np.array([char_to_num(char) for char in key]).reshape(key_size, key_size)
    inv_key_matrix = matrix_mod_inverse(key_matrix, 26)
    for i in range(0, ciphertext_len, key_size):
        cipher_vector = np.array([char_to_num(char) for char in ciphertext[i:i+key_size]]).reshape(key_size, 1)
        plain_vector = np.dot(inv_key_matrix, cipher_vector) % 26
        plaintext += "".join([num_to_char(num) for num in plain_vector])

    label_plaintext["text"] = "Plaintext: " + plaintext


# Create Tkinter window
window = tk.Tk()
window.title("Hill Cipher")

# Create labels
label_plaintext = tk.Label(window, text="Plaintext:")
label_plaintext.grid(row=0, column=0, pady=5)

label_key = tk.Label(window, text="Key:")
label_key.grid(row=1, column=0, pady=5)

label_ciphertext = tk.Label(window, text="Ciphertext:")
label_ciphertext.grid(row=2, column=0, pady=5)

# Create entry fields
entry_plaintext = tk.Entry(window)
entry_plaintext.grid(row=0, column=1, pady=5)

entry_key = tk.Entry(window)
entry_key.grid(row=1, column=1, pady=5)

entry_ciphertext = tk.Entry(window)
entry_ciphertext.grid(row=2, column=1, pady=5)

# Create buttons
button_encrypt = tk.Button(window, text="Encrypt", command=hill_cipher_encrypt)
button_encrypt.grid(row=3, column=0, pady=10)

button_decrypt = tk.Button(window, text="Decrypt", command=hill_cipher_decrypt)
button_decrypt.grid(row=3, column=1, pady=10)

# Run the Tkinter event loop
window.mainloop()
