#!/usr/bin/env python
import random
n = int(input('please input how manys random numbers do you want to build:'))
print(n)
def randomnum():
    datas = []
    a = len(datas)
    while a < n:
        x = random.randint(1,200)
        datas.append(x)
        a = len(datas)
    return datas
