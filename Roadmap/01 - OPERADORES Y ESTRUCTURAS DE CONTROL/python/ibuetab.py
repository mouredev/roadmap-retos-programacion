#OPERADORES

#Operadores aritméticos
suma = 2+3;
resta = 5-2;
multiplicacion= 2*5;
division = 6/2;
modulo = 10%2;
division_entera = 10 // 3;
exponente = 2**2;

print(f"Suma 2+3 = {suma}, Resta 5-2 = {resta}, Multiplicación 2*5 = {multiplicacion}, División 6/2 = {division}, Módulo 10%2 = {modulo}, División entera 10 // 3 = {division_entera}, Exponente 2**2 = {exponente}");


#Operadores de asignación
operador_asignacion = 2;
print(operador_asignacion);
operador_asignacion += 1;
print(operador_asignacion);
operador_asignacion -= 1;
print(operador_asignacion);
operador_asignacion *= 2;
print(operador_asignacion);
operador_asignacion /= 2;
print(operador_asignacion);
operador_asignacion %= 2;
print(operador_asignacion);
operador_asignacion //= 2;
print(operador_asignacion);
operador_asignacion ** 2;
print(operador_asignacion);


#Operadores lógicos
operador_and = 3 < 5 and 2 < 4;
operador_or = 2 > 1 or 5 < 3;
operador_not = not(3 < 5 and 12 > 16);

print(f"AND = {operador_and}, OR = {operador_or}, NOT = {operador_not}");


#Operadores de comparación
variable_int = 10;
print(f"Igualdad: {variable_int==10}, Diferente: {variable_int!=10}, Mayor que: {variable_int > 10}, Menor que: {variable_int < 10}, Mayor o igual: {variable_int >= 10}, Menor o igual: {variable_int <= 10}   ");


#Operadores de identidad
cadena = "Hola Mundo";
cadena_2 = "Hola";
print(f"{cadena is cadena_2}");
print(f"{cadena is not cadena_2}");

#Operadores de pertenencia
print(f"{cadena_2 in cadena}");
print(f"{cadena_2 not in cadena}");

#Operadores bit
a = 10;
b =2;
print(f"AND {a & b}");
print(f"{a | b}");
print(f"{a ^ b}");
print(f"{~a}");
print(f"{a << 2}");
print(f"{a >> 2}");

#-------------------------------------------------------------------------------------------------------------------------------------------------------

#ESTRUCTURAS DE CONTROL

#Condicionales
variable_condicional = 2;

if(variable_condicional == 2):
    print("Igual");
elif(variable_condicional < 3):
    print("Verdadero");
else:
    print("Falso");

#Bucles
for i in range(11): #Imprime del 1 al 10 contando el 0
    print(i);


for i in range(1,10+1): #Imprime del 1 al 10 sin contar el 0
    print(i);
 
#Imprime del 1 al 10 contando el 0
i=0; 
while i <= 10:
    print(i);
    i+=1;

#Imprime del 1 al 10 sin contar el 0
i=1; 
while i <= 10:
    print(i);
    i+=1;

#Do-While emulado
counter = 0;
while True:
    print("Hola");
    counter += 1;
    if counter > 5:
        break;

#Excepciones
try:
    print(5/0);
except:
    print("No se puede dividir entre 0");
finally:
    print("Programa finalizado");


#EXTRA
for i in range(10,55+1):
    if(i % 2 == 0 and i != 16 and i % 3 != 0 ):
        print(i);




