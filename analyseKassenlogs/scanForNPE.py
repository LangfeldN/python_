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



def findNPE(in_str):
    searchStr01 = 'NullPointerException'
    searchStr02 = "Starting"


    if in_str.find(searchStr01) > 0:
        print(in_str)
    if in_str.find(searchStr02) > 0:
        print(in_str)



## START -------------------------------------------------------------------------------------------------
print time.ctime() + " --- START"

## LIST ALL FILES CONTAINING IN THE CURFOLDER
#path = "C:\Users\langfeldn\Desktop\WORK\PROJEKTE\LCB\ANIKA\ANALYSE\\20160622_v248_Kartenzahlung"
#path = 'C:\Users\langfeldn\Desktop\WORK\PROJEKTE\LCB\ANIKA\ANALYSE\\20160715 - B-Hbf-Kartenzahlung\ANALYSE'
path = raw_input('Bitte Ordner angeben!\n')


os.chdir(path)
curDir = os.getcwd();
fileList = os.listdir(curDir);

print "\n{} Dateien gefunden".format((len(fileList)))
# ---------------------------------------------------------------------------------------------------------

for item in fileList:
    print " " + item
    finPath = path+"\\"+item
    fopen = open(finPath ,'r')
    data = fopen.readlines();
    lineCount = len(data)
    fopen.close()
    print "VERARBEITUNG >> "


    for line in data:
        findNPE(line.rstrip())

    print "Es wurden {} Zeilen verarbeitet\n".format(lineCount);

    print time.ctime() + " --- ENDE "



