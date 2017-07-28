### ------------------------------------------------------------------------
##      OPENFILE.PY
##      - dient dazu eine Datei einzulesen
##      - Am Ende soll ausgegeben werden, wie viele Zeile gelesen wurden
### ------------------------------------------------------------------------

## IMPORT
import time
import os

## START
print time.ctime() + " --- START"

## LIST ALL FILES CONTAINING IN THE CURFOLDER
path = "C:\Users\langfeldn\Desktop\WORK\PROJEKTE\LCB\ANIKA\ANALYSE\\20160622_v248_Kartenzahlung"
os.chdir(path)
curDir = os.getcwd();
fileList = os.listdir(curDir);

print "\n{} Dateien gefunden".format((len(fileList)))

for item in fileList:
    print " " + item

## CHOOSE FILE
choice = raw_input("\nBitte eine Datei angeben.  ")

## CREATE FINAL FILEPATH
finPath = path+"\\"+choice

## OPEN FILE
fopen = open(finPath ,'r')

## READ LINES
data = fopen.readlines();
lines = len(data)

## PRINT RESULT
print "Es wurden {} Zeilen eingelesen\n".format(lines);


## ENDE
print time.ctime() + " --- ENDEs"



