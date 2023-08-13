def xor_encrypt(text):
    encrypted = bytearray()
    for i in range(len(text)):
        encrypted.append(text[i] ^ 1)
    return encrypted
def xor_decrypt(encrypted):
    decrypted = bytearray()
    for i in range(len(encrypted)):
        decrypted.append(encrypted[i] ^ 1)
    return decrypted

plaintext = "Ziyad"
#encryption_key = b"mykey"

encrypted_data = xor_encrypt(plaintext.encode())
hex_encrypted = encrypted_data.hex()
print("Encrypted: ",encrypted_data )
print("Hexadecimal:", hex_encrypted)

decrypted_data = xor_decrypt(encrypted_data)
hex_decrypted = decrypted_data.hex()
print("Decrypted: ",decrypted_data.decode())
print("Hexadecimal:", hex_decrypted)
