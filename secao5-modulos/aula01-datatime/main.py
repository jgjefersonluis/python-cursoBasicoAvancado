from datetime import datetime, timedelta

# strptime(str, formato(fmt))
# .strftime(fmt)
# timestamp
# fromtimestamp()

#data = datetime.strptime('20/04/1987 20:00:00','%d/%m/%Y %H:%M:%S')
#data = data + timedelta(days=5, seconds=59)
#data = data + timedelta(seconds=2*60*60)
#data = data + timedelta(seconds=59*60)
#print(data.strftime('%d/%m/%Y %H:%M:%S'))


d1 = datetime.strptime('20/04/1987 20:00:00','%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('25/04/1987 22:30:00','%d/%m/%Y %H:%M:%S')
dif = d2-d1
print(dif)
print(dif.days)




