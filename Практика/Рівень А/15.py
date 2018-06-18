import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

import functools as f

a = int(input("Введите числа: ")).split()
b=len(a)
s= f.reduce((lambda x,y: x+y),a)
k=s/a
print(k)
