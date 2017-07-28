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
    strList = [
    'Created new vouche id',
    "NEW_SALES_DATA",
    "FreshInputFragment requested VoucheId",
    "Stub::IAccountingRPC:doDwindling:",
    "doInPaymentWithCurrencies",
    "doOutPaymentWithCurrencies",
    "doClosePaymentWithCurrencies",
    "BillingBillFragment requested VoucheId:",
    "ConfirmDialog requested VoucheId:",
    "BillingArticlesFragment requested VoucheId:",
    "BillingPaymentFragment requested VoucheId: "
    ]


    bl_hit = False

    if in_str.find(strList) > 0:
        bl_hit = True

    if bl_hit == True:  return in_str
    if bl_hit == False: return ""


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

    # Reading File/s
    print " " + item
    finPath = path+"\\"+item
    fopen = open(finPath ,'r')

    # Accessing Data
    data = fopen.readlines();
    lineCount = len(data)
    fopen.close()

    # Start Verarbeitung
    print "VERARBEITUNG >> "

    # Anlage tempListe
    outList = []

    # Verarbeitung
    for line in data:
        output = findHIT(line.rstrip())
        if len(output) > 0:
            outList.append(output)


    print "Liste hat {} Eintraege".format(len(outList))
    c = 0                                       # Counter initiieren
    searchStr01 = 'Created new vouche id'       # SearchString initiieren

    for entry in outList:
        if c == 0:
            c = c + 1
            continue
        else:
            if outList[c].find(searchStr01) > 0 and outList[c-1].find(searchStr01) > 0:
                    print outList[c-1]
            c = c + 1



    print "Es wurden {} Zeilen verarbeitet\n".format(lineCount);

    print time.ctime() + " --- ENDE "



