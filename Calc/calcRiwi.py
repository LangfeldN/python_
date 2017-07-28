## Quadrantenlogik
#
# | dx | dy | Quad
# | +  | +  | 1     + 0gon
# | +  | -  | 2     + 200gon
# | -  | -  | 3     + 200gon
# | -  | +  | 4     + 400gon


import math

## Berechnung der Strecke zwischen zwei Punkten

# Punkt 1
x1 = 0
y1 = 0

# Punkt 1
x2 = 2
y2 = 0

## Calc
# calc deltas
dy = y2 - y1
dx = x2 - x1

s = math.tan(dy/dx)/(math.pi*360)
# dieser Werte m?sste nun in Grad ausgegeben werden

print "Punkt 1 : [ {:.2f} | {:.2f} ] ".format(float(x1),float(y1))
print "Punkt 2 : [ {:.2f} | {:.2f} ] ".format(float(x2),float(y2))
print "DeltaX  : {:.2f} ".format(float(dx))
print "DeltaY  : {:.2f} ".format(float(dy))
print "riwi    : {:.2f} ".format(float(s))

## Quadrantenlogik
#
# | dx | dy | Quad
# | +  | +  | 1
# | +  | -  | 2
# | -  | -  | 3
# | -  | +  | 4



