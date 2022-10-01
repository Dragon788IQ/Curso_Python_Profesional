from datetime import datetime
import pytz

my_city_timezone = pytz.timezone("America/Bogota")
my_city_time = datetime.now(my_city_timezone)
time_calculated = my_city_time.strftime("%d/%m/%Y, %H:%M:%S")
print(f"Bogota {time_calculated}")

my_city_timezone = pytz.timezone("America/Mexico_city")
my_city_time = datetime.now(my_city_timezone)
time_calculated = my_city_time.strftime("%d/%m/%Y, %H:%M:%S")
print(f"Mexico_city {time_calculated}")

my_city_timezone = pytz.timezone("America/Caracas")
my_city_time = datetime.now(my_city_timezone)
time_calculated = my_city_time.strftime("%d/%m/%Y, %H:%M:%S")
print(f"Caracas {time_calculated}")