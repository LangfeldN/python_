import math;
from random import random

def calcDist(x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1

    dist = math.sqrt(dx^2/dy^2)
    print "Distanz: {}".format(dist)
    return dist

dist1 = calcDist(1,2,3,4)
dist2 = calcDist(1,2,3,8)

if dist1 > dist2:
    print "dist1 ist laenger"
if dist1 < dist2:
    print "dist2 ist laenger"