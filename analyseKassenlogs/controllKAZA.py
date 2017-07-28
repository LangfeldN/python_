## Das Skript dient der Kontrolle der Kartenzahlung

# File einlesen
# Betraege raussuchen
# summieren


# 1)
import new
import os

# ---------------------------------------------------------------------
# 1) File einlesen - Dateien ermitteln
from cgitb import enable

os.chdir('C:\Users\langfeldn\Desktop\TEMP\\20170522 - B-Hauptbahnhof - KAZA')
dirList = os.listdir(os.getcwd())
newList = []

# hier filter wir die ZIPs raus und behalten die logdateien
for hit in dirList:
    if hit.find('.zip')<0:newList.append(hit)

print newList

# ---------------------------------------------------------------------
# 1.1) Dateien einlesen

print 'DATA READING > START'

fileobj = open(newList[0],'r')
data1 = fileobj.readlines()
fileobj.close()

fileobj = open(newList[1],'r')
data2 = fileobj.readlines()
fileobj.close()

print 'DATA READING > DONE'

# ---------------------------------------------------------------------
# 2) Betraege raussuchen

date = []
info = []
amount = []

for line in data1:
    line = line.rstrip()
    if line.find('INSERT OR REPLACE INTO CARD_PAYMENTPARTS') > 0:
        splitLine = line.split(',')
        info_ = splitLine[26]
        date_ = splitLine[0]
        amount_ = splitLine[27]

        # Bereingung INFO
        idx = info_.find('v')
        info_ = info_[idx:]

        # BEREINGUNG DATE
        date_ = date_[:19]

        date.append(date_)
        info.append(info_)
        amount.append(amount_)

        print "{} - {} - {}".format(date_,info_,amount_)

#allList = [[date],[info],[amount]]
#print allList
#allList.sort()
#print allList

c = 0;
for hit in splitLine:
    print "[{}]  - {}".format(c,hit)
    c = c + 1;
