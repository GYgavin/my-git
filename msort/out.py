list=[1,1,3,4,5,62,5,3,52,5,3,6,6,8,4,6,4,9,5,6]
count=0
for i in list:
    print(i,end=' ')
    count += 1
    if(count%10==0):
        print(end='\n')
print(len(list))
