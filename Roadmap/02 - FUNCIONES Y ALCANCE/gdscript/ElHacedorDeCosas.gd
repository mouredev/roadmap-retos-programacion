#Funciones

#en GDscript todo script tiene que estar asociado a una escena o nodo para poder ejecutarlo

#Funciones basicas
extends Node
#la función _ready es una especial de GDScript que hace que la función se ejecute al momento de iniciar la ecena de forma automatica
#y solo puede ser usada una vez por script
func _ready(): #voy a utilizar esta función para llamar a todas las que haga a partir de ahora en este ejercicio
    #Simple
    simple()
    #Con retorno
    con_retorno()
    resultado()
    #Con argumento 
    con_argumento("Hola", "tito")
    #Con argumento predeterminado
    con_argumento_predeterminado(67, 10)
    #Variables globales y locales
    global_print()
    local_print()
    #Extra
    ejercicio_extra("papa","boniato")

#Simple
func simple() -> void:
    print(4 + 2)

#Con retorno
var a = 3
var b = 7
func con_retorno() -> int:
    return a + b
func resultado() -> void:
    var resultados = con_retorno()
    print(resultados)

#Con argumento
func con_argumento(primero : String, segundo : String) -> void:
    print(primero + " " + segundo)

#Con argumento predeterminado
func con_argumento_predeterminado(c :int =3 , d :int =4) -> void:
    print(c + d)

#Variables globales y locales
#global
var variable_global = "Timo"
func global_print() -> void:
    print(variable_global)
#local
func local_print() -> void:
    var variable_local = "123456"
    print(variable_local)


#Extra

func ejercicio_extra(texto1, texto2) -> int:
    var numero_de_impresiones = 0
    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(texto1 + texto2)
        elif numero % 3 == 0:
            print(texto1)
        elif numero % 5 == 0:
            print(texto2)
        else:
            print(numero)
            numero_de_impresiones += 1
    print(numero_de_impresiones)
    return numero_de_impresiones