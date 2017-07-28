# SplitMsg.py
# Dieses Skript soll einen InputString aufspliten und darstellen, das spart 2 Minuten

## BEISPIEL:

#  Bitte Text eingeben:
#  lCodeSection#= 2000, tmp_sAnlageUser#= SauerW, tmp_dAnlageDatum#= 20161101 00:00:00.000, tmp_lPersonalID#= 69377, tmp_lDatengruppe#= -21157, tmp_lVkeID#= 718, tmp_dBezugsdatum#= 20161101 00:00:00.000, tmp_dDatumAnfang#= 20161101 06:00:00.000, tmp_dDatumEnde#= 20161101 14:00:00.000, tmp_lArbeitszeitTypID#= 1, tmp_fAbzurechnendeStd#= 0, tmp_lStatus#= 1, tmp_lPausentaste#= 0, tmp_lGeloescht#= 0, tmp_lAbgeschlossen#= 0, tmp_fNachtzuschlag#= ,25, tmp_sBemerkungen#= NULL, tmp_dAktualisierungsdatum#= 20161201 18:45:11.045, tmp_sUserTmp#= SAUERW

#  /*
#  lCodeSection#= 2000
#  tmp_sAnlageUser#= SauerW
#  tmp_dAnlageDatum#= 20161101 00:00:00.000
#  tmp_lPersonalID#= 69377
#  tmp_lDatengruppe#= -21157
#  tmp_lVkeID#= 718
#  tmp_dBezugsdatum#= 20161101 00:00:00.000
#  tmp_dDatumAnfang#= 20161101 06:00:00.000
#  tmp_dDatumEnde#= 20161101 14:00:00.000
#  tmp_lArbeitszeitTypID#= 1
#  tmp_fAbzurechnendeStd#= 0
#  tmp_lStatus#= 1
#  tmp_lPausentaste#= 0
#  tmp_lGeloescht#= 0
#  tmp_lAbgeschlossen#= 0
#  tmp_fNachtzuschlag#=
#  25
#  tmp_sBemerkungen#= NULL
#  tmp_dAktualisierungsdatum#= 20161201 18:45:11.045
#  tmp_sUserTmp#= SAUERW
#  */



input = raw_input('\n\nBitte Text eingeben: \n')

inputsplit = input.split(',')
print('\n')

print '/*'
for item in inputsplit:
    print item.lstrip()
print '*/'
