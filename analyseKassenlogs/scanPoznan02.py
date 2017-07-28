### ------------------------------------------------------------------------
##      SCAN4NPE.PY
##      - mit diesem Skript soll eine Reihe von Dateien gescannt werde
##      - Es soll ermittelt werden, ob und wann eine NPE aufgetreten ist
##      - Zusaetzlich soll f?r das Logfile der Shop und die jeweilige Kasse ermittelt werden
### ------------------------------------------------------------------------

## IMPORT
import time
import os

## METHODEN



def findHIT(in_str):
    searchStr01 = 'Created new vouche id'
    searchStr02 = "NEW_SALES_DATA"
    searchStr03 = "FreshInputFragment requested VoucheId"
    searchStr04 = "Stub::IAccountingRPC:doDwindling:"
    searchStr05 = "doInPaymentWithCurrencies"
    searchStr06 = "doOutPaymentWithCurrencies"
    searchStr07 = "doClosePaymentWithCurrencies"
    searchStr08 = "BillingBillFragment requested VoucheId:"
    searchStr09 = "ConfirmDialog requested VoucheId:"


    if in_str.find(searchStr01) > 0:
        print(in_str)
    if in_str.find(searchStr02) > 0:
        print(in_str)
    if in_str.find(searchStr03) > 0:
        print(in_str)
    if in_str.find(searchStr04) > 0:
        print(in_str)
    if in_str.find(searchStr05) > 0:
        print(in_str)
    if in_str.find(searchStr06) > 0:
        print(in_str)
    if in_str.find(searchStr07) > 0:
        print(in_str)
    if in_str.find(searchStr08) > 0:
        print(in_str)
    if in_str.find(searchStr09) > 0:
        print(in_str)



## START -------------------------------------------------------------------------------------------------
print time.ctime() + " --- START"

## LIST ALL FILES CONTAINING IN THE CURFOLDER
path = raw_input('Bitte Ordner angeben!\n')


os.chdir(path)
curDir = os.getcwd();
fileList = os.listdir(curDir);

print "\n{} Dateien gefunden".format((len(fileList)))
# ---------------------------------------------------------------------------------------------------------

for item in fileList:
    print " " + item
    finPath = path+"\\"+item
    fopen = open(finPath ,'r')
    data = fopen.readlines();
    lineCount = len(data)
    fopen.close()
    print "VERARBEITUNG >> "


    for line in data:
        findHIT(line.rstrip())

    print "Es wurden {} Zeilen verarbeitet\n".format(lineCount);

    print time.ctime() + " --- ENDE "



