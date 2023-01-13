print("Type 'encode' to encrypt and 'decode' to decrypt:")
userin = input()
print("Type your message : ")
message = input()
print("Type the shift number : ")
num = int(input())
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encode(userinput,shiftnum):
    coded = ""
    for letter in userinput:
        pos = alphabet.index(letter)
        newpos = pos + shiftnum
        coded += alphabet[newpos]
    print("Here is your encoded result : %s" % coded)
def decode(userinput,shiftnum):
    coded = ""
    for letter in userinput:
        pos = alphabet.index(letter)
        newpos = pos - shiftnum
        coded += alphabet[newpos]
    print("Here is your decoded result : %s" % coded)
if userin == "encode":
    encode(message, num)
else:
    decode(message,num)
def cipher(messaged,shiftnum,userinput):
    coded = ""
    for letter in userinput:
        pos = alphabet.index(letter)
        if userinput == "decode":
            shiftnum *= -1
        newpos = pos + shiftnum
        coded += alphabet[newpos]
    print("Here is your result : %s" % coded)
def encode(userinput,shiftnum):
    coded = ""
    for letter in userinput:
        pos = alphabet.index(letter)
        newpos = pos + shiftnum
        coded += alphabet[newpos]
    print("Here is your encoded result : %s" % coded)
def decode(userinput,shiftnum):
    coded = ""
    for letter in userinput:
        pos = alphabet.index(letter)
        newpos = pos - shiftnum
        coded += alphabet[newpos]
    print("Here is your decoded result : %s" % coded)
cipher(message,num,userin)