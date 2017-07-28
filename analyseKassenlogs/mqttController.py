

## Einlesen der Files

import os
import time


path = raw_input("Working Directory:\n")
os.chdir(path)
if path == os.getcwd(): print "success"
    ### perfekt bis hier laeuft es

## Dateien ermitteln
allList = os.listdir(path)
fileList = []

for entry in allList:
    if entry.find("mqtt") <> -1 :
        print entry
        fileList.append(entry)

for entry in fileList:
    fullPath = path + '\\' + entry
    print "\n"+fullPath

    # init counter
    c1 = c2 = c3 = c4 = c5 = 0

    fopen = open(fullPath,'r')
    data = fopen.readlines()
    for item in data:
        item = item.rstrip()
        if item.find("MessageArrived") > -1 :
            if item.find("STORNO_SALE_VOUCHER") > -1:
                c1 = c1 + 1
            if item.find("DO_FRESH_POST") > -1:
                c2 = c2 + 1
            if item.find("DO_DWINDLING") > -1:
                c3 = c3 + 1
            if item.find("DO_FRESH_FRACTION_DWINDLING") > -1:
                c4 = c4 + 1
            if item.find("SELL_SALE_VOUCHER") > -1:
                c5 = c5 + 1


    print "{} - {}".format("SELL_SALES_VOUCHER", c5)
    print "{} - {}".format("STORNO_SALE_VOUCHER", c1)
    print "{} - {}".format("DO_FRESH_POST", c2)
    print "{} - {}".format("DO_DWINDLING", c3)
    print "{} - {}".format("DO_FRESH_FRACTION_DWINDLING", c4)

    fopen.close()

#"rpcmethod":"DO_FRESH_POST"

#   - Obtained SELL_SALES_VOUCHER:
#   - parsing message type: STORNO_SALE_VOUCHER
#   - parsing message type: DO_FRESH_POST
#   - parsing message type: DO_DWINDLING
#   - parsing message type: DO_FRESH_FRACTION_DWINDLING
