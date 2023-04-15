from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()

# Create a Fernet object with the key
fernet = Fernet(key)

# Function to encode text
def encode_text(text, fernet):
    encoded_text = fernet.encrypt(text.encode())
    return encoded_text

# Function to decode text
def decode_text(encoded_text, fernet):
    decoded_text = fernet.decrypt(encoded_text)
    return decoded_text.decode()

# Get input from user
text = input("Enter text to encode: ")

# Encode input text
encoded_text = encode_text(text, fernet)
print("Encoded text: ", encoded_text)

# Decode encoded text
decoded_text = decode_text(encoded_text, fernet)
print("Decoded text: ", decoded_text)