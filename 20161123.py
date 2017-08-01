# FIND INVENTURKAUDAWELSCH

suchString = 'Exiting CSPDBInventory::lastTimeStamp: retVal = null'

# open file


path = 'C:\\Users\\langfeldn\\Desktop\\'
filename = 'test.txt'

fileMain = path + filename

fopen = open(fileMain,'r')
data = fopen.readlines();

for entry in data:
    dataSplit = entry.split(' ')
    timestamp = dataSplit[0]
    hit = ''
    for i in dataSplit:
        c = i.find('CSPDBInventory')
        if c > -1 :  hit = i
    print timestamp + ' --- ' + hit
    # print entry



