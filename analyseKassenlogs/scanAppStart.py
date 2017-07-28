### ------------------------------------------------------------------------
##      SCAN4NPE.PY
##      - mit diesem Skript soll eine Reihe von Dateien gescannt werde
##      - Es soll ermittelt werden, ob und wann eine NPE aufgetreten ist
##      - Zusaetzlich soll f?r das Logfile der Shop und die jeweilige Kasse ermittelt werden
### ------------------------------------------------------------------------

## IMPORT
import time
import os

## METHODEN



def findAppStart(in_str):
    searchStr01 = 'NullPointerException'
    searchStr02 = "Starting"

    #if in_str.find(searchStr01) > 0:
        #print(in_str)
        #return in_str
    if in_str.find(searchStr02) > 0:
        #print(in_str)
        return in_str

def genPrevString(input):
    strSplit = input.split(' ')
    strDate00 = strSplit[0]
    dateSplit = strDate00.split('.')
    strDate01 = dateSplit[2] + dateSplit[1] + dateSplit[0] + ' ' + strSplit[1]
    strOut = strDate01 + ' ' + input
    return strOut

## START -------------------------------------------------------------------------------------------------
print time.ctime() + " --- START"

## LIST ALL FILES CONTAINING IN THE CURFOLDER
#path = "C:\Users\langfeldn\Desktop\WORK\PROJEKTE\LCB\ANIKA\ANALYSE\\20160622_v248_Kartenzahlung"
#path = 'C:\Users\langfeldn\Desktop\WORK\PROJEKTE\LCB\ANIKA\ANALYSE\\20160715 - B-Hbf-Kartenzahlung\ANALYSE'
path = raw_input('Bitte Ordner angeben:\t\t\t')

os.chdir(path)
curDir = os.getcwd();
fileList = os.listdir(curDir);

print "\n{} Dateien gefunden".format((len(fileList)))
# ---------------------------------------------------------------------------------------------------------

output = []
for item in fileList:

    finPath = path+"\\"+item
    fopen = open(finPath ,'r')
    data = fopen.readlines();
    lineCount = len(data)
    fopen.close()

    for line in data:
        if findAppStart(line.rstrip()) is not None:
            dat00 = findAppStart(line.rstrip())
            dat01 = genPrevString(dat00)
            output.append(dat01)

output.sort();

for element in output:
    if element is not None:
        print element

print time.ctime() + " --- ENDE "

