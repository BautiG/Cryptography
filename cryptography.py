"""
cryptography.py
Author: Bauti G
Credit: Liam S., Vinzent

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
redo="yes"
number=0

while redo == "yes":
    letter=str(input("Enter e to encrypt, d to decrypt, or q to quit: "))
    if letter == "e":
        message=input("message: ")
        messagelist=list(message)
        key=input("key: ")
        keylist=list(key)
        numbermessage=[]
        lengthmessage = len(messagelist)
        for char in messagelist:
            numbermessage.append(associations.find(char))

        numberkey=[]
        for char in keylist:
            numberkey.append(associations.find(char))

        sumlist=[]
        while number<lengthmessage:
            sumlist.append(numbermessage[number]+numberkey[number])
            number+=1
        print(sumlist)
        redo = "yes"
    elif letter == "d":
        message=input("message: ")
        messagelist=list(message)
        key=input("key: ")
        keylist=list(key)
        redo = "yes"
    elif letter == "q":
        print("Goodbye!")
        redo = "no"
    else:
        print("Did not understand command, try again.")
        redo = "yes"
"""
numbermessage=[]
for char in messagelist:
    numbermessage.append(associations.find(char))
print(numbermessage)

numberkey=[]
for char in keylist:
    numberkey.append(associations.find(char))
print(numberkey)

lengthmessage = len(numbermessage)
sumlist=[]
while number<lengthmessage:
    sumlist.append(numbermessage[number]+numberkey[number])
    number+=1
"""