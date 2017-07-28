file = 'C:\Users\langfeldn\Documents\Meine empfangenen Dateien\prod.beleg.v-2017-06-01.log'

fopen = open(file,'r')
data = fopen.readlines()
fopen.close()

print data[1]
idx_start = data[1].find('[',1)
idx_ende = data[1].find(']',idx_start)
print "hier"
print data[1][idx_start:idx_ende+1]

