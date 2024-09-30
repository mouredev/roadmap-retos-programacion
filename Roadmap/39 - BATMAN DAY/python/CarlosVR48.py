"""* EJERCICIO:
 * Cada año se celebra el Batman Day durante la tercera semana de septiembre... 
 * ¡Y este año cumple 85 años! Te propongo un reto doble:
 *
 * RETO 1:
 * Crea un programa que calcule cuándo se va a celebrar el Batman Day hasta 
 * su 100 aniversario.
 *
 * RETO 2:
 * Crea un programa que implemente el sistema de seguridad de la Batcueva. 
 * Este sistema está diseñado para monitorear múltiples sensores distribuidos
 * por Gotham, detectar intrusos y activar respuestas automatizadas. 
 * Cada sensor reporta su estado en tiempo real, y Batman necesita un programa 
 * que procese estos datos para tomar decisiones estratégicas.
 * Requisitos:
 * - El mapa de Gotham y los sensores se representa con una cuadrícula 20x20.
 * - Cada sensor se identifica con una coordenada (x, y) y un nivel
 *   de amenaza entre 0 a 10 (número entero).
 * - Batman debe concentrar recursos en el área más crítica de Gotham.
 * - El programa recibe un listado de tuplas representando coordenadas de los 
 *   sensores y su nivel de amenaza. El umbral de activación del protocolo de
 *   seguridad es 20 (sumatorio de amenazas en una cuadrícula 3x3).
 * Acciones: 
 * - Identifica el área con mayor concentración de amenazas
 *   (sumatorio de amenazas en una cuadrícula 3x3).
 * - Si el sumatorio de amenazas es mayor al umbral, activa el 
 *   protocolo de seguridad.
 * - Calcula la distancia desde la Batcueva, situada en (0, 0). La distancia es
 *   la suma absoluta de las coordenadas al centro de la cuadrícula amenazada.
 * - Muestra la coordenada al centro de la cuadrícula más amenazada, la suma de
 *   sus amenazas, la distancia a la Batcueva y si se debe activar el
 *   protocolo de seguridad."""


from os import system
import random,time
import calendar

print ("PRIMER EJERCICIO PARA CALCULAR EL DIA DEL 100 ANIVERSARIO DE BATMAN DAY")
#calculamos primero el año que sera el 100 aniversario
year = ((100-85)+2024)
#introducimos el mes que es el aniversario
mes = 9
#calculamos el calendario de ese mes y mostramos el numero de semanas
lista_mes = calendar.monthcalendar(year,mes)
print ("NUMERO DE SEMANAS QUE TIENE EL MES: ",len(lista_mes))
#introducimos la semana que sera el aniversario
semana_aniversario = 3
#muetra calendario
for index in lista_mes:
    print (index)
#guardamos el dia del aniversario y lo mostramos
dia_aniversario = lista_mes [semana_aniversario-1] [0]
print (f"EL 100 ANIVERSARIO SERA {dia_aniversario} - {mes} - {year}" )
input ("PULSA ENTER PARA CONTINUAR")

salir = ""

mapa = [["🦇"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        ]

#funcion que se le tiene que dar parametros numero de sensor, posicion central del 
#sensor y el nivel de cada casilla del sensor

def sensor_3x3(posicion,x,y,a,b,c,d,e,f,g,h,i):
    index = x
    indey = y
    #obtengo las codenadas de cada casilla del sensor
    xa1 = index - 1
    xa2 = index
    xa3 = index + 1
    ya = indey - 1
    yb = indey
    yc = indey +1

    monitor = (posicion,xa1,xa2,xa3,ya,yb,yc,a,b,c,d,e,f,g,h,i)
    protocolo = ((monitor [7] + monitor [8] + monitor [9] + monitor [10] + monitor [11] + monitor [12] + monitor [13] + monitor [14] + monitor [15]))
    
    #para cada casilla de sensor 3x3 muestro si su nivel es alto o bajo a partir de 7
    if monitor [7] >=7:
        aa = ("ALTO")
    else:
        aa = ("BAJO")
    if monitor [8] >=7:
        ab = ("ALTO")
    else:
        ab = ("BAJO")
    if monitor [9] >=7:
        ac = ("ALTO")
    else:
        ac = ("BAJO")

    if monitor [10] >=7:
        ba = ("ALTO")
    else:
        ba = ("BAJO")
    if monitor [11] >=7:
        bb = ("ALTO")
    else:
        bb = ("BAJO")
    if monitor [12] >=7:
        bc = ("ALTO")
    else:
        bc = ("BAJO")
    
    if monitor [13] >=7:
        ca = ("ALTO")
    else:
        ca = ("BAJO")
    if monitor [14] >=7:
        cb = ("ALTO")
    else:
        cb = ("BAJO")
    if monitor [15] >=7:
        cc = ("ALTO")
    else:
        cc = ("BAJO")
    
    #muestro por pantalla cada sensor
    print (f"{monitor [0]}  {type(monitor)} ")
    print (f"X: {monitor [1]} Y: {monitor [4]} | X: {monitor [2]} Y: {monitor [4]} | X: {monitor [3]} Y: {monitor [4]}")  
    print (f"NIVEL: {monitor [7]}      NIVEL: {monitor [8]}      NIVEL: {monitor [9]}")
    print (f"{aa}          {ab}          {ac} ")
    print (f"\nX: {monitor [1]} Y: {monitor [5]} | X: {monitor [2]} Y: {monitor [5]} | X: {monitor [3]} Y: {monitor [5]}")  
    print (f"NIVEL: {monitor [10]}     NIVEL: {monitor [11]}      NIVEL: {monitor [12]}")
    print (f"{ba}          {bb}         {bc} ")
    print (f"\nX: {monitor [1]} Y: {monitor [6]} | X: {monitor [2]} Y: {monitor [6]} | X: {monitor [3]} Y: {monitor [6]}")  
    print (f"NIVEL: {monitor [13]}      NIVEL: {monitor [14]}      NIVEL: {monitor [15]}")
    print (f"{ca}          {cb}          {cc} ")
    
    #el umbral de activacioon para el sensor tiene que ser 20 o mas 
    if protocolo >= 20:
        print (f"\nLA SUMA DE TODAS LAS CASILLAS ES {protocolo}")
        print ("MAYOR O IGUAL A 20 PROTOCOLO ACTIVADO \n")
        print ("───────────────────────────────────────────────")
    else:
        print (f"\nLA SUMA DE TODAS  LAS CASILLAS ES {protocolo}")
        print ("MENOR DE 20 PROTOCOLO DESACTIVADO\n")
        print ("───────────────────────────────────────────────")

#inicio del programa que se repite hasta que escribamos salir 
while not(salir == "SALIR"):
    system("cls")
    cantidad_sensores = 1
   
    #creo 6 sensores en el bucle while
    while cantidad_sensores<7:
        suma_sensor = int()
        sensor_a = []
        sensor_b = []
        sensor_c = []
        #creador de nivel de alerta en el sensor para cada casilla 3x3
        for index1 in range(3):
            sensor_a.append(random.randint(1,10))
        for index1 in range(3):
            sensor_b.append(random.randint(1,10))    
        for index1 in range(3):
            sensor_c.append(random.randint(1,10))

        #suma todos los sensores de la cuadricula 3x3 y los gurdo sumar_sensor
        for index_a,index_b,index_c in (sensor_a,sensor_b,sensor_c):
            suma_sensor = suma_sensor + index_a + index_b + index_c
        
        #segun el numero de sensor lo muestro en las cordenadas y escribo
        #la lista con numero de senso, cordenadas y distancia.
        #llamo a la funcion sensor_3x3 para monitorear el sensor
        if cantidad_sensores == 1:    
            mapa [4] [2] = str(sensor_a[0])
            mapa [4] [3] = str(sensor_a[1])
            mapa [4] [4] = str(sensor_a[2])
            mapa [5] [2] = str(sensor_b[0])
            mapa [5] [3] = str(sensor_b[1])
            mapa [5] [4] = str(sensor_b[2])
            mapa [6] [2] = str(sensor_c[0])
            mapa [6] [3] = str(sensor_c[1])
            mapa [6] [4] = str(sensor_c[2])
            mostrar_sensor1 = [suma_sensor,3,5,"Distancia: 8"]
            
            x = mostrar_sensor1 [1]
            y = mostrar_sensor1 [2]
            a = sensor_a [0]
            b = sensor_a [1]
            c = sensor_a [2]
            d = sensor_b [0]
            e = sensor_b [1]
            f = sensor_b [2]
            g = sensor_c [0]
            h = sensor_c [1]
            i = sensor_c [2]
            sensor_3x3(cantidad_sensores,x,y,a,b,c,d,e,f,g,h,i)

        if cantidad_sensores == 2:    
            mapa [1] [9] = str(sensor_a[0])
            mapa [1] [10] = str(sensor_a[1])
            mapa [1] [11] = str(sensor_a[2])

            mapa [2] [9] = str(sensor_b[0])
            mapa [2] [10] = str(sensor_b[1])
            mapa [2] [11] = str(sensor_b[2])

            mapa [3] [9] = str(sensor_c[0])
            mapa [3] [10] = str(sensor_c[1])
            mapa [3] [11] = str(sensor_c[2])    
            mostrar_sensor2 = [suma_sensor,10,2,"Distancia: 12"]
            
            x = mostrar_sensor2 [1]
            y = mostrar_sensor2 [2]
            a = sensor_a [0]
            b = sensor_a [1]
            c = sensor_a [2]
            d = sensor_b [0]
            e = sensor_b [1]
            f = sensor_b [2]
            g = sensor_c [0]
            h = sensor_c [1]
            i = sensor_c [2]
            sensor_3x3(cantidad_sensores,x,y,a,b,c,d,e,f,g,h,i)

        if cantidad_sensores == 3:    
            mapa [4] [15] = str(sensor_a[0])
            mapa [4] [16] = str(sensor_a[1])
            mapa [4] [17] = str(sensor_a[2])

            mapa [5] [15] = str(sensor_b[0])
            mapa [5] [16] = str(sensor_b[1])
            mapa [5] [17] = str(sensor_b[2])

            mapa [6] [15] = str(sensor_c[0])
            mapa [6] [16] = str(sensor_c[1])
            mapa [6] [17] = str(sensor_c[2])
            mostrar_sensor3 = [suma_sensor,16,5,"Distancia: 21"]

            x = mostrar_sensor3 [1]
            y = mostrar_sensor3 [2]
            a = sensor_a [0]
            b = sensor_a [1]
            c = sensor_a [2]
            d = sensor_b [0]
            e = sensor_b [1]
            f = sensor_b [2]
            g = sensor_c [0]
            h = sensor_c [1]
            i = sensor_c [2]
            sensor_3x3(cantidad_sensores,x,y,a,b,c,d,e,f,g,h,i)

        if cantidad_sensores == 4:    
            mapa [11] [9] = str(sensor_a[0])
            mapa [11] [10] = str(sensor_a[1])
            mapa [11] [11] = str(sensor_a[2])

            mapa [12] [9] = str(sensor_b[0])
            mapa [12] [10] = str(sensor_b[1])
            mapa [12] [11] = str(sensor_b[2])

            mapa [13] [9] = str(sensor_c[0])
            mapa [13] [10] = str(sensor_c[1])
            mapa [13] [11] = str(sensor_c[2])
            mostrar_sensor4 = [suma_sensor,10,12,"Distancia: 21"]

            x = mostrar_sensor4 [1]
            y = mostrar_sensor4 [2]
            a = sensor_a [0]
            b = sensor_a [1]
            c = sensor_a [2]
            d = sensor_b [0]
            e = sensor_b [1]
            f = sensor_b [2]
            g = sensor_c [0]
            h = sensor_c [1]
            i = sensor_c [2]
            sensor_3x3(cantidad_sensores,x,y,a,b,c,d,e,f,g,h,i)

        if cantidad_sensores == 5:    
            mapa [16] [2] = str(sensor_a[0])
            mapa [16] [3] = str(sensor_a[1])
            mapa [16] [4] = str(sensor_a[2])

            mapa [17] [2] = str(sensor_b[0])
            mapa [17] [3] = str(sensor_b[1])
            mapa [17] [4] = str(sensor_b[2])

            mapa [18] [2] = str(sensor_c[0])
            mapa [18] [3] = str(sensor_c[1])
            mapa [18] [4] = str(sensor_c[2])
            mostrar_sensor5 = [suma_sensor,3,17,"Distancia: 20"]

            x = mostrar_sensor5 [1]
            y = mostrar_sensor5 [2]
            a = sensor_a [0]
            b = sensor_a [1]
            c = sensor_a [2]
            d = sensor_b [0]
            e = sensor_b [1]
            f = sensor_b [2]
            g = sensor_c [0]
            h = sensor_c [1]
            i = sensor_c [2]
            sensor_3x3(cantidad_sensores,x,y,a,b,c,d,e,f,g,h,i)

        if cantidad_sensores == 6:    
            mapa [16] [15] = str(sensor_a[0])
            mapa [16] [16] = str(sensor_a[1])
            mapa [16] [17] = str(sensor_a[2])

            mapa [17] [15] = str(sensor_b[0])
            mapa [17] [16] = str(sensor_b[1])
            mapa [17] [17] = str(sensor_b[2])

            mapa [18] [15] = str(sensor_c[0])
            mapa [18] [16] = str(sensor_c[1])
            mapa [18] [17] = str(sensor_c[2])
            mostrar_sensor6 = [suma_sensor,16,17,"Distancia: 33"]

            x = mostrar_sensor6 [1]
            y = mostrar_sensor6[2]
            a = sensor_a [0]
            b = sensor_a [1]
            c = sensor_a [2]
            d = sensor_b [0]
            e = sensor_b [1]
            f = sensor_b [2]
            g = sensor_c [0]
            h = sensor_c [1]
            i = sensor_c [2]
            sensor_3x3(cantidad_sensores,x,y,a,b,c,d,e,f,g,h,i)

        cantidad_sensores += 1

    #Muestro por pantalla el mapa de Gotham
    print ("────────────────────────────────────────")
    for index in mapa: 
        print ("|".join(index))
        print ("────────────────────────────────────────")
    print()

    #Busco el de la suma de sensores 3x3 el mas grande
    s1 = mostrar_sensor1 [0]
    s2 = mostrar_sensor2 [0]
    s3 = mostrar_sensor3 [0]
    s4 = mostrar_sensor4 [0]
    s5 = mostrar_sensor5 [0]
    s6 = mostrar_sensor6 [0]
    
    s7 = [s1,s2,s3,s4,s5,s6]
    
    if  s1 > s2 and  s1 > s3 and s1 > s4 and s1 > s5 and s1 > s6:
        if s7.count(s1) == 1:
            print (f"\nEL NIVEL DE ALERTA SENSOR 1 ES EL MAS ALTO: {mostrar_sensor1 [0] }.")
            print (f"LAS CORDENADAS SON X: {mostrar_sensor1 [1]}  Y; {mostrar_sensor1 [2]}.")
            print (f"LA {mostrar_sensor1 [3]} Km.")
        else:
            print ("DOS SENSORES O MAS ESTAN MIDIENDO LO MISMO, REFRESCA LA PANTALLA.")

    elif s2 > s3 and s2 > s4 and s2 > s5 and s2 > s6:
        if s7.count(s2) == 1:
            print (f"\nEL NIVEL DE ALERTA SENSOR 2 ES EL MAS ALTO: {mostrar_sensor2 [0]}.")
            print (f"LAS CORDENADAS SON X: {mostrar_sensor2 [1] }  Y: {mostrar_sensor2 [2]}.")
            print (f"La {mostrar_sensor2 [3] } Km.")
        else:
            print ("DOS SENSORES O MAS ESTAN MIDIENDO LO MISMO, REFRESCA LA PANTALLA.")

    elif s3 > s4 and s3 > s5 and s3 > s6:
        if s7.count(s3) == 1:
            print (f"\nEL NIVEL DE ALERTA SENSOR 3 ES EL MAS ALTO: {mostrar_sensor3 [0]}.")
            print (f"LAS CORDENADAS SON X: {mostrar_sensor3 [1]}  Y: {mostrar_sensor3 [2]}.")
            print (f"La {mostrar_sensor3 [3]} Km.")
        else:
            print ("DOS SENSORES O MAS ESTAN MIDIENDO LO MISMO, REFRESCA LA PANTALLA.")

    elif s4 > s5 and s4 > s6:
        if s7.count(s4) == 1:
            print (f"\nEL NIVEL DE ALERTA SENSOR 4 ES EL MAS ALTO: {mostrar_sensor4 [0]}.")
            print (f"LAS CORDENADAS SON X: {mostrar_sensor4 [1]}  Y: {mostrar_sensor4 [2]}.")
            print (f"La {mostrar_sensor4 [3]} Km.")
        else:
            print ("DOS SENSORES O MAS ESTAN MIDIENDO LO MISMO, REFRESCA LA PANTALLA.")

    elif s5 > s6:
        if s7.count(s5) == 1:
            print (f"\nEL NIVEL DE ALERTA SENSOR 5 ES EL MAS ALTO: {mostrar_sensor5 [0]}.")
            print (f"LAS CORDENADAS SON X: {mostrar_sensor5 [1]}  Y: {mostrar_sensor5 [2]}.")
            print (f"La {mostrar_sensor5 [3]} Km.")
        else:
            print ("DOS SENSORES O MAS ESTAN MIDIENDO LO MISMO, REFRESCA LA PANTALLA.")

    else :
        if s7.count(s6) == 1:
            print (f"\nEL NIVEL DE ALERTA SENSOR 6 ES EL MAS ALTO: {mostrar_sensor6 [0]}.")
            print (f"LAS CORDENADAS SON X: {mostrar_sensor6 [1]}  Y: {mostrar_sensor6 [2]}.")
            print (f"La {mostrar_sensor6 [3]} Km.")
        else:
            print ("DOS SENSORES O MAS ESTAN MIDIENDO LO MISMO, REFRESCA LA PANTALLA.")

    salir = input ("PARA REFRESCAR LOS SENSORES PULSA ENTER, PARA SALIR ESCRIBE SALIR Y PULSA ENTER ")
    salir = str(salir).upper()
