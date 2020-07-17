def encrypt(secret, key):
  encrypted = ""
  for x in range(0, len(secret)):
    encrypted += chr(ord(secret[x])+key)
  return encrypted

def decrypt(encrypted, key):
  decrypted = ""
  for x in range(0, len(encrypted)):
    decrypted += chr(ord(encrypted[x])-key)
  return decrypted

print("Python Casear Cipher")
print("Enter a secret message");
secret = input()

print("Insert Key To Encrypt: ")
key = int(input())

encrypted_val = encrypt(secret,key)

print("Encrypted: " + encrypted_val )
print("Enter Key To Decrypt Cipher: ")

key = int(input())

print(decrypt(encrypted_val, key))
