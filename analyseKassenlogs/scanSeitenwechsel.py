
## Dieses Script soll alle Dateien in einem Ordner scannen und auflisten

import os
import time


def log(text):
    import time
    print(time.ctime() + ' --- ' + text)

def changeDir():
    print ('Aktuelles Verzeichnis:\t\t\t' + os.getcwd())
    s_input = raw_input('Bitte Verzeichnis angeben:\t\t')
    os.chdir(s_input)
    print ('Aktuelles Verzeichnis:\t\t\t' + os.getcwd())
    return s_input

path = changeDir()
list_File = os.listdir(path)
ergStr = []

for item in list_File:
    #print item
    fpath = path + "\\" + item
    fopen = open(fpath,'r')
    data = fopen.readlines()
    fopen.close()

    for line in data:
        if line.find('setAktiveModul( 249,') > 0:
            line = line.rstrip()
            line = line.replace('T',' ')
            line = line.replace(',', '')
            split_ = line.split(' ')
            #print  split_
            ergStr.append(( split_[0], split_[1], split_[12], split_[13], split_[14], split_[15]))
            #print split_[0], split_[1], split_[12], split_[13], split_[14], split_[15]
            # print findata

ergStr.sort();

## Schreiben des Ergebnisses
outfile = path + "\\" + "out.txt"
fobj = open(outfile, 'w')

for item in ergStr:
    # print item
    fobj.write(item[0] + ',' + item[1] + ',' + item[2] + ',' + item[3] + ',' + item[4] + ',' + item[5]+ '\n')


fobj.close()

