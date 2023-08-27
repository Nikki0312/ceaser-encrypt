def encrypt(encryptMessage,shift):
  for alpha in encryptMessage:
    ascii=ord(alpha)
    ascii=ascii+shift
    print(chr(ascii),end="")


message=input("Enter a message to encrypt: ")
shift_number=int(input("Enter a number to shift to encode: "))
encrypt(message,shift_number)
