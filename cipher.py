string = input("Enter the message you'd like to encrypt: ")
offset = int (input ("Enter how much you would like to offset by: "))
while offset>26:
    offset = int (input ("offset too big, try again: "))
i = 0
newstr = ""

while i<len(string):
    if (ord(string[i])>64 and ord(string[i])<=90):
        char=ord(string[i])+offset
        if not(char>64 and char<=90):
            if offest < 0:
                char= ord(char)-26
            else:
                char= ord(char)+26
    elif (ord(string[i])>96 and ord(string[i])<=122):
        char=ord(string[i])+offset
        if not(char>96 and char<=122):
            if offest < 0:
                char= ord(char)-26
            else:
                char= ord(char)+26
    else:
        char=ord(string[i])
    newstr= newstr + chr(char)    
    i+=1

print("Your encrypted message is "+ newstr)
