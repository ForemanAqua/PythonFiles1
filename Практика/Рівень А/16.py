import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

д=float(input("Довжина:"))
ш=float(input("Ширина:"))
S=(float(д)*float(ш))
гектар=float(S)/10000
аар=float(гектар)*100
print("Площа :",S,"м**2")
print("Площа :",гектар,"гектар")
print("Площа :",аар,"аар")
