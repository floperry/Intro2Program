#!/usr/bin/env
#coding:utf-8
#寻找完全立方数的立方根

x = int(raw_input('Enter an integer: '))

for ans in range(0, abs(x)+1):
    if ans**3 >= abs(x):
        break
if ans**3 != abs(x):
    print x, 'is not a perfect cube'
else:
    if x < 0:
        ans = -ans
    print 'Cube root of', x, 'is', ans
