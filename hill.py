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

def hill_cipher_encrypt(plaintext, key):
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

    return ciphertext

def hill_cipher_decrypt(ciphertext, key):
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

    return plaintext

# Example usage
# You can change the data to encrypt/decrypt as you like
plaintext = "HELLO"
key = "GYBNQKURP"

encrypted_text = hill_cipher_encrypt(plaintext, key)
print("Encrypted Text:", encrypted_text) 

decrypted_text = hill_cipher_decrypt(encrypted_text, key)
print("Decrypted Text:", decrypted_text)

"""
Note:
In the Hill cipher, the key matrix determines the encryption and decryption process. 
When you use the key "GYBNQKURP" and encrypt the plaintext "HELLO", the resulting ciphertext is "TFJJZX". 
Then, when you decrypt the ciphertext using the same key, you should obtain the original plaintext "HELLO" again.

The output "SGVsbG8sIFdvcmxkIQ" is the Base64 encoding of the string "Hello, World!" 
but is not directly related to the Hill cipher encryption and decryption.
"""
