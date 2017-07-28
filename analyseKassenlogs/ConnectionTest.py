import os
import time

def ping(host):
    bOnline = False
    result = os.popen("ping -n 2 " + host).read()
    if result.find("ms") > -1:
        bOnline = True
        #print ("\t{} >>> SUCCESS".format(host))
    else:
        bOnline = False
        #print ("\t{} >>> FAIL".format(host))
    return bOnline

def ping2(hostname):
    response = os.system("ping -n 5 " + hostname)
    print 'ANTWORT ------------\n'
    print response
    if response == 0:
        pingstatus = "Network Active"
        #print hostname + ' ' + pingstatus
        return  pingstatus
    else:
        pingstatus = "Network Error"
        #print hostname + ' ' + pingstatus
        return pingstatus

# --- MAIN ----------------------------------------------------------
print time.ctime() + ' --- START '


pingresults = []
pingresults.append("google.com > {}".format(ping("google.com")))
pingresults.append("portal.lecrobag.de > {}".format(ping("portal.lecrobag.de")))
pingresults.append("SG-HHW019 > {}".format(ping("SG-HHW019")))
pingresults.append("RaspBerryPi > {}".format(ping("172.30.28.151")))
pingresults.append("DEX02 > {}".format(ping("10.49.0.17")))
pingresults.append("DEX23 > {}".format(ping("192.168.251.17")))


print pingresults

str_html="<html><head><style>div.on {border: 1px solid;width: 10px ;height: 10px;background-color: lime;}div.off {border: 1px solid;width: 10px;height: 10px;background-color: red;}</style></head><body><table>"

for item in pingresults:

    if item.find('google')>-1:
        print 'in google'
        if item.find('True') > -1 :   str_html = str_html + '<tr><td><div>google.de</div></td><td><div class="on"></div></td></tr>'
        else:                           str_html = str_html + '<tr><td><div>google.de</div></td><td><div class="off"></div></td></tr>'
    if item.find('SG-HHW019') > -1:
        print 'in HHW019'
        if item.find('True') > -1:    str_html = str_html + '<tr><td><div>SG-HHW019.schiffl-group.net</div></td><td><div class="on"></div></td></tr>'
        else:                           str_html = str_html + '<tr><td><div>SG-HHW019.schiffl-group.net</div></td><td><div class="off"></div></td></tr>'
    if item.find('lecrobag.de') > -1:
        print 'in lecrobag'
        if item.find('True')> -1:     str_html = str_html + '<tr><td><div>portal.Lecrobag.de</div></td><td><div class="on"></div></td></tr>'
        else:                           str_html = str_html + '<tr><td><div>portal.Lecrobag.de</div></td><td><div class="off"></div></td></tr>'
    if item.find('RaspBerryPi') > -1:
        print 'in RaspBerryPi'
        if item.find('True') > -1:    str_html = str_html + '<tr><td><div>RaspBerryPi</div></td><td><div class="on"></div></td></tr>'
        else:                           str_html = str_html + '<tr><td><div>RaspBerryPi</div></td><td><div class="off"></div></td></tr>'
    if item.find('DEX02') > -1:
        print 'in DEX02'
        if item.find('True') > -1:
            str_html = str_html + '<tr><td><div>DEX02</div></td><td><div class="on"></div></td></tr>'
        else:
            str_html = str_html + '<tr><td><div>DEX02</div></td><td><div class="off"></div></td></tr>'
    if item.find('DEX23') > -1:
        print 'in DEX23'
        if item.find('True') > -1:
            str_html = str_html + '<tr><td><div>DEX23</div></td><td><div class="on"></div></td></tr>'
        else:
            str_html = str_html + '<tr><td><div>DEX23</div></td><td><div class="off"></div></td></tr>'


str_html = str_html + '</table><br><div> Generiert am: {}'.format(time.ctime())
str_html = str_html + '	</body></html>'

print str_html

# open file for writing

fopen = open('C:/Users/langfeldn/Desktop/test.html','w')
fopen.write(str_html)
fopen.close()

os.startfile('C:/Users/langfeldn/Desktop/test.html')
print time.ctime() + ' --- ENDE '






