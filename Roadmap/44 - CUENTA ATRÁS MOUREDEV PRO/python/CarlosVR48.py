import datetime,threading,pytz
from pytz import timezone
from os import system

def muestra_tiempo():
    hora_actual_esp = datetime.datetime.now(timezone("Europe/Madrid"))
    hora_actual_utc = datetime.datetime.now(timezone("UTC"))
    print (f"DIA Y HORA UTC :       {hora_actual_utc}")
    print (f"DIA Y HORA DE ESPAÑA : {hora_actual_esp}\n")

def datos():
    salir = True
    while salir:
        print ("INTRODUCE LA FECHA Y LA HORA DE FINALIZACION \n")
        year = input ("AÑO (XXXX)? ")
        mes = input ("MES (XX)? ")
        dia = input ("DIA (XX)? ")
        hora = input ("HORA (XX)? ")
        minuto = input ("MINUTOS (XX)? ")
        segundo = input ("SEGUNDOS (XX)? ")

        try:
            fecha_final = datetime.datetime.strptime(year + mes + dia + hora + minuto + segundo , "%Y%m%d%H%M%S")
            salir = False
            return fecha_final
        except:
            print ("\nHAS INTRODUCIDO ALGUN DATO MAL")

def programa():
    system("cls")            
    muestra_tiempo()
    #FECHA FINAL INTRODUCIDA POR CONSOLA (fecha_final)
    fecha_final = datos()
    #ASSIGNO A LA VARIABLE (europa) "Europe/Madrid" . FECHA FINAL DE EUROPA ESPAÑA (fecha_local)
    europa = pytz.timezone("Europe/Madrid")
    fecha_local = europa.localize(fecha_final, is_dst=None)
    #FECHA FINALIZACION UTC (fecha_utc)
    fecha_utc = fecha_local.astimezone(pytz.utc)

    while True:
        system ("cls")
        hora_actual_utc = datetime.datetime.now(timezone("UTC"))
        tiempo_final=(fecha_utc-hora_actual_utc)

        muestra_tiempo()
        print (f"DIA Y HORA UTC DE FINALIZACION {fecha_utc} ")
        # la variable tiempo_final es del tipo timedelte, dando su valor en dias , segundos y microsegundos
        dias = tiempo_final.days
        horas = int(tiempo_final.seconds / 3600)
        minutos = int((tiempo_final.seconds % 3600) / 60)
        segundos = int(tiempo_final.seconds % 3600) % 60
        print (f"\n{dias} dias , {horas} h , {minutos} minutos y {segundos} segundos \n")
        
        if hora_actual_utc >= fecha_utc :
            system("cls")
            print (f"DIA Y HORA UTC DE FINALIZACION {fecha_utc} \n")
            print ("LA CUENTA A FINALIZADO")
            break

principal = threading.Thread(target=programa)
principal.start()




        

