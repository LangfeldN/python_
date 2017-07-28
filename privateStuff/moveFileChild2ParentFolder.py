#
# IMPORT -----------------------
import time
import os


# METHODEN ---------------------
def LOG(text):  print "{} --- {}".format(time.ctime(), text)


# VARIABLEN --------------------

cwd = ''
fParent = ''
fChildren = []
fChild = ''
file2move = ''

# MAIN -------------------------

LOG('START')

# 1) Ordner wechseln

cwd = os.getcwd()
fParent = 'C:\Users\langfeldn\Documents\STEVEN'
os.chdir(fParent)
if os.getcwd() == fParent: LOG('Verzeichniswechsel erfolgreich')

# 2) fChildren ermitteln und fuellen

files = []
files = os.listdir(fParent)
for entry in files :
    dataTyp = entry[len(entry) - 4:len(entry)]
    if dataTyp.find('.') < 0 : fChildren.append(fParent + '\\' + entry)

# 3) in den Ordner rein, Datei suchen und verschieben
for i in fChildren:
    fChild = i
    os.chdir(fChild)
    fList = os.listdir(os.getcwd())
    if len(fList) > 0:
        file2move = fList[0]
        src = fChild + '\\' + file2move
        dst = fParent + '\\' + file2move
        print 'src: ' + src
        print 'dst: ' + dst
        os.rename(src, dst)
    else:
        file2move = '<no File>'

    #print "{} \n\t {}".format(fChild,file2move)


# 4) Ordner Ordner loeschen
# wurde vorerst manuell erledigt



LOG('ENDE')