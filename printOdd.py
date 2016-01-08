#!/usr/bin/env
# coding: utf-8

x , y, z = 1, 2, 3

if x > y:
    if y > z:
        x, y, z = x, y, z
    elif x > z:
        x, y, z = x, z, y
else:
    if y < z:
        x, y, z = z, y, x
    else:
        if x < z:
	    x, y, z = y, z, x
	else:
 	    x, y, z = y, x, z

if x % 2 != 0:
    print x
elif y % 2 != 0:
    print y
elif z % 2 != 0:
    print z
else:
    print 'There is no odd number'
        

