##
# Der Mqtt-Message-Counter soll sich eine Mqtt-Datei holen und die unterschiedlichen Messages zählen

# Workflow:
#   - open file
#   - find Messages
#   - count different messages



# --------------------------------------------------------------------------------
#   - open file

def openfile():
    import time                                             ## IMPORT
    import os                                               ## IMPORT
    print time.ctime() + " --- START"                       ## START
        ## LIST ALL FILES CONTAINING IN THE CURFOLDER
    path = "C:\Users\langfeldn\Desktop\WORK\PROJEKTE\LCB\ANIKA\ANALYSE\\20160622_v248_Kartenzahlung"
    os.chdir(path)                                          ## GET DIR
    curDir = os.getcwd();                                   ## CHANGE DIR
    fileList = os.listdir(curDir);                          ## GET FILELIST
    print "\n{} Dateien gefunden".format((len(fileList)))   ## PRINT RESULT
    for item in fileList:                                   ## PRINT FILES
        print " " + item                                    ## PRINT FILES
    choice = raw_input("\nBitte eine Datei angeben.  ");    ## CHOOSE FILE
    finPath = path + "\\" + choice                          ## CREATE FINAL FILEPATH
    fopen = open(finPath, 'r')                              ## OPEN FILE
    data = fopen.readlines();                               ## READ LINES
    lines = len(data)                                       ## READ LINES
    print "Es wurden {} Zeilen eingelesen\n".format(lines); ## PRINT RESULT
    print time.ctime() + " --- ENDEs";                      ## ENDE




# --------------------------------------------------------------------------------

# suchstring :
#   - Obtained SELL_SALES_VOUCHER:
#   - parsing message type: STORNO_SALE_VOUCHER
#   - parsing message type: DO_FRESH_POST
#   - parsing message type: DO_DWINDLING
#   - parsing message type: DO_FRESH_FRACTION_DWINDLING

# --------------------------------------------------------------------------------





# --------------------------------------------------------------------------------