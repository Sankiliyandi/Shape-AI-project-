import hashlib
message=input("Enter the message:")
result=hashlib.md5(message.encode())
print("Encrypted message in byte equivalent of hash:",result.digest())
print("Encrypted message in hexadecimal equivalent of hash:",result.hexdigest())