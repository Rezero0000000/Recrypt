# Base64 character table
base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def base64_encode(data):
    encoded_data = ""
    padding = 0

    # Process each three bytes of input data
    for i in range(0, len(data), 3):
        # Get three bytes of data
        chunk = data[i:i+3]
        
        # Convert three bytes to binary form
        binary_chunk = "".join(format(byte, '08b') for byte in chunk)
        
        # Divide three bytes into four groups of six bits
        groups = [binary_chunk[j:j+6] for j in range(0, len(binary_chunk), 6)]
        
        # Add padding if the number of bytes is less than three
        padding = 3 - len(chunk)
        if padding > 0:
            groups[-1] = groups[-1] + ("0" * padding * 2)
        
        # Convert six-bit groups to Base64 characters
        encoded_chunk = [base64_chars[int(group, 2)] for group in groups]
        encoded_data += "".join(encoded_chunk)
    
    return encoded_data


def base64_decode(encoded_data):
    decoded_data = b""
    padding = 0

    # Remove padding characters if present
    encoded_data = encoded_data.rstrip("=")
    
    # Process each four Base64 characters
    for i in range(0, len(encoded_data), 4):
        # Get four characters
        chunk = encoded_data[i:i+4]
        
        # Convert Base64 characters to six-bit binary groups
        groups = [base64_chars.index(char) for char in chunk]
        binary_chunk = "".join(format(group, '06b') for group in groups)
        
        # Remove padding if present
        padding = chunk.count("=")
        if padding > 0:
            binary_chunk = binary_chunk[:-padding * 2]
        
        # Convert six-bit groups to original three-byte data
        bytes_chunk = [int(binary_chunk[j:j+8], 2) for j in range(0, len(binary_chunk), 8)]
        decoded_data += bytes(bytes_chunk)
    
    return decoded_data


# Example usage
# You can change the data to encode/decode as you like
data = "Hello, World!"
data_utf = data.encode()  # Convert to UTF-8 bytes

# Encoding
encoded_data = base64_encode(data_utf)
print(encoded_data)  # Output: 'SGVsbG8sIFdvcmxkIQ=='

# Decoding
decoded_data = base64_decode(encoded_data)
print(decoded_data.decode())  # Output: 'Hello, World!'
