import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

a=input("Месяц:")
if a in ["January","March","May","July","August","October","December"]:
    print("In "+str(a)+" 31 days")
elif a in ["April","June","September","November"]:
    print("In " + str(a) + " 30 days")
else:
    print("In " + str(a) + " 28 or 29 days")
