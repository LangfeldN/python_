
def sumNumInString(inStr):
    splitStr = inStr.split(',')
    sum = 0
    cNum = 0
    for num in splitStr:
        try:
            num = int(num)
            print "Element = {} Type: {}".format(num, type(num))
            sum = sum + num
            cNum = cNum + 1
        except ValueError: continue

    print "{} Nummern gefunden".format(cNum)
    print "Ergeben eine Summe von {}".format(sum)


def createStatement(pre,suf,val,multi):
    strOut = pre + (val*multi) + suf
    print strOut


createStatement('mygrid.setColAlign("', '");', 'true,', 45-19)
createStatement('mygrid.setColTypes("', '");', 'edtxt,', 45)
createStatement('mygrid.setColSorting("', '");', 'str,', 45)

inStr ='8,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,6'
#sumNumInString(inStr)

inStr ='0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,20, 20, 10, 10, 5,20,5, 5, 5, 20,5, 5, 5, 5, 5, 5, 5'
#sumNumInString(inStr)



