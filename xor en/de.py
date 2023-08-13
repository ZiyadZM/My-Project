def xor_encrypt(text, key):
    encrypted = bytearray()
    for i in range(len(text)):
        encrypted.append(text[i] ^ key[i % len(key)])
    return encrypted
def xor_decrypt(encrypted, key):
    decrypted = bytearray()
    for i in range(len(encrypted)):
        decrypted.append(encrypted[i] ^ key[i % len(key)])
    return decrypted

plaintext = "Ziyad"
encryption_key = b"mykey"

encrypted_data = xor_encrypt(plaintext.encode(), encryption_key)
hex_encrypted = encrypted_data.hex()
print("Encrypted: ",encrypted_data )
print("Hexadecimal:", hex_encrypted)

decrypted_data = xor_decrypt(encrypted_data, encryption_key)
hex_decrypted = decrypted_data.hex()
print("Decrypted: ",decrypted_data.decode())
print("Hexadecimal:", hex_decrypted)
