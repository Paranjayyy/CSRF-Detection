import secrets

def generate_hex_token(length):
    num_bytes = (length + 1) // 2
    random_bytes = secrets.token_bytes(num_bytes)
    hex_token = random_bytes.hex()
    return hex_token[:length]  
hex_token_48 = generate_hex_token(48)
print("Hexadecimal token (48 bits):", hex_token_48)
