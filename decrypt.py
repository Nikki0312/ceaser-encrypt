def decrypt(decryptMessage,shift):
    for dec in decryptMessage:
        ascci=ord(dec)
        ascci=ascci-shift
        print(chr(ascci),end="")


message=input("Enter your encrpted message: ")
shift_number=int(input("Enter a shift number to decode: "))
decrypt(message,shift_number)
