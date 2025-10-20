# INFO PARA EJECUTAR ESTE CODIGO SIN ASIGNARLO A UN NODO SE AGREGA EL <<@tool>>,
# SE HEREDA CON <<extends EditorScript>> Y SE USA LA FUNCION <<func _init() -> void:>>
# PUEDES HACERLO PRESIONANDO <<File -> Run o (Ctrl+Shift+X)>>. YA LO IDEAL SERIA CREAR
# UNA ESCENA JUNTO A UN NODO Y A ESTE ASIGNALE UN SCRIPT PARA EMPEZAR A ENTENDER COMO
# FUNCIONA GODOT Y SU SITESTEMA DE NODES Y SCENES. 

# NOTE Este ejemplo se encuentra en la version de GODOT 4.5
 
@tool

# Sitio Oficial de GODOT (GDScript) https://godotengine.org/


extends EditorScript # El comentario tampien puede ir despues e una linea de codigo

#region TIPOS_DE_COMENTARIOS
# Este es un comentario de una sola linea,
# para cada linea nueva que se requiera comentar,
# se ocupa iniciar con (#) y siempre tiene que  
# tener un espacio despues del (#), por convención.

# Tambien estan los comentario de region de codigo,
# si inician con #region y se finalizan con #endregion,
# como en este ejemplo. Estos sirven para agrupar partes 
# del código y poder plegarlas (fold/unfold) fácilmente en el editor.

## Tambien estan los comentarios de documentación:
# Son comentarios especiales en GDScript que se escriben con doble almohadilla (##).
# El motor de Godot los usa para generar documentación que aparece como ayuda en el
# editor cuando pasas el cursor sobre una clase, variable o función. Sirven para 
# explicar el propósito del código y facilitar su comprensión a otros programadores.

"""
Esto parece un comentario multilínea
pero realmente es un string que no se usa.
Godot lo ignora, aunque existe en memoria.
"""
'''
Esto tambien parece un comentario multilínea
pero realmente es un string que no se usa.
Godot lo ignora, aunque existe en memoria.
La diferencia es que se usan comillas simples.
'''

# WARNING: Los dos ejemplos anteriores, se usan para
# documentacion temporal pero NO son comentarios
# oficiales, y recuarda que usan espacio en memoria.
#endregion FIN_TIPOS_DE_COMENTARIOS

#region VARIABLES
# Las variables son espacios en memoria con un nombre y dato (valor asignado).
# En GDScript una variable se declara con la palabra reservada <<var>>.
# La sintaxis es la siguiente:
# <<var>> "espacio" + <<nombre_variable>> "espacio" + <<=>> "espacio" + <<valor>>
# para el nombre de la variable se usa por convencion <<snake_case>>.

var nombre_jugador = "NicDev95"
var vida_jugador = 100

# NOTE: Una variable puede cambiar su valor asignado en tiempo de ejcucion del
# script o  programa, por lo tanto aunque nombre_juagdor su valor inicial es NicDev95, mas
# adelante podria ser MoureDev, por ejemplo, y vida_jugador ser 50.
#endregion FIN_DE_VARIABLES

#region CONSTANTES
# Las CONSTANTES son espacios en memoria con un nombre y dato (valor asignado)
# En GDScript una constante se declara con la palabra reservada <<const>>.
# La sintaxis es la siguiente:
# <<const>> "espacio" + <<NOMBRE_CONSTANTE>> "espacio" + <<=>> "espacio" + <<valor>>
# para el nombre de la variable se usa por convencion <<SNAKE_UPPERCASE>>.

const NOMBRE_JUGADOR = "NicDev95"
const VIDA_INICIAL = 100

# NOTE: Una constante NO puede cambiar su valor asignado en tiempo de ejcucion del
# script o programa, por lo tanto NOMBRE_JUGADOR siempre sera NicDev95, si se quisiera 
# cambiar el valor de una constante seria antes de ejecutar el script o preograma.
#endregion FIN_DE_CONSTANTES

#region TIPOS_DATOS_PRIMITIVOS
# Son los tipos básicos con los que se construyen todos
# los demás tipos de datos y estructuras.

# Son los siguientes:
var tiempo # Variable con dato nulo "es una variable sin valor asignado".
var esta_vivo: bool = true # Variable con dato bolena true/false.
var vida_inicial: int = 3 # Variable con dato entero 1, 200, -35, etc.
var velocidad: float = 2.5 # Variable con dato con punto flotante -3.1, 6.6, etc.
var lenguaje: String = "GDScript" # Variable con dato de cadena de texto "HOLA", "adios 55".
var clave: StringName = &"mi_variable" # Variable con dato cadena de texto que se usa como ID.
var ruta: NodePath = ^"Jugador/Arma" # Variable con dato que basicamente es la ruta del node.

# Existen mas tipos de datos que se pueden 
# asignar a una variable o contante pero  
# estos son los primitivos o basicos.
#endregion FIN_TIPOS_DATOS_PRIMITIVOS

#region IMPRIMIR_EN_CONSOLA
func _init() -> void:
	print("Hola, " + lenguaje)
#endregion FIN_IMPRIMIR_EN_CONSOLA
