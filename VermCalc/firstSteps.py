# coding=utf-8
## Ablauflogik
##

## IMPORTS ------------------------------------------------

import math
import time

## METHODEN -----------------------------------------------

def Log(text):
    print time.ctime()+ " --- " + text

def calcPointDist(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dist = math.sqrt((dx*dx)+(dy*dy))
    print dist

def calcPointRiwi(x1,y1,x2,y2):
    dx = x2-x1
    dy = y2-y1
    result = math.atan(dy / dx)
    result = (result * 400)/ math.pi          # Umrechnung in GON

    ## ACHTUNG SONDERBEHANDLUNGEN
    if(dy > 0 and dx > 0):result = result + 0
    if(dy > 0 and dx < 0):result = result + 200
    if(dy < 0 and dx < 0):result = result + 200
    if(dy < 0 and dx > 0):result = result + 400

    print "Hinweis:\n die Berechnung ist noch nicht ganz sauber."
    print result


def calcFreqLevelDist(freqInMHz, levelInDb):
    # dieses Skript soll auf Basis der Frequenz und dem WLAN-Level eine Strecke berechen.

    result = (27.55 - (20 * math.log10(freqInMHz)) + math.fabs(levelInDb)) / 20.0
    result = math.pow(10.0, result)     # Anwendung des 10er-Log
    result = result/ 3.28              # Umrechnung in Meter
    print result                        #Druckausgabe



## MAIN ----------------------------------------------------

Log("START")

Log("STRECKEN")

calcPointDist(230.30 ,401.10 , 280.50 , 461.20 )
calcPointDist(230.30 ,401.10 , 252.44 , 351.00 )
calcPointDist(230.30 ,401.10 , 186.36 , 350.50 )
calcPointDist(230.30 ,401.10 , 200.00 , 444.00 )
# -- funktioniert

Log("RIWI")

calcPointRiwi(401.10 , 230.30 , 461.20 , 280.50 )
calcPointRiwi(401.10 , 230.30 , 351.00 , 252.44 )
calcPointRiwi(401.10 , 230.30 , 350.50 , 186.36 )
calcPointRiwi(401.10 , 230.30 , 444.00 , 200.00  )

Log("ENDE")

## ----------------------------------------------
## Testumgebung








