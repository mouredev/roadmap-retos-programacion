#Estructuras de datos

#En GDscript todo script tiene que estar asociado a una escena o nodo para poder ejecutarlo

extends Node
#La función _ready es una especial de GDScript que hace que la función se ejecute al momento de iniciar la ecena de forma automatica
#y solo puede ser usada una vez por script
func _ready(): #voy a utilizar esta función para llamar a todas las que haga a partir de ahora en este ejercicioç
    ##Ejemplos de estructuras
    #Arrays
    print_un_array()
    print_dos_array()
    #Diccionario
    print_diccionario()
    print_var_array_en_diccionario()
    ##Operaciones
    #Incerción
    incerción_en_array()
    #Borrado
    borrado_en_array()
    #Actualización
    actualizar_array()
    #Ordenamiento
    ordenar_array()



##Ejemplos de estructuras
#Array o arreglo
var mi_primer_array = [7, 0, "hola", true]
var array_estatico: Array[int] = [1, 2, 3 , 4, 1_800_70]

func print_un_array() -> void:
    print(mi_primer_array)
func print_dos_array() -> void:
    print(mi_primer_array + array_estatico)

#Diccionario
var mi_primer_diccionario = {
    "hola": 5,
    7:"hola",
    "nose": 1914,
    1985: mi_primer_array, #puedes agregar una variable ya echa en el diccionario
    "array_en_diccionario":[7, 57, "lobo"], #además de poder crear un nuevo array ya dentro del diccionario
    }

func print_diccionario() -> void:
    print(mi_primer_diccionario)
func print_var_array_en_diccionario() -> void:
    print(mi_primer_diccionario[1985])


##Operaciones
#en este caso voy a hacerlo unicamente con los arrays, pero con los diccionarios es practicamente lo mismo
var array_de_operaciones: Array[String] = []
var array_adicional = ["pollo", "manteca", "filistea"]
#Incerción
func incerción_en_array() -> void:
    array_de_operaciones.append("hola")
    print(array_de_operaciones)
    array_de_operaciones.append("pato")
    print(array_de_operaciones)
    array_de_operaciones.append("ganso")
    print(array_de_operaciones)
    array_de_operaciones.append_array(array_adicional) #puedes insertar el contenido de un array en otro
    print(array_de_operaciones)
    print(array_adicional)
    array_de_operaciones.insert(4, "ganso") #tambien puedes reemplazar un dato en la pocición deseada
    print(array_de_operaciones)

#Borrado
func borrado_en_array() -> void:
    array_de_operaciones.erase("hola")
    print(array_de_operaciones)
    array_de_operaciones.erase(array_de_operaciones[0])
    print(array_de_operaciones)

#Actualización
func actualizar_array() -> void:
    array_de_operaciones[1] = "merengue"
    print(array_de_operaciones)

#Ordenamiento
func ordenar_array() -> void:
    array_de_operaciones.reverse() #sentido inverso
    print(array_de_operaciones)
    array_de_operaciones.sort() #de mayor a menor u orden alfabetico
    print(array_de_operaciones)
    array_de_operaciones.shuffle() #orden aleatorio
    print(array_de_operaciones)


##Extra
#Por limitaciones del lenguaje y de la modalidad de la Road map no puedo hacer el extra
#ya que requeriría crear un archivo de Escena para vincularlo con el script y poder ejecutarlo
#además de que GDScript está pensado para usarse con el editor Godot para videojuegos y aplicaciones con entorno gráfico
#desconozco de momento si hay alguna otra manera de hacerlo
#todo esto sin contar mi desconocimiento sobre el uso de terminal con GDScript
#si en algún momento a futuro encuentro la forma lo haré ya que es muy similar a lo que tendrías que hacer
#en un lenguaje como Phyton cosa que es sencilla 