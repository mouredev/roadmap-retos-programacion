#https://godotengine.org/

#En GDscript es un comentario todo lo que esté en la misma linea del # a partir de este
# Para cada linea hay que poner uno nuevo

#variable y constante
var variable_jamón = "bueno"
const constante_queso = "exelente"

#variable null
var variable_null = null

#variables booleanas o bool
var booleano_verdadera : bool = true
var booleano_falso : bool = false
var numero_verdadero : bool = 1 #cualquiern numero mayor a 0 es verdadero
var numero_falso : bool = 0

#variables enteras o int
var variable_positiva : int = 1
var variable_negativa : int = -70

#variables flotantes on float
var flotante_positiva : float = 1.5
var flotante_negativa : float = -27.591

#variable de tipo texto o string
var texto_cualquiera : string = "cualquiera"

#en GDscript todo script tiene que estar asociado a una escena o nodo para poder ejecutarlo
#función de print
func _ready():
    var saludo : string = "¡Hola "
    const lenguaje : string = "GDscript!"
    print (saludo + lenguaje) # "," = "+"