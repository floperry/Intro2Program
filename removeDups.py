#!/usr/bin/env
#coding:utf-8
#删除列表L1出现在L2中的元素

def removeDups(L1, L2):
    """假定L1和L2是列表，
       删除L1中出现在L2中的元素"""
    for e1 in L1:
        if e1 in L2:
            L1.remove(e1)

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
removeDups(L1, L2)
print 'L1 =', L1

