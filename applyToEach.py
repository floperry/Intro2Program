#!/usr/bin/env
#coding:utf-8
#将函数应用到列表中的元素

def applyToEach(L, f):
    """假定L是列表，f是函数
       将f应用在L的每个元素上，并用返回值替换原来的元素"""
    for i in range(len(L)):
        L[i] = f(L[i])

def fact(n):
    if n == 1:
        return n
    else:
        return n*fact(n-1)

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
def testApplyToEach():
    L = [1, -2, 3.33]
    print 'L =', L
    print 'Apply abs to each element of L.'
    applyToEach(L, abs)
    print 'L =', L
    print 'Apply int to each element of L.'
    applyToEach(L, int)
    print 'L =', L
    print 'Apply factorial to each element of L.'
    applyToEach(L, fact)
    print 'L =', L
    print 'Apply Fibonnaci to each element of L.'
    applyToEach(L, fib)
    print 'L =', L
        
