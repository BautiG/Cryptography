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
        
        keystring = key
        lengthkey=len(keystring)
        while lengthkey<lengthmessage:
            keystring=keystring+key
            lengthkey=len(keystring)
        while lengthkey>lengthmessage:
            keystring=keystring[:-1]
            lengthkey=len(keystring)
        
        numberkey=[]
        for char in keystring:
            numberkey.append(associations.find(char))
        
        sumlist=[]
        while number<lengthmessage:
            sumlist.append(numbermessage[number]+numberkey[number])
            number+=1
        number=0

        while number < lengthmessage:#if this dosn't work, change the numbers
            if sumlist[number]>84:
                sumlist[number]-=85
            number+=1
        
        number=0
        endlist=[]
        while number<lengthmessage:
            endlist.append(associations[sumlist[number]])
            number+=1
        print(''.join(endlist))

        redo = "yes"
    elif letter == "d":
        message=input("message: ")
        messagelist=list(message)
        key=input("key: ")
        keylist=list(key)
        numbermessage=[]
        lengthmessage = len(messagelist)
        for char in messagelist:
            numbermessage.append(associations.find(char))
        
        keystring = key
        lengthkey=len(keystring)
        while lengthkey<lengthmessage:
            keystring=keystring+key
            lengthkey=len(keystring)
        while lengthkey>lengthmessage:
            keystring=keystring[:-1]
            lengthkey=len(keystring)
        
        numberkey=[]
        for char in keystring:
            numberkey.append(associations.find(char))
        
        sumlist=[]
        while number<lengthmessage:
            sumlist.append(numbermessage[number]-numberkey[number])
            number+=1
        number=0

        while number < lengthmessage:#if this dosn't work, change the numbers
            if sumlist[number]<0:
                sumlist[number]+=85
            number+=1
        
        number=0
        endlist=[]
        while number<lengthmessage:
            endlist.append(associations[sumlist[number]])
            number+=1
        print(''.join(endlist))

        
        
        redo = "yes"
    elif letter == "q":
        print("Goodbye!")
        redo = "no"
    else:
        print("Did not understand command, try again.")
        redo = "yes"
