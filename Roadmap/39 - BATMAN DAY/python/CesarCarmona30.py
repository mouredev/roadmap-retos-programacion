from datetime import datetime, timedelta

year_of_creation = 1939
anniversary_year = year_of_creation + 85

batman_day_anniversary_dates = []

while anniversary_year <= year_of_creation + 100:
  
  september = datetime(anniversary_year, 9, 1)

  first_saturday = 5 - september.weekday() if september.weekday() <= 5 else \
    12 - september.weekday()

  third_saturday = september + timedelta(days=first_saturday + 14)

  batman_day_anniversary_dates.append(
    (
      anniversary_year,
      anniversary_year - year_of_creation,
      third_saturday.strftime("%d-%m-%Y")
    )
  )

  anniversary_year += 1

for year, anniversary, batman_day in batman_day_anniversary_dates:
  print(f"Batman day {year} ({anniversary} aniversario): {batman_day}")


def sum_subgrid_alerts(sensors, center_x, center_y):
  total = 0

  for x in range(center_x - 1, center_x + 2):
    for y in range(center_y - 1, center_y + 2):
      for sensor in sensors:
        if sensor[0] == x and sensor[1] == y:
          total += sensor[2]

  return total

def batcave_security_system(sensors):
  
  max_alert_level = 0
  max_alert_coordinate = (0, 0)

  for x in range(1, 19):
    for y in range(1, 19):
      alert_level = sum_subgrid_alerts(sensors, x, y)
      if alert_level > max_alert_level:
        max_alert_level = alert_level
        max_alert_coordinate = (x, y)

  distance = abs(max_alert_coordinate[0]) + abs(max_alert_coordinate[1])
  activate_protocol = max_alert_level > 20

  return max_alert_coordinate, max_alert_level, distance, activate_protocol

sensors = [
  (2, 3, 7),
  (4, 3, 8),
  (2, 2, 7),
  (10, 12, 8),
  (11, 11, 8),
  (10, 11, 8),
  (15, 18, 4)
]

result = batcave_security_system(sensors)

print(f"Centro de cuadrícula mas amenzada: {result[0]}")
print(f"Máximo nivel de alerta: {result[1]}")
print(f"Distancia a la Baticueva: {result[2]}")
print(f"Activar protocolo de seguridad: {result[3]}")