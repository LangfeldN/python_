# diese Skript dient dem Ablauf, dass das Serverlog in JSON geparst wird und aus dem resultierenden Objekt
# Update-Statements generiert werden

# 1) Open file

import json
import os

file = 'C:\Users\langfeldn\Documents\Meine empfangenen Dateien\prod.beleg.v-2017-06-01.log'

fopen = open(file,'r')
data = fopen.readlines()
fopen.close()

os.chdir('C:\Users\langfeldn\Documents\Meine empfangenen Dateien')
print os.getcwd()

fopen = open('out_update.txt','w')


for i in data:
    #print data[1]
    idx_start = data[1].find('[',1)
    idx_ende = data[1].find(']',idx_start)
    #print "hier"
    #print data[1][idx_start:idx_ende+1]
    fcontent = data[1][idx_start:idx_ende+1]

#file = 'C:\Users\langfeldn\Desktop\jsontest.txt'
#fopen = open(file,'r')
#fcontent = fopen.read()
#fopen.close()

#jsonObj = json.loads( '[{	"menge": "0",	"gposid": "1393806561",	"lposid": "106",	"artid": "1224",	"preis": "0",	"lvkpreis": "31790" }, {"menge": "0",	"gposid": "1393806629",	"lposid": "140",	"artid": "1461",	"preis": "0",	"lvkpreis": "11170"}]')

    jsonObj = json.loads(fcontent)


    #print jsonObj

    for entry in jsonObj:

        #'wasser'.replace('.','')
        gposid = entry['gposid']
        menge = entry['menge']
        menge = menge.replace('.', '').replace(',','.')
        #str_Select = "SELECT GPOSID, SARTIKEL, {} as MENGE_NEW, menge as MENGE_OLD FROM LCBDATA.V_AB_SONST WHERE GPOSID = {} \n UNION ".format(menge, gposid)
        #str_Select = "SELECT GPOSID, LVKEID, SARTIKEL, {} as MENGE_NEW, menge as MENGE_OLD FROM LCBDATA.V_AB_SONST WHERE GPOSID = {} \n UNION ".format(menge, gposid)
        str_update = "UPDATE LCBDATA.AB_SONST SET menge = {}, DAKTUALISIERUNGSDATUM = SYSTIMESTAMP  WHERE GPOSID = {};\n ".format(menge, gposid)
        #print str_Select

        #fopen.write(str_Select)
        fopen.write(str_update)

fopen.close()


