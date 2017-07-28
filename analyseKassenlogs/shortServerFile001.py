
## IMPORT ------------------------------
import time
import os

def LOG(text):
    print time.ctime() + " --- " + text


## START
LOG("START")
## LIST ALL FILES CONTAINING IN THE CURFOLDER
path = "C:\Users\langfeldn\Desktop\WORK\PROJEKTE\LCB\ANALYSE"
f_path = "C:\Users\langfeldn\Desktop\WORK\PROJEKTE\LCB\ANALYSE\\File1.txt"
os.chdir(path)
curDir = os.getcwd();
## OPEN FILE
fopen = open(f_path ,'r')
## READ LINES
data = fopen.readlines();
lines = len(data)
## PRINT RESULT
print "Es wurden {} Zeilen eingelesen\n".format(lines);
## CLOSE FILE
fopen.close()


for entry in data:
    entry = entry.rstrip()
    split01 = entry.split(' ')
    print split01[0] + ' - ' + split01[13]

## c = 0;
## for entry in split01:
##     c = c + 1
##     print c.__str__() + ' - ' + entry

## ENDE
LOG("ENDE")