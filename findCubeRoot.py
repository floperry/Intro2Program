#!/usr/bin/env
#coding:utf-8
#使用二分查找寻找任意数的立方根

x = int(raw_input('Enter a number: '))
epsilon = 0.01
numGuesses = 0
low = min(-1.0, x)
high = max(1.0, x)
ans = (low + high)/2.0

while abs(ans**3 - x) >= epsilon:
    print 'low =', low, 'high =', high, 'ans =', ans
    numGuesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (low + high)/2.0
print 'numGuesses =', numGuesses
print ans, 'is close to cube root of', x
