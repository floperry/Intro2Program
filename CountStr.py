#!/usr/bin/env
#coding:utf-8
#计算小数字符串的元素之和，小数之间用逗号分开

s = '1.23,2.4,3.123'
total = 0
i, j = 0, 0
str2num = 0.0

for c in s:
    i = i + 1
    if c == ',':
        str2num = float(s[j:i-1])
        j = i
        total = total + str2num
    if i == len(s):
        str2num = float(s[j:i])
        total = total + str2num
print total

