import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()), "\n")
printTimeStamp("Valeriy Neroznak")

import math

s = int(input('Довжина сторони: '))
n = int(input('Кількість сторін: '))

print ((n*(s**2))/(4*math.tan(math.degrees(math.pi)/n)))

