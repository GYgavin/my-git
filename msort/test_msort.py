from msort import *
list = [12,23,213,4,34,32,432,324,324,3,24,32,123]
first = 0
last = len(list)-1
print(quickSort(list))
print(quickSortHelper(list,first,last))
print(partition(list,first,last))
