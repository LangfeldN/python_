## IMPORT
import time
import os


## START
print time.ctime() + " --- START --- "

path = 'V:\LECROBAG\ABLAGE\SHOPS\LE CROBAG POZNAN [618]'
os.chdir(path)
curDir = os.getcwd();
fileList = os.listdir(curDir);

print " {} Dateien gefunden".format((len(fileList)))
searchStr01 = 'Created new vouche id:'
outFile = "out.txt"
fopenOut = open(outFile,'w')

for file in fileList:
    fopen = open(file,'r')                  # ?ffenen
    data = fopen.readlines()                # auslesen
    fopen.close()                           # schlie?en
    #print "Dokument ge?ffnet: {}".format(file)
    #print "{} Zeilen gelesen".format(len(data))
    c = 0

    for line in data:
        if line.find(searchStr01) > 0:
            c = c + 1
            fopenOut.write(line)
            fopenOut.write(data[c])
            fopenOut.write(data[c+1])
            fopenOut.write(data[c+2])




    #print "{} Treffer".format(c)
    print "Dokument: {} |  Zeilen: {}  |  Treffer {}".format(file,len(data),c)

fopenOut.close()
## START
print time.ctime() + " --- ENDE --- "



## NOTIZEN ---------------------------------------------------------------------------------
# NEW_SALES_DATA = 4008
# Created new vouche = 4282



