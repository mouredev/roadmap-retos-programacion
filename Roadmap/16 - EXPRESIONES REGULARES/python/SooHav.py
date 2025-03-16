# 16 EXPRESIONES REGULARES

# Ejercicio

import re

patron = r"\d+((\,\d+)|(\.\d+))*"

"""\d+: Coincide con uno o más dígitos (\d). El + indica que debe coincidir al menos con un dígito.
(\,\d+)*: Este grupo de captura (...) seguido de * indica que puede coincidir cero o más veces con una coma seguida de uno o más dígitos.
(\.\d+)?: Este grupo de captura (...) seguido de ? indica que puede coincidir cero o una vez con un punto seguido de uno o más dígitos."""


txt = """A partir de la UM1, se determinó que el prototipo no presentó un offset asociado a la presión atmosférica durante el período observado, mientras que el equipo
         comercial tuvo un offset promedio de 18 mm. La repetibilidad y reproducibilidad del sistema de medición se evaluaron utilizando el método de promedios
         y rangos sugerido por Moret y Paisan (2010), con los datos de la UM2. El % de repetibilidad promedio de todos los niveles de agua resultó ser 15,430
         ligeramente mayor al % de reproducibilidad promedio (12,369). Esto indica que la variabilidad existente entre las mediciones se debe al instrumento
         en sí y/o al sistema utilizado para realizar las mediciones en los diferentes tratamientos aplicados. El porcentaje de la relación entre la repetibilidad
         y la reproducibilidad promedio R&R fue de 20,041, ubicándose entre el rango 10% y 30%. Esto implica que el sistema de medición es aceptable temporalmente,
         aunque se requieren mejoras. Se plantearon dos hipótesis: en primer lugar, puede ser necesario aumentar la tolerancia admitida (T= 10 mm) en la medición; y
         en segundo lugar, se debe revisar el sistema de medición, ya que los mejores resultados se obtuvieron en las mediciones centrales, lo que sugiere que los extremos
         podrían tener un error asociado a una mayor dificultad operativa. El sesgo de las mediciones se obtuvo a partir del método de Bland-Altman (Figura 2). A partir del
         gráfico se puede observar que el sesgo medio de los datos se mantiene cerca del cero. La mayoría de las diferencias individuales se encuentran dentro de un rango
         de confianza del 95% (± 5 mm). El 99% de los datos se encuentra dentro de las líneas establecidas como tolerancia del instrumento (± 10 mm), y todos los
         datos están dentro de la tolerancia proporcionada por el fabricante del sensor (máximo ± 50 mm para la sonda utilizada)."""

resultado = re.sub(patron, "", txt)
print(resultado)

# Extra

# Correos electronicos

patron = r"[\w\.-]+@[\w\.-]+"
mail = 'havrylenko.sb@gmail.com'

resultado = re.search(patron, mail)
if resultado:
    print(f"Mail válido: {mail}")
else:
    print(f"Mail inválido: {mail}")

# Nùmeros de telefono
patron = r"\+?\d{0,2}?-?\d{3,4}?-?\d{5,9}"

telefonos = ['+54-011-1511111111', '+54-011-11111111',
             '011-11111111', '11111111', '1511111111']

for telefono in telefonos:
    resultado = re.search(patron, telefono)
    if resultado:
        print(f"Teléfono válido: {telefono}")
    else:
        print(f"Teléfono inválido: {telefono}")

# URL

patron = r"(\www\.)[\w\.-]+"
url = "www.disneyplus.com\es"

resultado = re.search(patron, url)
if resultado:
    print(f"URL válida: {url}")
else:
    print(f"URL inválida: {url}")
