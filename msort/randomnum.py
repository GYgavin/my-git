#!/usr/bin/env python
import random
n = int(input('How manys random numbers do you want to build?  '))
def randomnum():
    datas = []
    a = len(datas)
    while a < n:
        x = random.randint(1,10000)
        datas.append(x)
        a = len(datas)
    return datas
