import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

name=input("Введіть ваше і'мя: ")
print("Доброго здоров'ячка,",name)