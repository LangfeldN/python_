## ----------------------------------------------------------------
##  Analyse von Kassenlogfiles
##  
## ----------------------------------------------------------------


## IMPORT ---------------------------------------------

import os
import time

## METHODE --------------------------------------------

def scanFile(infile, bool_print, 'out.txt'):
    fopen = open(infile, 'r')
    
    data = fopen.readlines();
    outStr = ''
    searchStr = "Created new vouche id"
    
    for line in data:
        if line.find(searchStr)>0:
            outStr = line
            res = outStr.split(':')
            if bool_print == True:
                print res[0] + ':' + res[1] + ':'+ res[2]+' ,' + res[5].rstrip('\n')
                
    fopen.close()

    

# SCAN - TEMP-ORDNER
print(time.ctime() + ' - - - START - - - - - - - - - - - - - -')

os.chdir("C:\\Users\\langfeldn\\Desktop\\TEMP")
dirList = os.listdir("C:\\Users\\langfeldn\\Desktop\\TEMP")

c0 = 0;
for f in dirList:
    c0 = c0 + 1;

fout = open('out.txt','w')

print(str(c0) + " Dateien gefunden.")

c1 = 0
for f in dirList:
    scanFile(f, False)
    c1 = c1 + 1
    print ("Datei " + str(c1) + " von " + str(c0))
    fout.append(

fout.close();
print(time.ctime() + ' - - - ENDE - - - - - - - - - - - - - -')















