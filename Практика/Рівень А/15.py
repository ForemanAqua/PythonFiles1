import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

a=list(map(int,input("Введіть числа:").split(" ")))
if a[0]==int(0):
  print("Error , first number can't be 0")
elif int(0) in a:
    print(sum(a)/(len(a)-1))
