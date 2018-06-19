import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

import functools as f
import itertools as i
s=list(map(int, input("Введите числа: ").split()))
a=len(s)
summ=f.reduce((lambda x,y: x+y),s)
mid=summ/a
n=0
for item in i.count(1):
    n=n+1
    k=s[0]+s[n]
    if mid < k:
        print("Введене число більше за середнє значення")

    if mid > k:
        print("Введене число менше за середнє значення")
