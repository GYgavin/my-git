#!/usr/bin/env python
def dataoperate():
    f = open('data.txt','r')
    data1 = f.readline()
    data2 = data1.strip() 
    data3 = data2.split(' ')
    data = []
    for i in data3:
        i = int(i)
        data.append(i)
    return data
