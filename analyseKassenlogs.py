## --- ANALYSE FEHLENDER VERK?UFE -------------------
##
## In Polen ist es vorgekommen, dass Belege von der Kasse
## angelegt wurde und auch vom Fiscaldrucker gedruckt wurden.
## Diese Belege wurden jedoch nicht von der Kasse gespeichert
## oder gebucht und tauchten somit nicht im Server/Datenabnk auf.

## WORKFLOW
## 1) ORdner Suchen
## 2) alles scannen, was enthalten ist
## 3) Alle Daten wegschreiben und wirgendwie ordnen
## 4) Daten auswerten
##  4.1) Ermittlung des Zeitstempels
##  4.2) Ermittlung des Beleges
##  4.3) Ermittlung, ob der Beleg auch final erzeugt wurde
##      -- Das sollte sich wiederrum auch aus dem Kassenlog ermitteln lasse.
##      -- Vielleicht sollte man dann einfach f?r jede Kasse eine neue Liste schaffen
##      -- Es gibt ja Kassen, die sowhol erzeugen als auch empfangen
##      -- Es gibt aber auch Kassen, die nur empfangen

##  Der Logik nach sollte ja ein Beleg, der auf einer Kasse defeinitiv erzeugt wurde,
##  auch auf die anderen Kassen kommuniziert werden.


## IMPORT ------------------------------------------
import os
import time



## METHODEN ------------------------------------------


analyseDir = ''

os.chdir(analyseDir);
print(os.getcwd())
fileList = []               ## INIT FLIST
fileList = getAllFiles 

def getAllFiles(curDir):
    fList = []
    fList = os.listdir(curDir)
    return fList








