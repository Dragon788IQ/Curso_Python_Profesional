#Practicando con el uso de las fechas y las horas
from datetime import datetime

my_date = datetime.now()
print(my_date)

my_str = my_date.strftime("%d/%m/%Y")
print(f"formato Latam: {my_str}")

my_str = my_date.strftime("%m/%d/%Y")
print(f"Formato USA: {my_str}")

my_str = my_date.strftime("Estamos en el anno %Y")
print(my_str)

#Formato 12h
#print(my_datetime.strftime('%I:%M %p'))