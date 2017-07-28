import os
import time

def log(text):
    print '{} --- {}'.format(time.ctime(), text)

log('START')    

mode = 'work'

if mode == 'private': file = '/home/dbg/Schreibtisch/python/work/KA1/videooutput.log'   #path on private laptop
if mode == 'work': file = 'C:\Users\langfeldn\Desktop\\tmp\KA1\\videooutput.log'   #path on work laptop

file1 = 'C:\Users\langfeldn\Desktop\\tmp\KA2\\videooutput0.log'   #path on work laptop
file2 = 'C:\Users\langfeldn\Desktop\\tmp\KA2\\videooutput1.log'   #path on work laptop
file3 = 'C:\Users\langfeldn\Desktop\\tmp\KA2\\videooutput2.log'   #path on work laptop

fobj = open(file1)
data1 = fobj.readlines()
fobj.close()

fobj = open(file2)
data2 = fobj.readlines()
fobj.close()

fobj = open(file3)
data3 = fobj.readlines()
fobj.close()

data = []
for entry in data1:
    data.append(entry)
for entry in data2:
    data.append(entry)
for entry in data3:
    data.append(entry)




treffer = []
for entry in data:
    if entry.find('Storv') > -1: treffer.append(entry)
    if entry.find('Verkv') > -1: treffer.append(entry)


fobj_write = open(os.getcwd()+'\out.txt','w')
outStr = ""

for entry in treffer:
    data_ = entry.split(' ')
    len_ = len(data_)
    beleg_ = "v{}".format(data_[8].split('v')[1])
    outStr = "{} {} {} {}\n".format(data_[0], data_[1], beleg_, data_[len_-2])
    fobj_write.write(outStr)

fobj_write.close()



log('END')





