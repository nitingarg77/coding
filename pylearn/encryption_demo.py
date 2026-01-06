import random
import string

chars = " " +string.punctuation + string.ascii_letters + string.digits

chars = list(chars)
key = chars.copy()
random.shuffle(key)


print(f"chars : {chars}")
print(f"key : {key}")

#Encryption
plain_text = input("Enter plain text: ")
cipher_text = ""
for ch in plain_text:
    index = chars.index(ch)
    cipher_text += key[index]   
print(f"Cipher Text: {cipher_text}")


#Decryption
cipher_text = input("Enter cipher text: ")
plain_text = ""
for ch in cipher_text:
    index = key.index(ch)
    plain_text += chars[index]   
print(f"Plain Text: {plain_text}")
