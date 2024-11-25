from datetime import datetime,date
from calendar import Calendar

# Reto 1
#Batman day is the 3rd Saturday of september

for year in range(2024,2040):
   c = Calendar()
   weeks = c.monthdatescalendar(year=year,month=9)
   #Find the thrid saturday of the month
   saturdays = 0

   for week in weeks:
      for day in week:
         if day.weekday() == 5 and day.month == 9:
            saturdays += 1
            if saturdays == 3:
               print(f'El dia de batman {year} se celebrara el dia {day.day}')
def calculateSum(matrix,row,column):
   sum = 0

   for i in range(row,row+3):
      for j in range(column,column+3):
         sum += matrix[i][j]
   return sum      

def batmanSecurity(sensors:list):
   #Initialize the matrix
   matrix = 20*[0]
   for row in range(0,20):
      matrix[row] = 20*[0]
   
   #Set the values from the sensors
   for sensor in sensors: 
      matrix[sensor[0]][sensor[1]] = sensor[2]

   # Find the 3x3 submatrix with more level of danger
   max_threat = 0
   centerX = 0
   centerY = 0
   distance_batcave = 0
   for i in range(0,18):
      for j in range(0,18):
        sum =  calculateSum(matrix,i,j)
        if sum >= max_threat:
           distance_batcave = abs((i+1)+(j+1))
           centerX = i+1
           centerY = j+1       
           max_threat = sum
   print(f'Suma de amenazas cuadricula mas amenazada: {max_threat}')
   print(f'Centro cuadricula mas amenazada: {centerX},{centerY}')
   print(f'Distancia a la  batcueva: {distance_batcave}')
   if max_threat >= 20:
      print("Activando protocolo de alerta")
   else:
      print("Protocolo de alerta no activado")   
           
print("--- Batman security system ---")
sensors = [(0,0,2),(0,1,8),(0,2,3),(1,0,4),(1,1,0),(1,2,3),(2,0,0),(2,1,3),(2,2,3),
           (17,3,24),(17,4,5),(17,5,9),(18,3,23),(18,4,0),(18,5,24),(19,3,0),(19,4,0),(19,5,6)]
batmanSecurity(sensors)
