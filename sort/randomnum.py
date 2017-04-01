#!/usr/bin/env python
import random
from msort import *
n = int(input('please input how many amounts you want to build:'))
def randomnum():
    datas = []
    a = len(datas)
    while a < n:
        x = random.randint(1,200)
        datas.append(x)
        a = len(datas)
    return datas
alist = randomnum()
quickSort(alist)
print (alist)
