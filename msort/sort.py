from msort import *
from dataoperate import *
from randomnum import *
import time

def Out(x):
    list = x
    count=0
    for i in list:
        print(i,end=' ')
        count += 1
        if(count%10==0):
            print(end='\n')
alist = randomnum()

print('\norigin data:')
Out(alist)

start = time.clock()
operated = quickSort(alist)
end = time.clock()

print('\nresult data:')
Out(operated)

Max = operated[len(alist)-1]
print('\nYou have built',n,'random numbers, and the max is',Max,'!')
print('This program running with',end-start,'seconds!')
