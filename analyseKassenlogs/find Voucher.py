

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
kasseIndex = 0;
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
            if not voucherDict.has_key( voucherID ):
                voucherDict[voucherID] = ['','',''];
            voucherDict[voucherID][ kasseIndex ] = 'X';
            #print voucherDict

    fopen.close()
    kasseIndex += 1
    print kasseIndex



for entry in voucherDict:
    print "{} \t  {}".format(entry,voucherDict[entry])



#"rpcmethod":"DO_FRESH_POST"

#   - Obtained SELL_SALES_VOUCHER:
#   - parsing message type: STORNO_SALE_VOUCHER
#   - parsing message type: DO_FRESH_POST
#   - parsing message type: DO_DWINDLING
#   - parsing message type: DO_FRESH_FRACTION_DWINDLING
