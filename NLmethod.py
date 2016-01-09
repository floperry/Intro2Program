#!/usr/bin/env
#coding:utf-8
#用牛顿-拉夫逊方法寻找平方根
#寻找x，满足x**2 - 24在epsilon和0之间

epsilon = 0.01
k = 24.0
guess = k/2.0

while abs(guess*guess -k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess))
print 'Square root of', k, 'is about', guess
