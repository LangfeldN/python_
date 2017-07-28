
import urllib2
import os
import time

def log(text):
    print "{} -- {}".format(time.ctime(), text)

def onlineScan(url,saveFile):
    log('OnlineScan')
    # bSave = True or False
    log('Open URL')
#    urlObj = urllib2.urlopen("https://bs.to/serie/Game-of-Thrones")
    urlObj = urllib2.urlopen(url)
    log('Read Src')
    data = urlObj.read()
    #print data
    if len(saveFile) > 1:
        log('Write src 2 file')
        file = saveFile
        fobj = open(file, 'w')
        fobj.write(data)
        fobj.close()
        return data
    else:
        print len(data)
        return data

def offlineScan(file):
    log('OfflineScan')
    fobj = open(file,'r')
    data = fobj.readlines()
    fobj.close()
    return data


log('START')

data = onlineScan('https://bs.to/serie/Game-of-Thrones/5/','src.txt')
data = offlineScan('src.txt')
treffer = []
for item in data:
    if item.find('AuroraVid') > -1:
        tmp = 'https://bs.to/'+item.rstrip().lstrip().split('"')[5]
        treffer.append(tmp)
        print tmp

strTreffer = "{} Treffer".format(len(treffer))
log(strTreffer)

intLinks = treffer
extLinks = []

fObj = open('finalLinks.txt','w')

log('next step scan AuroraVid')
for intLink in treffer:
    log(intLink)
    urlObj = urllib2.urlopen(intLink)
    dataTmp = urlObj.read()
    urlObj.close()
    tmpFObj = open('scantmp.txt','w')
    tmpFObj.write(dataTmp)
    tmpFObj.close()
    tmpFObj = open('scantmp.txt','r')
    dataTmp = tmpFObj.readlines()
    tmpFObj.close()

    for item in dataTmp:
        #print item
        if item.find('//bs.to/out/') > -1:
            #print item
            extLink = item.split('"')[1]
            extLinks.append(extLink)
            #tmpstr = "{}\t>>>\t{}".format(extLink,intLink)
            #tmpstr = "{}".format(extLink)
            tmpstr = "{}".format(intLink)
            fObj.writelines(tmpstr+'\n')
            log(extLink)

#print dataTmp
fObj.close()



log('ENDE')



