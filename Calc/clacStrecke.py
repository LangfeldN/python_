## Berechnung der Strecke zwischen zwei Punkten

# Punkt 1
x1 = 0
y1 = 0

# Punkt 1
x2 = -2
y2 = -2

## Calc
# calc deltas
dy = y2 - y1
dx = x2 - x1

s = abs(dy/dx)

print "Punkt 1 : [ {} | {} ] ".format(x1,y1)
print "Punkt 2 : [ {} | {} ] ".format(x2,y2)
print "DeltaX  : {} ".format(dx)
print "DeltaY  : {} ".format(dy)
print "Strecke : {} ".format(s)

## Quadrantenlogik
#
# | dx | dy | Quad
# | +  | +  | 1
# | +  | -  | 2
# | -  | -  | 3
# | -  | +  | 4


# wenn dx > 0 und dy > 0
