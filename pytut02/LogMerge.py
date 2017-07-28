#!/usr/bin/python
# -*- coding: ascii -*-

##
# Dieses Skript dient dazu, Logs zu mergen

##  ABLAUF -----------------------------------------------
#   1) Beide Dateien laden
#   2) beide Dateien auslesen
#   3) beide Dateien in eine Liste schreiben
#   4) Liste nach Zeitstempel ordnen
#   5) Geordnete Liste in eine neue Datei schreiben


## -------------------------------------------------------
## IMPORT

from datetime import datetime
import os

f01 = 'C:\Users\langfeldn\Desktop\WORK\PROJEKTE\LCB\ANIKA\ANALYSE\\20160708-Chemnitz-Videoueberwachung\input.log'
f02 = 'C:\Users\langfeldn\Desktop\WORK\PROJEKTE\LCB\ANIKA\ANALYSE\\20160708-Chemnitz-Videoueberwachung\\video.log'
path = 'C:\Users\langfeldn\Desktop\WORK\PROJEKTE\LCB\ANIKA\ANALYSE\\20160708-Chemnitz-Videoueberwachung\\'

fopen01 = open(f01,'r')
fopen02 = open(f02,'r')

data01 = fopen01.readlines()
data02 = fopen02.readlines()

print "Zeilen: {}".format(len(data01))
print "Zeilen: {}".format(len(data02))

##  DATENVERARBEITUNG ----------------------------------------
data = data01 + data02                              # alle beiden Datens?tze mergen
#print "Zeilen: {}".format(len(data))

newList = []                    # Erzeugung einer leeren Liste
counter = 0
        # Schleife ?ber alle Elemente in der DATA
        # Zeilenumbruch mit rstrip entfernen
        # Element spliten
        # Datum umwandeln
        # Werte an Liste anh?ngen

for hit in data:
    test = hit.rstrip()
    try:
        temp = test.split(' [INFO] ')
        temp[0] = datetime.strptime(temp[0], '%Y-%m-%d %H:%M:%S.%f')
        newList.append(temp)
        counter = counter + 1
    except: continue

## SORTIERUNG ---------------------------------------------------------
newList.sort()

## VERZEICHNISWECHSEL -------------------------------------------------
os.chdir(path)

## AUSGABE ------------------------------------------------------------
outfile = path + 'out.txt'
fopen = open(outfile,'w')

for item in newList:
    # Formatierte Ausgabe  aller Werte
    fopen.write(item[0].strftime('%Y-%m-%d %H:%M:%S.%f') + ' ' + item[1] + '\n')

## DATEIEN SCHLIESSEN -------------------------------------------------
fopen.close()
fopen01.close()
fopen02.close()