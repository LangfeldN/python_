import time
import os

file = 'C:\Users\langfeldn\Desktop\TEMP\Berlin Hbf\input.txt'

fobj = open (file , 'r');
data = fobj.readlines()
fobj.close()

for item in data:
    if item.find('AMOUNT') > -1:
        data01 = item.split('[')
        data02 = data01[3].split(']')
        data03 = "{} \t {}".format(data02[0].split(',')[0], data02[0].split(',')[1])
        print data03