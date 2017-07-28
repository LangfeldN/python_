# diese Skript soll eine Datei / mehrere Dateien so umbenennen, dass sie eindeutig unterscheidbar sind.

# 1) File suchen
# 2) File oeffnen
# 3) File auslesen
# 4) Info zu Shop und Kasse finden
# 5) Info zu Start und Ende des Logs finden
# 6) neuen File schreiben im Format
#           v###_k##_yyyymmddhhminss_yyyymmddhhminss.txt

# und los



# -- IMPORT ---------------------------------------------------------------

import time
import os

# -- METHODEN -------------------------------------------------------------

def log(text):
    print time.ctime() + ' --- ' + text


# -- MAIN -----------------------------------------------------------------

log('MAIN - START -------------------------------------')

## 1) File suchen ---------------------------------------------------------
log('Verzeichniswechsel - START')
wohin = raw_input("\tPfad angeben:\t")
os.chdir(wohin)
if wohin == os.getcwd(): log('SUCCESS')
log('Verzeichniswechsel - ENDE')

log('Dateisuche - START')
fileList = os.listdir(wohin)
fileList_new = []

for file in fileList:
    if file.find('.txt')>-1:
        if file.find('Log') > -1:
            fileList_new.append(file)

print "\t{} Logfiles gefunden".format(fileList_new.__len__())
log('Dateisuche - ENDE')


## 2) File oeffnen --------------------------------------------------------
log('Datei oeffnen - START')

file = fileList_new[0];

# ab hier kann das Thema in eine Methode ausgelagert werden --------------------------------------------------
fobj = open(file,'r')

## 3) File auslesen -------------------------------------------------------
log('Daten speichern - START')
data = fobj.readlines()             # alle Zeile in data
log('Daten speichern - ENDE')
fobj.close()
log('Datei oeffnen - ENDE')


## 4) Info zu Shop und Kasse finden ---------------------------------------
## Created new vouche id: v201_k3_535

log('Shop- und Kasseninfos finden - START')
hit_ = ""

for hit in data:
    hit = hit.rstrip()
    if hit.find('Created new vouche id: v') > 0:
        hit_ = hit

        idx = hit_.find(': v')
        hit_ = hit_[idx+2:]

vkeka_info = hit_
idx = vkeka_info.find('_')
idx = vkeka_info.find('_', idx+1)
vkeka_info = vkeka_info[:idx+1]

print '\tErgebnis: ' + vkeka_info
log('Shop- und Kasseninfos finden - ENDE')

## 5) Info zu Start und Ende des Logs finden ------------------------------
# fuer Start und Ende brauchen wir ja eigentlich nur die erste und letzte Zeile

log('Start und Ende finden - START')

start = data[0]
ende = data[data.__len__()-1]

# folgende Variablen brauchen wir somit
year = ""
month = ""
day = ""
hour = ""
minute = ""
second = ""

day = start[0:2]
#print day
month = start[3:5]
#print month
year = start[6:10]
#print year
hour = start[11:13]
#print hour
minute = start[14:16]
#print minute
second = start[17:19]
#print second

#print day + month + year + hour + minute + second
start_ = day + month + year + hour + minute + second
#print  'START ' + start_

day = ende[0:2]
#print day
month = ende[3:5]
#print month
year = ende[6:10]
#print year
hour = ende[11:13]
#print hour
minute = ende[14:16]
#print minute
second = ende[17:19]
#print second

#print day + month + year + hour + minute + second
ende_ = day + month + year + hour + minute + second
#print  'ENDE ' + ende_

log('Start und Ende finden - ENDE')

# 6) neuen File schreiben im Format --------------------------------------

log('Neuen Filenamen erzeugen - START')
newFileName = vkeka_info + start_ + '_' + ende_ + '_Log.txt'
log('Neuen Filenamen erzeugen - ENDE')

# os.path.join(path, filename)
oldFileName = os.path.join(os.getcwd(),file)
newFileName = os.path.join(os.getcwd(),newFileName)

log('Neuen File speichern - START')
# os.rename(newFileName, oldFileName)             # das hier hat nicht funktioniert sicher wegen den Klammern oder derartigen Zeichen

## os.path.isfile('C:\Users\langfeldn\Desktop\TEMP\test\v236_k2_07052017091139_18052017141206_Log.txt')

#print os.path.isfile(oldFileName)
#print os.path.isfile(newFileName)

if os.path.isfile(newFileName) == True:
    print "\t File {} existiert bereits. Es wurde nichts unternommen.".format(newFileName)

if os.path.isfile(newFileName) == False:
    fopen_new = open(newFileName,'w')
    fopen_new.writelines(data)
    fopen_new.close()
    print "\t File {} existiert noch nicht. Die Datei wurde angelegt".format(newFileName)
    os.remove(oldFileName)
    print "\t File {} wurde entfernt".format(oldFileName)

log('Neuen File speichern - ENDE')





## FINALE
log('MAIN - ENDE -------------------------------------')

