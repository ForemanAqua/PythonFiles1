import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

h=input('Зараз вихідний? Напишіть "Так" або "Ні"\n')
f=input('Ви у  відпустці? Напишіть "Так" або "Ні"\n')

if h== 'Так' or f== 'Так':
  print ('Не вмикати будильник')
else:
  print ('Вімикнути будильник')

в2
h=input('Зараз вихідний? Напишіть "Так" або "Ні"\n')
f=input('Ви у  відпустці? Напишіть "Так" або "Ні"\n')

def alclock (x,y):
  if x== 'Так' or y== 'Так':
    print ('Не вмикати будильник')
  else:
    print ('Увімкнути будильник')
alclock(h,f);