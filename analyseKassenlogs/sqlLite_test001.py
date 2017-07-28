
import sqlite3
import sys
import time

# print time.ctime() + "--- import sqlite3 - success"
# print time.ctime() + "--- import sys - success"
# print time.ctime() + "--- import time - success"


con = None
inPath = "C:\Users\langfeldn\Desktop\TEMP\\20170104 - Jungfernstieg\\"
inFile = "v67_k1.db"
inMain = inPath + inFile

print inFile

## SELECTS
sel_1 = "SELECT Reason, sum(LCOUNT_Numerator), sum(LCOUNT_denominator),count(*) FROM FRESH_COUNTS group by REASON;"
sel_2 = "SELECT datetime(substr(creation_time,1,10), 'unixepoch') , datetime(substr(timeofinput,1,10), 'unixepoch') , *  FROM FRESH_COUNTS order by timeofinput;"
sel_3 = "SELECT datetime(substr(creation_time,1,10), 'unixepoch') , datetime(substr(timeofinput,1,10), 'unixepoch') , *  FROM FRESH_COUNTS WHERE REASON = 'ADD_STORNO' order by timeofinput;"
sel_4 = "SELECT count(*) , Reason  FROM FRESH_COUNTS group by REASON;"
sel_5 = "SELECT datetime(substr(creation_time,1,10), 'unixepoch') , datetime(substr(timeofinput,1,10), 'unixepoch') , *  FROM FRESH_COUNTS WHERE REASON = 'DWINDLING' order by timeofinput;"
sel_6 = "SELECT datetime(substr(creation_time,1,10), 'unixepoch') , datetime(substr(timeofinput,1,10), 'unixepoch') , *  FROM FRESH_COUNTS WHERE REASON = 'NVKWARE' order by timeofinput;"
sel_7 = "select ITEM_ID, ITEM_Number, NAME_Real from ART_SALES_ITEM_HIST where ITEM_ID in (2123, 1221, 1141, 308) ;"
sel_8 = "SELECT LARTICLEID,  LCOUNT_NUMERATOR,  LCOUNT_DENOMINATOR,  REASON,  CREATION_TIME,  TIMEOFINPUT,  VOUCHER_ID,  CANCELED_VOUCHER_ID,  POSITION,  CASH_NO,  ISRESETCOUNT,  LREALARTIKELID FROM FRESH_COUNTS f1 WHERE f1.REASON NOT IN ('ADD_STORNO','SELL_STORNO') AND f1.VOUCHER_ID NOT IN( SELECT  CANCELED_VOUCHER_ID FROM FRESH_COUNTS f2 WHERE f2.REASON IN ('ADD_STORNO','SELL_STORNO') AND CANCELED_VOUCHER_ID IS NOT NULL ) ORDER BY CREATION_TIME ASC ; "

try:
    con = sqlite3.connect(inMain)

    useSelect = sel_3
    print useSelect

    cur = con.cursor()
    cur.execute(useSelect)

    data = cur.fetchall()
    for entry in data: print entry
##    for entry in data: print entry[1] + " ... " + entry[8] + " ... {} ".format(entry[13])

except sqlite3.Error, e:
    print "Error %s:" % e.args[0]
    sys.exit(1)

finally:
    if con: con.close()


