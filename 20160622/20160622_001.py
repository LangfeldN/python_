'''
# Ask the user to type in their name an store it in a  variable named "name"

# Create a variable
name = str(raw_input('What is your name? \n'))

# Print out hello followed by the enetered Name
print 'Hello ', name

# -------------------------------------------------------------------------

# Ask the user to input 2 values and store them in variable num1 and num2
#

print "INPUT ----------------------"
num1 = raw_input("Num1 = ");
num2 = raw_input("Num2 = ");

# Convert Strings into Integer
num1_int = int(num1)
num2_int = int(num2)

print "OUTPUT ----------------------"

# Add the values an store in sum
sum = 0
sum = num1_int + num2_int
print str(num1_int) + " + " + str(num2_int) + " = " + str(sum);

# substract both values and store in diff
diff = 0
diff = num1_int - num2_int
print str(num1_int) + " - " + str(num2_int) + " = " + str(diff);

# multiply both values and store in product
product = 0
product = num1_int * num2_int
print str(num1_int) + " * " + str(num2_int) + " = " + str(product);

# divide both values and store in qoutient
qoutient = 0
qoutient = num1_int / num2_int
print str(num1_int) + " / " + str(num2_int) + " = " + str(qoutient);


# use modulus and store in remainder
remainder = 0
remainder = num1_int % num2_int
print str(num1_int) + " % " + str(num2_int) + " = " + str(remainder);


print "\nOUTPUT - FORMATED ----------------------"

print "{} + {} = {} ".format(num1,num2,sum)
print "{} - {} = {} ".format(num1,num2,diff)
print "{} * {} = {} ".format(num1,num2,product)
print "{} / {} = {} ".format(num1,num2,qoutient)
print "{} % {} = {} ".format(num1,num2,remainder)

# ---------------------------------------------------------------
# Problem 1 : Recieve miles and convert to kilometers

# kilometers = miles * 1.60934
# Enter miles = 5
# 5 miles equals 8.04 kilometers


# 1) Inupt number
miles = raw_input("Enter the miles: ")

# 2) convert string to integer
miles = int(miles)

# 3) calc kilometer
kilometers = miles * 1.60934

# 4) print an screen
print "{} miles equals {} kilometers".format(miles,kilometers)


# ---------------------------------------------------------------
# Problem 2 : Buliding a calculator

# Enter calculation: 5 * 6
# 5 * 6 = 30

# 1) store the user input of 2 values
input_calc = raw_input("Enter Calculation: ");

# 2) convert to int
values = input_calc.split()
num1 = int(values[0])
num2 = int(values[2])

result = 0
# 3) if + then we need to provide output based on addition
if values[1] == "+":
    result = num1 + num2
elif values[1] == "-":
    result = num1 - num2
elif values[1] == "*":
    result = num1 * num2
elif values[1] == "/":
    result = num1 / num2
elif values[1] == "%":
    result = num1 % num2
else:
    print "Use either + - * or / next time"


# 4) print result
print "num1 = " + str(num1)
print "num2 = " + str(num2)
print "{} = {}".format(input_calc,result)


# ---------------------------------------------------------------
# Problem 3 : different output based on age

# 1 - 18 -> Important
# 21, 50, > 65 -> Important
# All others -> Not important

# Recieve age an store in age
age = 0
age = int(raw_input("Enter an age: "));

# if age is BOTH greater than or equal to 1 and less than or equal to 18 -> Important
# age >= 1
# age <= 18
# >>> Important

## MY LOGIC
 if age >= 1 and age <= 18: print "IMPORTANT"
 elif age == 21 or age == 50: print "IMPROTANT"
 else: print "Not Important"

# if age is either 21 or 50 >>> IMPORTANT

# WE check if age is less than 65 and then convert true to false and vice versa

# Else "Not Important" << should used as default

'''


# ---------------------------------------------------------------
# Problem 4 : Sending to somewhere based on age

# if age is 5 go to kindergarten
# ages 6 throught 17 goes to grades 1 through 12
# if age ist greater then 17 say go to collega
# try to complete in 10 or less lines


age = eval(raw_input("Enter age: "))
if age == 5:                    print "Go to Kindergarten"
elif age < 5:                   print "Too young for school"
elif age >= 6 and age <= 17:
    print "Go to grade " + str(age -5)
elif age > 17:                  print "Go to college"
else: print "Nothing to say :)"


