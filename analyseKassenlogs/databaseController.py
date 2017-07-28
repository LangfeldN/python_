

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
voucherDict = {}

for entry in allList:
    if entry.find("database") <> -1 :
        print entry
        fileList.append(entry)

for entry in fileList:
    fullPath = path + '\\' + entry
    print "\n"+fullPath

    # dict

    # init counter
    c1 = c2 = c3 = c4 = c5 = 0

    fopen = open(fullPath,'r')
    data = fopen.readlines()
    for item in data:
        item = item.rstrip()

        if item.find("INSERT OR REPLACE INTO FRESH_COUNTS_ALL") > -1 :

            spItem = item.split(")::sql_params::[")
            sp001 = spItem[1].split(",")
            voucherID = sp001[6]
            voucherDict[voucherID] = (0,0,0)
            #print voucherDict

            if item.find("SELL") > -1:
                c1 = c1 + 1
            if item.find("DWINDLING") > -1:
                c2 = c2 + 1
            if item.find("ADD") > -1:
                c3 = c3 + 1
            if item.find("SELL_STORNO") > -1:
                print item
                c4 = c4 + 1
            if item.find("ADD_STORNO") > -1:
                c5 = c5 + 1


    print "{} - {}".format("SELL", c1)
    print "{} - {}".format("DWINDLING", c2)
    print "{} - {}".format("ADD", c3)
    print "{} - {}".format("SELL_STORNO", c4)
    print "{} - {}".format("ADD_STORNO", c5)

    fopen.close()


for entry in voucherDict:
    print entry



#"rpcmethod":"DO_FRESH_POST"

#   - Obtained SELL_SALES_VOUCHER:
#   - parsing message type: STORNO_SALE_VOUCHER
#   - parsing message type: DO_FRESH_POST
#   - parsing message type: DO_DWINDLING
#   - parsing message type: DO_FRESH_FRACTION_DWINDLING
