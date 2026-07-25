a= 5
b= 3

#* operadores aritmeticos
def aritmeticos():
  suma= a+b
  resta = a-b
  multiplicacion= a*b
  divicion= a/b
  resto= a%b
  print("\t operadores aritmeticos")
  print(a," + ",b," = ",suma)
  print(a," - ",b," = ",resta)
  print(a," * ",b," = ",multiplicacion)
  print(a," / ",b," = ",divicion)
  print(a," % ",b," = ",resto)

#* operaciones logicos
def logicos():
  verdadero= True
  falso = False
  and_logico = verdadero and verdadero
  or_logico = verdadero and falso
  negacion = not verdadero
  print("\t operadores logicos")
  print("verdadero: ", verdadero)
  print("falso: ",falso)
  print(verdadero," and ",verdadero," = ", and_logico)
  print(verdadero," or ",falso," = ", or_logico)
  print("not ",verdadero)

#* operadores de comparacion
def comparacion():
  mayor= a>b
  menor = a<b
  igual = a==b
  diferente = a != b
  mayor_igual = a>=b
  menor_igual = a<=b
  print("\t operadores de comparacion")
  print(a," > ",b," = ",mayor)
  print(a," < ",b," = ",menor)
  print(a," == ",b," = ",igual)
  print(a," != ",b," = ",diferente)
  print(a," >= ",b," = ",mayor_igual)
  print(a," <= ",b," = ",menor_igual)

#* asignacion
def asigacion():
  n=0
  print("\t asignacion")
  print("n= ",n)
  print("se le asignara a n el numero 5")
  n=5
  print("ahora n= ",n)

#*operadores de identidad
def identidad():
 c=10
 d=10
 arr_1=[1,2,3]
 arr_2=[1,2,3]
 print("\t operadores de identidad ")
 print (c," is ", d," = ",(c is d))
 print (arr_1," is ", arr_2," = ",(arr_1 is arr_2))
 """
 'is' verifica si ambos utilizan el mismo onbjero (el mismo espacio de memoria para almacenar  que sean iguales , no significa que utilicen el mismo espacio de memoria , como el ejemplo del array
 """

 # is not, es lo contrario a is
 print (c," is not ", d," = ",(c is not d))
 print (arr_1," is not ", arr_2," = ",(arr_1 is not arr_2))
 
 print("direccion de memoria a: ",id(c))
 print("direccion de memoria b: ",id(d))
 print("direccion de memoria arr_1: ",id(arr_1))
 print("direccion de memoria arr_2: ",id(arr_2))

#* operador de pertenencia
def pertenencia():
  frutas=["manzana","pera","naranja"]
  #* in : ve si el elemento que se busca enstá en el array
  print("\t pertenencia")
  print("pera in frutas = ", ("pera" in frutas))
  print("coco in frutas = ", ("coco" in frutas))
  #* not in, es lo contrario
  print("pera not in frutas= ",("pera" not in frutas))
  print("coco not in frutas= ",("coco" not in frutas))

#* operadores de bits
def bits():
  A= 1010
  B= 1011
  print("\t operadores de bits")
  print(f" {A} & {B} = {A & B}") #* AND
  print(f" {A} | {B} = {A | B}") #* OR
  print(f" {A} ^ {B} = {A ^ B}") #* XOR
  print(f" ~10 = {~10}") #* NOT
  print(f"Desplazamiento a la Derecha 10 >> 3 = {10 >> 3}")
  print(f"Desplazamiento a la Izquierda 10 << 3 = {10 << 3}")

#* estructuras de control
def estructuras_de_control():
  #* condicionales
  if(a > b):
    print(f"sumamos a + b : {a+b}")
  else:
    print(f"restamos a - b : {a-b}")
  valor =20
  resultado = "El valor es 10" if valor == 10 else "El valor es 20"
  print(resultado)
  #* ciclos
  #* for
  print("for")
  frutas=["manzana","coco","pera","platano"]
  for i in frutas:
    print(i)
  print("while")
  #* while
  contador=0
  while (contador < 2):
    print(frutas[contador])
    contador+=1

#* excepciones
# def excepciones():
 # try:
	  # Codigo a ejecutar
	  # Pero podria haber errores en este bloque
    
 # except <tipo de error>:
	  # Haz esto para manejar la excepcion
	  # El bloque except se ejecutara si el bloque try lanza un error
    
 # else:
	  # Esto se ejecutara si el bloque try se ejecuta sin errores
   
 # finally:
	  # Este bloque se ejecutara siempre

#* ejercicio extra
def extra():
  i= 10
  fin= 55
  while(i <= fin):
    if((i%2 == 0) and (i!= 16) and (i%3 != 0) or (i == fin)):
      print(i)
    i+=1

aritmeticos()
logicos()
comparacion()
asigacion()
identidad()
pertenencia()
bits()
estructuras_de_control()
# execiones()
extra()