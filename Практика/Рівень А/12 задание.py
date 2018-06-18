import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

z=int(input("seconds"))
v=int(input("minutes"))
x=int(input("hours"))
c=int(input("days"))
s=z+(x*3600)+(c*86400)+(v*60)
print(s)