#!/usr/bin/env
#coding:utf-8
#将输入的数表示成幂指数形式

usrinput = int(raw_input('Enter a Number: '))
root = 1
pwr = 1

while root ** pwr != usrinput:
    pwr = pwr + 1
    if pwr > 5:
        root = root + 1
        pwr = 0
    if root ** pwr > usrinput:
        root = root + 1
        pwr = 0
print usrinput, "=", root, "**", pwr

