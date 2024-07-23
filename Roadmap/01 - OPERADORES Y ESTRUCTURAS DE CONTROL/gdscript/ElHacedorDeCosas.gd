# Operadores

#en GDscript todo script tiene que estar asociado a una escena o nodo para poder ejecutarlo

#Operadores Aritméticos
extends Node
func _ready(): #la función _ready hace que la función se ejecute al momento de iniciar la ecena y solo puede ser usada una vez por script
    #suma
    print(10 + 3)
    #resta
    print(10 - 3)
    #multiplicación
    print(10 * 3)
    #división
    print(10 / 3.0) #si no se especifica que uno de los dos numeros es flotante te dará siempre como resultado un entero
    print(10 / float(3)) #se puede hacer de estas dos formas
    #modulo o resto
    print(10 % 3)
    #potencia
    print(10 ** 3)

#Operadores de comparación
extends Node
func _ready():
    var x = 2
    print ("x = " + str(x)) #para poder hacer print a una variable de tipo texto y una de tipo booleano a la vez
    #Igualdad               # tienes que convertir esta a texto
    print("x == 10 = " + str(x == 10))
    #Desigualdad
    print("x != 10 = " + str(x != 10))
    #Mayor que
    print("x > 10 = " + str(x > 10))
    #Menor que
    print("x < 10 = " + str(x < 10))
    #Mayor o igual que
    print("x >= 10 = " + str(x >= 10))
    #Menor o igual que
    print("x <= 10 = " + str(x <= 10))

#Operadores lógicos
extends Node
func _ready():
    # "and" o "&&"
    print("(2 > 3 and 4 + 3 = 7)= " + str(2 > 3 and (4 + 3 == 7)))
    # "or" o "||"
    print("(2 > 3 or 4 + 3 = 7)= " + str(2 > 3 or (4 + 3 == 7)))
    # "not" o "!"
    print("not 3 > 2 = " + str(not 3 > 2))

#Operadores de asignación
#Las asignaciones en GDScript no pueden estar dentro de expreciones 
extends Node
func _ready():
    #Asignación
    var y = 7
    #Suma y asignación
    y += 2
    print(y)
    #Resta y asignación
    y -= 2
    print(y)
    #Multiplicación y asignación
    y *= 2
    print(y)
    #División y asignación
    y /= 2
    print(y)
    #Resto y asignación
    y %= 2
    print(y)
    #Exponente y asignación
    y **= 2
    print(y)

#Operadores de pertenencia
extends Node
func _ready():
	# in
    print("u in pablo = " + str("u" in "pablo"))
    print("a in pablo = " + str("a" in "pablo"))
    # not in
    print("u not in pablo = " + str("u" not in "pablo"))
    print("a not in pablo = " + str("a" not in "pablo"))

#Operadores de bit
extends Node
func _ready():
    var numero_uno = 10 #1010
    var numero_dos = 5  #0101
    # "&" o "AND"
    print("10 & 5 = " + str(numero_uno & numero_dos)) #0  = 0000
    # "^" o "XOR"
    print("10 ^ 5 = " + str(numero_uno ^ numero_dos)) #15 = 1111
    # "|" o "OR"
    print("10 | 5 = " + str(numero_uno | numero_dos)) #15 = 1111
    # "~" o "NOT"
    print("~10 = " + str(~numero_uno)) #-11
    # Desplazamiento a la derecha o ">>"
    print("10 >> 3 = " + str(numero_uno >> 3)) #1  = 0000001
    # Desplazamiento a la izquierda o "<<"
    print("10 << 3 = " + str(numero_uno << 3)) #80 = 1010000

#Estructuras de control

#Condicionales
extends Node
var edad = 21
func _ready():
    #Condicional "si" o "if"
    if (edad < 18):
        print ("eres menor de edad")
    #Condicional "sino, si" o "elif"
    elif (edad > 29):
        print("eres un adulto")
    #Condicional "sino" o "else"
    else: print("eres un joven adulto")

#Iterativas
extends Node 
func _ready():
    for i in 7:
        print(i)
    for i in range(7):
        print(i)
    #while
    var i = 0
    while (i< 12):
        print(i)
        i += 2
    
#Excepciones
#GDScript no maneja execpriones y la explicaciñon sacada de la pagina de GDScript es la siguiente:
#"Creemos que los juegos no deben fallar no importa la situación. Si una situación inesperada sucede,
#Godot mostrara un error (el cual puede incluso llevarte al script),
#pero seguidamente intentara recuperarse lo mejor posible y continuar en la medida de lo posible."


#Ejercicio extra
extends Node
func _ready():
    for numero in range(10, 56, 2): #en el rango entre 10 y 56 avanza cada 2 numeros
        if numero != 16 and numero % 3 != 0:
            print(numero)
