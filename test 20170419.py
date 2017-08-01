import os

def sub(inStr):
    strL = len(inStr)
    subString = inStr[0:strL - 8]
    print subString


print os.getcwd()

dirList = os.listdir(os.getcwd())

for item in dirList:
    sub(item)

# stringTest =  "Dateiname.EndungChecksum"


    


