#!/usr/bin/env
#coding:utf-8
#回文检测

def isPalindromel(s):
    """假定s是字符串
       如果s是回文字符串返回True，否则返回False
       忽略标点符号、空格和大小写"""

    def toChars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c
        return letters

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))

def testIsPalindromel():
    print 'Try dogGod'
    print isPalindromel('dogGod')
    print 'Try doGood'
    print isPalindromel('doGood')
