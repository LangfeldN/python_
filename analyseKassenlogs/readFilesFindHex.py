### ------------------------------------------------------------------------
##      OPENFILE.PY
##      - hier soll eine Datei eingelesen werden, und die Stellen herausgesucht werden, die einen
##        HEX-String enthlaten
##      - Am Ende soll ausgegeben werden, wie viele Zeile gelesen wurden
### ------------------------------------------------------------------------

## IMPORT
import time
import os

## METHODEN


def hex2ascii(in_str):
    import binascii
    splitRes = in_str.split(' ');
    newString = ""          # neuen leeren String angelegt
    #list = [hex(06),hex('0F'),hex(29),hex('F0')]

    for element in splitRes:
        if element > hex(28) and element != list:
            try:
                if element != list:
                    hexStr = binascii.a2b_hex(element)
                    newString = newString + hexStr
            except TypeError:
                newString = newString + ''

    return newString



## START
print time.ctime() + " --- START"

## LIST ALL FILES CONTAINING IN THE CURFOLDER
#path = "C:\Users\langfeldn\Desktop\WORK\PROJEKTE\LCB\ANIKA\ANALYSE\\20160622_v248_Kartenzahlung"
#path = 'C:\Users\langfeldn\Desktop\WORK\PROJEKTE\LCB\ANIKA\ANALYSE\\20160715 - B-Hbf-Kartenzahlung\ANALYSE'
path = raw_input('Bitte Ordner angeben!\n')


os.chdir(path)
curDir = os.getcwd();
fileList = os.listdir(curDir);

print "\n{} Dateien gefunden".format((len(fileList)))

for item in fileList:
    print " " + item
    finPath = path+"\\"+item
    fopen = open(finPath ,'r')
    data = fopen.readlines();
    lines = len(data)
    fopen.close()
    print "VERARBEITUNG >> "
    searchStr = "Response starts with"
    searchStr1 = "F7 56 58 36 38 30 57 2E 53 45 43 43"
    cleanStr = ""

    for line in data:
        if line.find(searchStr) > 0 :
            if not line.find(searchStr1) > 0:
                #print line.rstrip()
                line =  line.rstrip()
                cleanStr = line.rsplit(":")[5]
                #print cleanStr
                tempStr = line.rsplit("com.")[0]
                print tempStr + "..." +  hex2ascii(cleanStr)

    print "Es wurden {} Zeilen verarbeitet\n".format(lines);

    print time.ctime() + " --- ENDEs"



