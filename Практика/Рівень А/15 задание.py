import datetime as d

рік=int(input())
місяць=int(input())
день=int(input())
дата=d.date(рік, місяць, день)
f=дата+d.timedelta(days=1)

print("Завтрішня дата",f)
