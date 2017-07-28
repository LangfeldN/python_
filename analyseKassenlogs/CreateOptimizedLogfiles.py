# Verarbeitung Logfiles

# ABLAUF - DETAIL -----------------------------
# 1) Logfile einlesen
# 2) Ermittlung von Shop und Kasse
#       > v201_k1
# 3) Ermittlung von Start und Ende
#       > 20170401103546_20170403030734
# 4) Speicherung des Logfiles unter dem neuen Namen
#       > v201_k1_20170401103546_20170403030734.txt


## IMPORT --------------------------------------------------
import time
import os
from distutils.ccompiler import new_compiler

## METHODEN ------------------------------------------------

## LOGGER
def log(text):
    print time.ctime() + ' --- ' + text

## SCANNER
def scanFile(fullFileName):
    fo = open(fullFileName,'r')
    data = fo.readlines()
    fo.close()
    id = extractID(data)
    time = extractTime(data)
    try:
        final = id + '_' + time
        return final
    except TypeError:
        return ''

# EXTRACTER TIME
def extractTime(data):
    times = []
    for entry in data:
        try:
            dataSplit = entry.split(' ')
            timestamp = dataSplit[0] + ' ' + dataSplit[1]
            #print timestamp          # Ausgabe funktioniert
            fTime = formatTimestamp(timestamp)
            #print fTime
            times.append(fTime)

        except IndexError:
            break

        t_start = times[0]
        t_end = times[times.__len__() - 1]
        extractedTime =  t_start + '_' + t_end
        return extractedTime

def formatTimestamp(timestampIn):
# hier bitte einen Zeitstempel in folgendem Format eingeben
# 15.05.2017 11:05:29:387

        tsSplit = timestampIn.split('.')
# Im ersten Schritt ziehen wir das Datum raus und wandeln es in yyyymmdd um
        dateOut = tsSplit[2].split(' ')[0]+tsSplit[1]+tsSplit[0]
# Im zweiten Schritt ziehen wir die Zeit raus und wandeln diese in HHMM um
        timeTemp = tsSplit[2].split(' ')[1]
        tempSplit = timeTemp.split(':')
        timeOut = tempSplit[0]+tempSplit[1]+tempSplit[2]
        return dateOut+timeOut

# EXTRACTER - ID
def extractID(data):
    hit00 = 0
    hit01 = 0
    hit02 = 0
    hit03 = 0

    for entry in data:
        entry = entry.rstrip()
        hit00 = entry.find('Created new vouche ')
        if hit00 > 0:
            hit01 = entry.find('v', hit00+15)
            newEntry = entry[hit01:]
            hit02 = newEntry.find('_')
            hit03 = newEntry[hit02+1:].find('_')
            id = newEntry[0:hit02+hit03+1]
            return id

def checkFileExist(searchPath, searchFile):
    fileList = os.listdir(searchPath)
    bool_exist = False
    for file in fileList:
        if file == searchFile:
            bool_exist = True
    return bool_exist


# --- MAIN ------------------------------------------

log('START')

str_cwd = os.getcwd()
print '\t Aktuelles Verezeichnis: ' + str_cwd

log('Verzeichniswechsel')

newPath = "C:\Users\langfeldn\Downloads"
os.chdir(newPath)
str_cwd = os.getcwd()
print '\t Aktuelles Verezeichnis: ' + str_cwd
if newPath == str_cwd: print '\t Success'

## Scannen nach Textdateien
log('Scannen nach Textdateien')
fileList = os.listdir(str_cwd)
new_fileList = []
logFileList = []
for file in fileList:
    if file.find('.txt') > 0 :
        new_fileList.append(str_cwd+'\\'+file)

log('Scannen nach Logdateien')
for file in new_fileList:
    if file.find('Log') > 0 :
        logFileList.append(file)

#newFileCollector = []
for logfile in logFileList:
    id = scanFile(logfile)
    if id.__len__() > 10:
        try:
            newFileName = id + '.txt'
            nfn = newPath + '\\' + newFileName
            if checkFileExist(newPath,newFileName)== True:
                print nfn
                print 'EXISTS'
            if checkFileExist(newPath, newFileName) == False:
                print nfn
                print 'NOT EXISTS'
                os.renames(logfile, nfn)

        except TypeError:
            break

print nfn
log('ENDE')