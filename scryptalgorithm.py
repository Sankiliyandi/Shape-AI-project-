import scrypt
password=input("Enter passwrod:")
salt=b"48h6#N$HUB2#^&"
hashedpasswd=scrypt.hash(password,salt,N=1024,r=1,p=1,buflen=32)
print(hashedpasswd)