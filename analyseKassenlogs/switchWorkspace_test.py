## Ermittlung aller *.db-Dateien im Ordner auf der angegebenen Ebene

## IMPORT -------------------------

import time
import os

## METHODE ------------------------

def log(text):
    print time.ctime() + ' --- ' + text


wd = 'C:\Users\langfeldn\Desktop\TEMP\\20161121_BremenTunnel'

os.chdir(wd)
log("CHDIR")

cwd = os.getcwd()
print " cwd = " + cwd

if cwd == wd : log("success")

dirList = os.listdir(cwd)
fileList = []

for f in dirList :
    if f.find('.db') > 0 : fileList.append(cwd + '\\' + f)




