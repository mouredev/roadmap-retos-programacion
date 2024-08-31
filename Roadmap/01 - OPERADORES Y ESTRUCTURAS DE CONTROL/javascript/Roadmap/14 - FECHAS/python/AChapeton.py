from datetime import datetime

today = datetime.now()
print('today: ', today)

birth = datetime(1997, 6, 2, 15, 30, 00)
print('birth: ', birth)

# DIFICULTAD EXTRA

print('Dia, mes y año: ', birth.strftime("%d/%m/%y"))
print('Dia, mes y año completo: ', birth.strftime("%d/%m/%Y"))
print('Hora formato 12, minuto y segundos: ', birth.strftime("%I:%M:%S"))
print('Hora formato 24, minuto y segundos: ', birth.strftime("%H:%M:%S"))
print('Dia del año: ', birth.strftime("%j"))
print('Semana del año: ', birth.strftime("%U"))
print('Mes del año abreviado: ', birth.strftime("%h"))
print('Mes del año: ', birth.strftime("%B"))
print('Dia de la semana: ', birth.strftime("%A"))
print('Representacion horaria: ', birth.strftime("%p"))