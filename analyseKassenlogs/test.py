import os
import time
#import subprocess as sp

# METHODEN ------------------------------
from unittest import result


def ping(host):
    #host = 'google.de'
    result = os.popen("ping -n 2 " + host).read()
    res_Split = result.split(' ')
    #for entry in res_Split:
    #    print entry
    if result.find("ms") > -1: print ("\t{} >>> SUCCESS".format(host))
    else: print ("\t{} >>> FAIL".format(host))

print (time.ctime() + ' ---- START ----------------')

ping("google.de")
ping("waserbuefl")
ping("172.30.28.151")
ping("SG-HHW019")
ping("lcb-dex-scan.lecrobag.de")

print (time.ctime() + ' ---- ENDE ----------------')




