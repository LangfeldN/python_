# LOOP BASICS -----------------------
'''
for i in [2,4,6,8,10]:
    print "i = " , i

for i in range(10):
    print "i = " , i
'''
# LOOP BASICS -----------------------

# BOOL BASICS -----------------------
# i = 2
# print i % 2 == 0    # >> TRUE
# BOOL BASICS -----------------------


# Loop through the list from 1 to 21

# for i in range(1, 21):
#    if (i % 2) != 0:
#        print "i = ", i


# your_float = raw_input("Enter a float: \n")

# if your_float.find(",") > 0:
#    new_float = your_float.replace(",",".")
#    print "Deine Eingabe '{}' wird in '{}' geaendert".format(your_float,new_float)
#    your_float = new_float

# your_float = float(your_float)
# print ("Round to 2 decimals : {:.2f}".format(your_float))

## >> BUILDING A METHODE FOR REUSING
from operator import inv


def inputCatchKoma(prompt):
    your_float = raw_input(prompt + ": ")
    if your_float.find(",") > 0:
        new_float = your_float.replace(",",".")
        print "Deine Eingabe '{}' wird in '{}' geaendert".format(your_float,new_float)
        your_float = new_float
    return your_float


# TASK 001 ---------------------------------------
# Have the user enter their investment amount and expected interest
# each year their investment will increase by their
#  investment + investment * interess rate is
# Print out the earnings after a 10 year period


# Ask for the money invested + the interest rate
invest = inputCatchKoma("How much invest")
rate = inputCatchKoma("Interest rate")

# convert the values to float
invest = float(str(invest))

# round the percantage rate by 2 digits
rate = float(str(rate)) * .01

# cycle through 10 years using a for loop from 0 to 9
for i in range(10):
    invest = invest + (invest * rate)

# output results
print "Investment after 10 years = {:.2f}".format(invest)





