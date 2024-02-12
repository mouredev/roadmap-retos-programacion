'''

# #04 CADENAS DE CARACTERES
> #### Dificultad: Media | Publicación: 22/01/24 | Corrección: 29/01/24

## Ejercicio

```
/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */
```
#### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.

Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

> Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.


'''

# Conversión a Mayúscula.
cadena = "Esto Es Una Cadena De Caracteres Mi Telefono es 777888999"
mayuscula = cadena.upper()
print ("")
print (mayuscula)

# Conversión a Minuscula.
cadena2 = "Esto Es Una Cadena De Caracteres"
cadena2 = cadena2.lower()
print ("")
print (cadena2)

# Conteo de digitos de la cadena
cadena3 = "Esto Es Una Cadena De Caracteres"
cadena3 = len(cadena3)
print ("")
print (cadena3)

# Conteo de digitos de la cadena
cadena4 = "Esto Es Una Cadena De Caracteres"
cadena4 = len(cadena4)
print ("")
print (cadena4)

# Conteo de digitos de la cadena
cadena5 = "Esto Es Una Cadena De Caracteres "
cadena6 = "concatenamos otra cadena más"
concatenado = cadena5 + cadena6
print ("")
print (concatenado)

# Subcadenas.
cadena7 = "Esto es una cadena para tratar los substrigs"
pos1 = 1
pos2 = 3
subcadena = cadena7[pos1:pos2]
print ("")  
print (subcadena)

# Repeticion de cadenas.
cadena8 = "Esta es la cadena para el ejemplo de repeticion de cadenas - "
print ("")
cadena9 = cadena8 * 4
print (cadena9)

# Recorridos de variables strings.
cadena10 = "Recorrido de variables"
print ("")
for x in cadena10:
    print (x)

# Reemplazo.
cadena11 = "Reemplazo en variables , Reemplazo"
nuevacadena = cadena11.replace("Reemplazo","Texto nuevo que reemplaza al texto Reemplazo - ")
print (nuevacadena)

# Division en cadenas string.
cadenaDivision = "Esta cadena la vamos a dividir"
dividida = cadenaDivision.split()
print ("")
print (dividida)

# Unión de cadenas string.
cadenaUnir = "Esta cadena la vamos a unir"
cadenadiv = cadenaUnir.split()
print ("")
resultado = ",".join(cadenadiv)
print (resultado)

# interpolacion de strings.
a = 2000
b = "hola"
c = "Clipper"
d = False
e = 1900

print ("")
print ("%d + 1200 = 3000" % (a))
print ("%s es un saludo incial para empezar una conversación, en Español es %s" % ("Hellow", b ))

# Verificación de palabras en strings.
print ("")
cadenaVerif = "Esta cadena es para verificar la existencia en strings"
encontrada = cadenaVerif.find("cadena")
print (encontrada) # Nos indica con un número en que posición ha encontrado la cadena, en este caso la posición 5.

