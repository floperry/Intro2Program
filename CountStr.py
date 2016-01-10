#!/usr/bin/env
#coding:utf-8
#计算小数字符串的元素之和，小数之间用逗号分开

s = '1.23,2.4,3.123'
total = 0.0

L = s.split(',')
for e in L:
    total += float(e)
print total

