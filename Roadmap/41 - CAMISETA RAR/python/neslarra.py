"""
 EJERCICIO:
 ¿Has visto la camiseta.rar?
 https://x.com/MoureDev/status/1841531938961592740

 Crea un programa capaz de comprimir un archivo
 en formato .zip (o el que tú quieras).
 - No subas el archivo o el zip.
"""
import gzip, os


# Comprimir
try:
    with open('reto_41_neslarra.txt', 'rb') as regular_file:
        data = regular_file.read()
        regular_file.flush()

    with gzip.open('reto_41_neslarra.txt.gz', 'wb') as compressed_file:
        compressed_file.write(data)
        compressed_file.flush()
except Exception as e:
    print(f"Exception: {str(e)}")
    os.remove("reto_41_neslarra.txt.gz")
else:
    os.remove("reto_41_neslarra.txt")

_ = input("Revisar y apretar Enter para contiuar...")

# Descomprimir
try:
    with gzip.open('reto_41_neslarra.txt.gz', 'rb') as compressed_file:
        data = compressed_file.read()
        compressed_file.flush()

    with open('reto_41_neslarra.txt', 'wb') as regular_file:
        regular_file.write(data)
        regular_file.flush()
except Exception as e:
    print(f"Exception: {str(e)}")
    os.remove("reto_41_neslarra.txt")
else:
    os.remove("reto_41_neslarra.txt.gz")
