from Crypto.Cipher import AES
import os

def encrypt_file(filename, key):
    cipher = AES.new(key, AES.MODE_EAX)
    with open(filename, 'rb') as f:
        data = f.read()
    ciphertext, tag = cipher.encrypt_and_digest(data)
    with open(filename + ".enc", 'wb') as f:
        [f.write(x) for x in (cipher.nonce, tag, ciphertext)]
    print("✅ File encrypted successfully!")

def decrypt_file(filename, key):
    with open(filename, 'rb') as f:
        nonce, tag, ciphertext = [f.read(x) for x in (16, 16, -1)]
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    with open(filename[:-4], 'wb') as f:
        f.write(data)
    print("✅ File decrypted successfully!")

key = b'ThisIsASecretKey'  # 16 bytes key

print("1. Encrypt file")
print("2. Decrypt file")
choice = input("Enter your choice: ")

if choice == '1':
    fname = input("Enter file name to encrypt: ")
    encrypt_file(fname, key)
elif choice == '2':
    fname = input("Enter .enc file to decrypt: ")
    decrypt_file(fname, key)
else:
    print("Invalid choice!")
