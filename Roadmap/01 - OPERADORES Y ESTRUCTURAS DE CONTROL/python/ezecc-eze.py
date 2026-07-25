# operadores aritmeticos

print(5+2)  # suma
print(5-2)  # resta
print(5*2)  # multi
print(5/2)  # division
print(5 % 2)  # devuelve lo que sobra de la division entera
print(5//2)  # devuelve division sin decimales
print(5**2)  # exponente
# primero resuelve el exponente, luego la multi,despues la division , la suma y por ultimo la resta
print(5**2+3-5*4/2)
print("hola " + "python ")  # suma los str
print("hola " + str(2))  # suma el hola y el 2 lo convertimos a str
print("hola "*3)  # imprime el hola 3 veces

# operadores comparativos

print(5 > 2)
print(5 < 2)
print(5 >= 2)
print(5 <= 2)
print(5 == 2)
print(5 != 2)
print("soy" < "eze")  # compara un orden alfabetico
print(len("eze") >= len("quiel"))  # cuenta caracteres

# operadores logicos

print(5 < 2 and 7 < 5)
print(5 > 2 and 7 > 5)
print(5 > 2 or 5 == 5)
print(5 > 2 and 6/2)
print(5 > 2 and 8/2 == 4)
print(5 > 2 and 5 == 5 or "eze" < "soy")
print(not (5 > 2))

#operadores de asignacion

numerito = 5 # asignacion
print(numerito)
numerito += 2 #suma y asignacion
print(numerito)
numerito -= 2 #resta y asignacion
print(numerito)
numerito *= 2 #multi y asignacion
print(numerito)
numerito /= 2 #divi y asignacion
print(numerito)
numerito %= 2 #modulo y asignacion
print(numerito)

#operadores de identidad

mi_numero = 1.0
print(mi_numero is 1.0)
print(mi_numero is not numerito)

#operadores de pertenencia

print(f"'u' in 'auto' ={'u' in 'auto'}") 
print(f"'u'  not it 'auto' ={'u' not in 'auto'}") 

#operadores de bit

ope = 10 #1010
oper = 3  #0011

print(f"AND: 10 & 3 = {10 & 3}") #0010 #and : si ambos bit son 1 el bit resultante es 1 de lo contrario es 0
print(f"OR: 10 & 3 = {10 | 3}") #1011 #or: si al menos 1 de los bit es 1 , el resultado es 1
print(f"XOR: 10 & 3 = {10 ^ 3}") #1001 #xor: si los bit son diferentes el resultado es 1 , si los bit son iguales el resultado es 0
print(f"not: ~10 = {~10}") #1001 # not: intercambia el valor bit a bit de cualquiera de los elementos
print(f"desplazamiento a la derecha: 10 >> 2 = {10 >> 2}") # 0010
print(f"desplazamiento a la izquierda: 10 << 2 = {10 << 2}") # 101000


# estructuras de control
# condicinales

velocidad_auto_1 = 70
if velocidad_auto_1 < 120 and velocidad_auto_1 > 60:
    print("velocidad permitida:puede circular")
elif velocidad_auto_1 == 60:
    print("circula al limite minimo")
elif velocidad_auto_1 == 120:
    print("circula al limite maximo")
else:
    print("no esta en el rango disponible para circular")

velocidad_auto_1 = ""

if not velocidad_auto_1:
    print("el auto no esta en marcha")
#iterativas

for velocidadess in range(60, 70):
    print(velocidadess)


# loops

mi_auto_nuevo = 100
while mi_auto_nuevo < 120:
    print(mi_auto_nuevo)
    mi_auto_nuevo += 5
else:
    print("'mi_auto_nuevo' no se encuentra en el rango")

while mi_auto_nuevo < 150:
    print(mi_auto_nuevo)
    mi_auto_nuevo += 5
    if mi_auto_nuevo == 130:
        print("mi auto supera lo permitido:bajar velocidad")
        break
print(mi_auto_nuevo)

velocidades_de_hoy = [67, 75, 90, 90, 103, 125, 115]
for velocidades in velocidades_de_hoy:
    print(velocidades)
    if velocidades == 103:
        break
    print(" no supera los 103")

else:
    print("los autos no vuelan")

# excepciones

giro = 180
dobla = 90
giro = "un u"

try:
    print(giro + dobla)
    print("todo bien")
except:
    print("se ha producido un error")
else:
    print("la ejecucion sigue correctamente")
finally:
    print("sigue funcionando")

#extra

for numeros_validos in range (10, 55):
    if numeros_validos == 16:
        continue
    if numeros_validos % 3 != 0 and numeros_validos % 2 == 0:
        print(numeros_validos) 
        
