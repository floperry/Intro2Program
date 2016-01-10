#!/usr/bin/env
#coding:utf-8
#输出20和100的公约数并求和

def findDivisors(n1, n2):
    """Assumes n1 & n2 positive integer
       Return a tuple, include divisors of nq & n2"""
    divisors = ()  #empty tuple
    for i in range(1, min(n1, n2) + 1):
        if n1%i == 0 and n2%i == 0:
            divisors = divisors + (i,)
    return divisors

divisors = findDivisors(20, 100)
print divisors
total = 0
for d in divisors:
    total += d
print total
