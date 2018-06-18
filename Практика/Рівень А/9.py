import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

возвраст=int(input("Введите свой возвраст:"))
x=возвраст - 2
y=x*4
собака=y+21
if возвраст >= 0:
    print(возвраст ,"еквівалентно", собака ,"років собаки")
else:
    print("Введено від'ємне число")
