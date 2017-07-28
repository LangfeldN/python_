## SCAN INPUT LOG

import time, os
from dircache import listdir


def log(text):
    import time
    print(time.ctime() + ' --- ' + text)

def changeDir():
    print ('Aktuelles Verzeichnis:\t\t\t' + os.getcwd())
    s_input = raw_input('Bitte Verzeichnis angeben:\t\t')
    os.chdir(s_input)
    print ('Aktuelles Verzeichnis:\t\t\t' + os.getcwd())
    return s_input

## MAIN ---------------------------------------------------------------------------------

searchStr01 = 'InputDialog Button'
searchStr02 = 'FreshVoucherList'
searchStr03 = 'StornoDialog'

strings = ['InputDialog','FreshVoucherList','StornoDialog','GoodsSelectionFragment', 'VoucheHistoryFragmentDialog', 'Schwundauswahl' ]


#path = changeDir()
#list_File = os.listdir(path)                   -- erstmal eine einzelne Datei
filePath = 'C:\Users\langfeldn\Desktop\TEMP\\20170310 - Suedkreuz Kiosk\KASSE 1\input.log'


fopen = open(filePath, 'r')
data = fopen.readlines()
fopen.close()

for item in data:
    treffer = False

    for str in strings:
        if item.find(str) > 5:    treffer = True

    if treffer == False:
        print item.rstrip()





