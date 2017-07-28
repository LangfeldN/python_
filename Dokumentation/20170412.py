import os
import time


def log(text):
    str = '<p>' + time.ctime() + ' --- ' + text + '</p>'
    return str

def newParag(text):
    str = "<p>" + text + "</p>"
    return str

# Create file
TITEL = 'DOKUMENTATION - 20170412'

str = "<html><body>"
str = str + "<head><h1>" + TITEL + "</h1></head>"
str = str + log('Start')

str = str + newParag("SELECT * FROM LCBDATA.ANIKA_RESET_FRESH_COUNTS_HIST WHERE lvkeid = 223 order by DAKTUALISIERUNGSDATUM desc;")

str = str + newParag(" 223	4351	5	1	ADD	2017-04-12 13:56:54.000000	2017-04-12 13:56:54.908000	v223_k1_1	(null)	1	1	1	2017-04-12 14:02:28.740598	2017-04-12 00:00:00.000000	52	23")
str = str + newParag(" 733	6	1	ADD	2017-04-12 13:57:04.000000	2017-04-12 13:57:04.923000	v223_k1_2	(null)	1	1	1	2017-04-12 14:02:28.738383	2017-04-12 00:00:00.000000	52	22")
str = str + newParag(" 13575	3	1	ADD	2017-04-12 13:57:26.000000	2017-04-12 13:57:26.683000	v223_k1_3	(null)	1	1	1	2017-04-12 14:02:28.718179	2017-04-12 00:00:00.000000	52	21")

str = str + log('Zwischenstand')
str = str + "<p> Der 24H-Shop funktioniert wie gewuenscht. </p>"

str = str + newParag("-- KONTROLLE ---------------------------------------")
str = str + newParag("SELECT *")
str = str + newParag("FROM LCBDATA.v_be_best")
str = str + newParag("WHERE lvkeid = 223")
str = str + newParag("AND erfdatum > systimestamp - 15;")
str = str + newParag("")
str = str + newParag("SELECT *")
str = str + newParag("FROM LCBDATA.ANIKA_RESET_FRESH_COUNTS_HIST")
str = str + newParag("WHERE lvkeid = 223 order by DAKTUALISIERUNGSDATUM desc;")
str = str + newParag("")
str = str + newParag("-- BEREINIGUNG -------------------------------------")
str = str + newParag("")
str = str + newParag("UPDATE LCBDATA.be_best")
str = str + newParag("SET erfdatum = TO_DATE('20170401 23:59:59', 'yyyymmdd HH24:mi:ss')")
str = str + newParag("WHERE GBELEGID IN (1211605196, 1211605198, 1211605200, 1211605201, 1211605202, 1211605203);")
str = str + newParag("")
str = str + newParag("DELETE FROM lcbdata.be_best")
str = str + newParag("WHERE GBELEGID IN (1211605204, 1211605206, 1211605270, 1211605272, 1211605274, 1211605275, 1211605276, 1211605277, 1211605306, 1211605308);")
str = str + newParag("")
str = str + newParag("DELETE FROM LCBDATA.ANIKA_RESET_FRESH_COUNTS_HIST")
str = str + newParag("WHERE lvkeid = 223;")

str = str + log('Ende')
str = str + "</body></html>"

fobj = open('C:\Users\langfeldn\Desktop\\20170412.html','w')
fobj.writelines(str)
fobj.close()

