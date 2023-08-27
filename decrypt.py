def decrypt(decryptMessage):
    for dec in decryptMessage:
        ascci=ord(dec)
        ascci=ascci-4
        print(chr(ascci),end="")


message=input("Enter your encrpted message: ")
decrypt(message)
