
import sqlite3
import sys
import time
import os

# print time.ctime() + "--- import sqlite3 - success"
# print time.ctime() + "--- import sys - success"
# print time.ctime() + "--- import time - success"


def switchWS(wd):           # <<< PLEASE INSERT WORKINGDIRECTORY HERE
    os.chdir(wd)
    cwd = os.getcwd()
    dirList = os.listdir(cwd)
    fileList = []
    for f in dirList:
        if f.find('.db') > 0: fileList.append(cwd + '\\' + f)
    return fileList


def processDB(inFile):
    con = None
    sel = "SELECT count(*) , Reason  FROM FRESH_COUNTS group by REASON;"            ## FILL IN A SELECT IF NECESSARY
    try:
        con = sqlite3.connect(inFile)
        cur = con.cursor()
        cur.execute(sel)
        data = cur.fetchall()
    except sqlite3.Error, e:
        print "Error %s:" % e.args[0]
        sys.exit(1)
        data = []
    finally:
        if con: con.close()
        return data

## In weiser Vorraussicht, dass man vllt. auch mal Suedsteg analysieren
## muss, sollte man vllt. mal 7 dataStorages anlegen


data01 = []
data02 = []
data03 = []
data04 = []
data05 = []
data06 = []
data07 = []
c = 0                                                               # COUNTER
wd = 'C:\Users\langfeldn\Desktop\TEMP\\20161121_BremenTunnel'       # GRUNDLEGENDER ARBEITSBEREICH


fileList = switchWS(wd)

try:
    c = c + 1
    data01 = processDB(fileList[0])
    c = c + 1
    data02 = processDB(fileList[1])
    c = c + 1
    data03 = processDB(fileList[2])
    c = c + 1
    data04 = processDB(fileList[3])
    c = c + 1
    data05 = processDB(fileList[4])
    c = c + 1
    data06 = processDB(fileList[5])
    c = c + 1
    data07 = processDB(fileList[6])
except: print "Es wurden {} Datensaetze angelegt".format(c)
