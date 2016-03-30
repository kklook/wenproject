# -*- coding:utf-8 -*-
import sys
import math
list=range(6)
def exp(i):
    if i==1:
        list[i]=1
        return 1
    if i==2:
        list[i]=1
        return 1
    list[i]=exp(i-2)+exp(i-1)
    return exp(i-2)+exp(i-1)
exp(5)
print list