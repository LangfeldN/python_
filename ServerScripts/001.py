# Lesen
# Auswerten

# FileToRead = f2r

import time

#['16:42:01.603', '[qtp251210093-76005]', 'TRACE', 'AndroidServer.base', '-', 'Verkauf', 'v3:', 'Inside', 'SaleRPCRequestHandler::process', 'Method:getSalesVoucherSinceWithCurrenciesV3', 'Params:Class:class', 'com.schiffl.androidcash.common.anikabeans.CashIdentBean', 'toString:618:4', ',', 'Class:class', 'java.lang.Long', 'toString:1923839753', ',', 'Class:class', 'com.schiffl.androidcash.common.anikabeans.TimeStampBean', 'toString:2016.11.10', '12:00:00', ',', '\n']
#['16:42:13.228', '[qtp251210093-76236]', 'TRACE', 'DataLayer_Oracle-104', '-', 'ORACLE-DB:', 'Inside', 'DataLayer_Oracle::setAktiveModul(', '104,', '2,', 'Haupmenu)\n']


def hit01(input):
    string.split()

# START
print time.ctime() + " - START"

f2r = "C:\Users\langfeldn\PycharmProjects\ServerScripts\data\\20161111_001\\2016_11_11.stdout.log";
c = 0;      # COUNTER

fopen = open(f2r, 'r');
data = fopen.readlines();
fopen.close()

# Alle Daten lesen
for item in data:
    c = c + 1;
print "{} Zeilen gelesen".format(c);

# Einfuehrung von Suchstrings
searchStr01 = ' Method:getSalesVoucherSince';
searchStr02 = 'ORACLE-DB: Inside DataLayer_Oracle::setAktiveModul(';

# Processing
for item in data:
    item.rstrip();

    if item.find(searchStr01) > 0:
        #print item
        dat1 = item.split(' ');
        shop = dat1[12].split(':')[1]
        knr = dat1[12].split(':')[2]
        print "OR: {} {}/{}".format(dat1[0], shop, knr)

    if item.find(searchStr02)>0:
        if item.find('Haupmenu') > 0:
            dat2 = item.split(' ')
            print "HM: {} {}/{}".format(dat2[0], dat2[8].split(',')[0], dat2[9].split(',')[0])


#print dat1[0]

# funzt ... Augabe bei Hauptmenue funzt
#print "{} {}/{}".format(dat2[0], dat2[8].split(',')[0], dat2[9].split(',')[0])

# ENDE
print time.ctime() + " - FINISH"