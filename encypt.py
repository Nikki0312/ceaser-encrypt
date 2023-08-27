def encrypt(encryptMessage):
  for alpha in encryptMessage:
    ascii=ord(alpha)
    ascii=ascii+4
    print(chr(ascii),end="")


message=input("Enter a message to encrypt: ")
encrypt(message)
