"""
EJERCICIO:
¿Has visto la camiseta.rar?
https://x.com/MoureDev/status/1841531938961592740

Crea un programa capaz de comprimir un archivo en formato .zip (o el que tú quieras).
No subas el archivo o el zip.
 """

import zipfile,os

archivo_org = input("DIME EL ARCHIVO A COMPRIMIR? <nombre.extension>: ")
archivo_zip=input ("QUE NOMBRE LE QUIERES PONER AL ARCHIVO COMPRIMIDO? <nombre.zip>: ")

try:    
    
    with zipfile.ZipFile(archivo_zip, mode='w') as comprime:
        print ("\nCOMPRIMIENDO ........")
        comprime.write(archivo_org)
        print (f"\nEL ARCHIVO {archivo_org} a sido satisfactoria.")
        comprime.printdir()
except:
    os.remove(archivo_zip)
    print("\nNO SE HA PODIDO CREAR EL ARCHIVO!!!")

print()
