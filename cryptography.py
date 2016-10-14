"""
cryptography.py
Author: Bauti G
Credit: Liam S.

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
redo="yes"

while redo == "yes":
    letter=str(input("Enter e to encrypt, d to decrypt, or q to quit: "))
    if letter == "e":
        message=input("message: ")
        key=input("key: ")
        redo = "yes"
    elif letter == "d":
        message=input("message: ")
        key=input("key: ")
        redo = "yes"
    elif letter == "q":
        print("Goodbye!")
        redo = "no"
    else:
        print("Did not understand command, try again."))
        redo = "yes"