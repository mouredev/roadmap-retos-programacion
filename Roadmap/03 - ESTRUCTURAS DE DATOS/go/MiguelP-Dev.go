package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"sync"
	"unicode"
)

// ordenamiento de un sync.Map
// Pair representa pares claves-valor
type Pair struct {
	key   string
	value int
}

// PairList es un slice de pares
type PairList []Pair

// Implementando la interface de ordenamiento para la pairList
func (p PairList) Len() int {
	return len(p)
}

func (p PairList) Swap(i, j int) {
	p[i], p[j] = p[j], p[i]
}

func (p PairList) Less(i, j int) bool {
	return p[i].value < p[j].value
}

func main() {
	// Array(Arreglos): Los array son un tipo de estructura fundamental en golang, aunque tienen sus limitaciones,
	// debido a su tamaño fijo, se pueden realizar algunas operaciones utiles con arrays.
	// Nota: Esta estractura manejas índice y valor, pero siempre del mismo tipo de valor.

	// Declaración
	var myArray [5]string
	fmt.Println("Declaración: ", myArray)

	// Inicialización
	var myArray2 = [5]int{10, 20, 30, 40, 50}
	fmt.Println("Inicialización: ", myArray2)

	// Acceso
	myArray[0] = "Miguel"
	myArray[2] = "Portillo"
	fmt.Println("Acceso a myArray: ", myArray[0])

	// Modificación
	myArray2[0] = 100
	fmt.Println("Modificación myArray2: ", myArray2[:])

	// Iteración con bucle for
	fmt.Println("Iteración con bucle for")
	for i := 0; i < len(myArray2); i++ {
		fmt.Println(myArray2[i])
	}

	// Iteración con range
	fmt.Println("Iteración con range")
	for id, value := range myArray {
		fmt.Println("Índice: ", id, "Valor: ", value)
	}

	// Copia manual
	var copyArray [5]string
	for i := range myArray {
		copyArray[i] = myArray[i]
	}
	fmt.Println("Copia Manual :", copyArray)

	// Copia usando slices
	copyArray2 := make([]int, len(myArray2))
	copy(copyArray2, myArray2[:])
	fmt.Println("Copia usando slices: ", copyArray2)

	// Subarrays(slices)
	mySlice := myArray2[2:5]
	fmt.Println("SubArrays(Slices): ", mySlice)

	// comparacion
	fmt.Println("Comparación")
	if copyArray == myArray {
		fmt.Println("copyArray es igual a myArray")
	}

	// suma de elementos
	total := 0
	for _, value := range myArray2 {
		total += value
	}
	fmt.Println("Suma de elementos: ", total)

	// Reversión
	arrayReverse := [5]int{1, 2, 3, 4, 5}
	for i, j := 0, len(arrayReverse)-1; i < j; i, j = i+1, j-1 {
		arrayReverse[i], arrayReverse[j] = arrayReverse[j], arrayReverse[i]
	}
	fmt.Println("Reversión: ", arrayReverse)

	// Slices(SubArrays): A diferencia de los arrays, los slices son flexibles en tamaño, lo que les permite crecer y decrecer según las necesidades.
	// Es importante saber que un slice no contiene datos, solo hace referencia a los datos en un array. Por lo que aunque estos copian el índice del array,
	// si se modifica el slice, el array de origen también cambiará.
	// si un array tiene 5 indices y se quiere agregar un 6to índice, el slice, creará otro array por debajo aunque se refiera al mismo desde el inicio.

	// inicialización
	var slice []int
	slice2 := []int{1, 2, 3} // inicialización corta con 3 elementos
	slice3 := make([]int, 5) // inicialización usando make con una longitud de 5
	fmt.Println("Slice iniciado: ", slice)
	fmt.Println("Slice con inicialización corta: ", slice2)
	fmt.Println("Slice con capacidad: ", cap(slice3), " y ", "longitud: ", len(slice3))

	// Índexación
	sliceNumber := []int{10, 20, 30, 40}
	fmt.Println("Indexación: ", sliceNumber[3], sliceNumber[1])

	// Inserción de elementos
	slice2 = append(slice2, 25)
	fmt.Println("Inserción: :", slice2)

	// Copiar un slice
	newSlice := make([]int, len(sliceNumber))
	copy(newSlice, sliceNumber)
	fmt.Println("Copiar un slice: ", newSlice)

	// Slice bidimensional
	towDimension := make([][]int, 3)
	for i := 0; i < 3; i++ {
		towDimension[i] = make([]int, 3)
		for j := 0; j < 3; j++ {
			towDimension[i][j] = i + j
		}

	}
	fmt.Println("Slice bidimensional: ", towDimension)

	// Mapas: En golang son un tipo de dato especial, que puede almacenar una colección de pares clave-valor, esto es similar a un
	// diccionario en python o un hashmap en java. En go, un mapa es un tipo de dato incorporado que se implementa
	// utilizando una tabla hash, lo que le da, caracteristicas de busqueda, adición, ctualización y eliminación de datos.
	// Al ser un tipo de referencia estos al ser creados, obtienen un puntero a los datos subyacentes.
	// son de crecimiento dinámico, tienen unicidad de clave(son únicas) y son colecciones desordenadas.

	// Declaración e Inicialización: La forma más común es usar la función make, aunque también se crean con sintaxis literal
	// al trabajar con mapas hay que tener en cuenta que el valor nulo de un mapa no inicializado es nil.
	// un mapa debe inicializarse para poder usarlo, esto se logra usando make.

	emptyMap := make(map[string]int) // cración con make

	fruitsMap := map[string]int{ // creación con sisntaxis literal
		"manzana": 2,
		"pera":    5,
		"banana":  4,
		"cereza":  2,
		"durazno": 5,
		"kiwi":    4,
	}

	var m = map[string]int{}
	if m == nil {
		m = make(map[string]int)
		fmt.Println("Mapa Inicializado.")
	} else {
		fmt.Println("Mapa ya inicializado y listo para usarse.")
	}

	// Inserción:
	emptyMap["miguel"] = 31
	fmt.Println(emptyMap)

	// Borrado:
	delete(emptyMap, "miguel")
	fmt.Println(emptyMap)

	// Actualización:
	fruitsMap["manzana"] = 12
	fmt.Println(fruitsMap["manzana"])

	// Ordenamiento: Por defecto, los mapas no permiten el ordenamiento porque estan hechos para acceder a sus valores por medio de claves.
	// pero hay manera de hcarlo:

	var keys []string          // Slice
	for k := range fruitsMap { // Extraer las claves del mapa
		keys = append(keys, k)
	}

	// Ordenamos las claves:
	sort.Strings(keys)

	// Recorremos las claves ordenadas y accedemos a los valores:
	for _, k := range keys {
		fmt.Printf("%s: %d:\n", k, fruitsMap[k])
	}

	// Seguridad y sync.map: AL utilizar un entorno multihilo, se debe prestar especial atención a los problemas de seguridad, en concurrencia.
	// En un escenario concurrente, el tipo mapa en golang puede llevar a condiciones de carrera si no se implementa una sincronización adecuada.
	// La biblioteca estándar de Go proporciona el tipo sync.Map, que es un mapa seguro diseñado para entornos concurrentes.
	// Este tipo ofrece métodos básicos como Load, Store, LoadOrStore, Delete y Range para operar en el mapa.

	// Declarando el  mapa
	var mySyncMap sync.Map

	// Inserción de datos en el mapa
	mySyncMap.Store("miguel", 26)
	mySyncMap.Store("alejandro", 33)

	// Leendo e imprimiendo datos
	if valor, ok := mySyncMap.Load("miguel"); ok {
		fmt.Printf("Clave: Miguel Valor:%d\n", valor)
	}

	// Iterando sobre eun sync.Map con range
	mySyncMap.Range(func(clave, valor interface{}) bool {
		fmt.Printf("Clave: %v, Valor: %v\n", clave, valor)
		return true // continuar la iteración
	})

	// Eliminando datos en el map
	mySyncMap.Delete("alejandro")
	fmt.Println(mySyncMap.Load("miguel"))    // Resultado: valor + un true
	fmt.Println(mySyncMap.Load("alejandro")) // Resultado: valor nil y false

	// Ordenamiento
	var animals sync.Map

	// Guardar algunos valores
	animals.Store("Mono", 5)
	animals.Store("Foca", 13)
	animals.Store("Águila", 3)
	animals.Store("Mandríl", 2)
	animals.Store("Burro", 1)

	var pairs PairList

	// Usa range sobre el mapa para obtener los pares
	animals.Range(func(key, value interface{}) bool {
		pairs = append(pairs, Pair{key: key.(string), value: value.(int)})
		return true
	})

	// Ordenar los pares por valor
	sort.Sort(pairs)

	// Imprime los pares ordenados
	for _, pair := range pairs {
		fmt.Printf("%s: %d\n", pair.key, pair.value)
	}

	// Actualización Valores:
	var myUpdateMap sync.Map
	myUpdateMap.Store("llave", "Valor Inicial")
	valor, _ := myUpdateMap.Load("llave")
	fmt.Printf("Clave: llave Valor: %s\n", valor)

	myUpdateMap.Store("llave", "Nuevo Valor")
	valor2, _ := myUpdateMap.Load("llave")
	fmt.Printf("Clave: llave Valor: %s\n", valor2)

	// Structs: En golang, son un tipo de dato compuesto muy utilizado para agrupar diferentes tipos de datos en una sola entidad, ya sean diferentes o identicos
	// en go los Structs son un aspecto fundamental para la programación orientada a objetos, con ligeras diferencias a los lenguajes tradicionales de poo.
	// la necesidad de strucs surge de los siguientes aspectos:
	// 	- Organizar variables con fuerte relevancia juntas para mejorar la mantenibilidad del código.
	//  - Proporcionar un medio para simular "clases", facilitando las características de encapsulación y agregación.
	//  - Al interactuar con estructuras de datos como JSON, registros de bases de datos, etc., los structs ofrecen una herramienta de mapeo conveniente.

	// Declaración:
	type person struct {
		name     string
		nickname string
		age      uint8
		mails    []string // Pueden obtener tipos comolejos como slices
	}

	// Instanciacion de una struct.
	var p person

	// Esto crea un puntero a la struct.
	p2 := new(person)
	fmt.Println(p2)

	// Inicializar con nombres de campo.
	p3 := person{
		name:     "Miguel",
		nickname: "Migue",
	}
	fmt.Println(p3)

	// inicializar sin nombre de campos:  es posible pero es obligatorio mantener el orden para que no se presenten errores.
	// Además no se pueden omitir campos, es decir que es obligatorio usarlos todo, más importante aún, esta manera es insostenible
	// en estructuras grandes.
	p4 := person{"miguel", "miguel", 31, []string{"miguelportillo2475@gmail.com"}}

	// Acceso e inserción de datos
	p.name = "Miguel"
	fmt.Println("Inserción: ", p)

	// Actualización
	p4.name = "Alejandro"
	fmt.Println("Actualización: ", p4)

	// Una estructura anónima; no declara explícitamente un nuevo tipo,
	// sino que utiliza directamente la definición de la estructura.
	// Esto es útil cuando necesitas crear una estructura una vez y
	// usarla de manera simple, evitando la creación de tipos innecesarios.

	pet := struct {
		name  string
		age   uint8
		owner string
	}{
		name:  "Winky",
		age:   6,
		owner: "Miguel",
	}

	fmt.Printf("Nombre: %s Edad; %d Propietario: %s\n", pet.name, pet.age, pet.owner)

	// El anidamieto de estructuras nos permite anidar una estructura como parte de otra, para crear estructuras más complejas.
	type address struct {
		originCity   string
		locationCity string
		work         bool
	}

	type person2 struct {
		name      string
		age       uint8
		direction address
	}

	p5 := person2{
		name: "miguel",
		age:  31,
		direction: address{
			originCity:   "Santa Bárbara de Zulia",
			locationCity: "Medellín",
			work:         true,
		},
	}
	fmt.Println("Nombre: ", p5.name, "\nEdad: ", p5.age, "\nCiudad de Origen: ", p5.direction.originCity, "\nCiudad Actual: ", p5.direction.locationCity, "\nTrabaja: ", p5.direction.work)

	// Las Strucs son muy extensas y versátiles, podría seguir con más ejemplos pero pienso que se pueden aclarar en otros ejercicios más adelante.

	// Llamada a la aplicación de agenda.
	Contacts()
}

var directoryOfContacts = make(map[string]int)
var options uint8
var contactName string
var contactNumber string

func Contacts() {
	for {
		fmt.Println("")
		fmt.Println("Bienvenido a mi lista de contactos")
		fmt.Println("1. Búscar un contacto.")
		fmt.Println("2. Crear un Contacto.")
		fmt.Println("3. Actualizar un contacto.")
		fmt.Println("4. Eliminar un contacto.")
		fmt.Println("5. Lista de contactos.")
		fmt.Println("6. Salir de la lista.")
		fmt.Println("Por favor selecciona una de las opciones:")
		fmt.Scan(&options)

		switch options {
		case 1: // Busqueda
			fmt.Println("Ingresa el nombre del contacto a buscar:")
			fmt.Scan(&contactName)

			if verifyIfUserExist(contactName) {
				fmt.Printf("Número de contacto: %v\n", directoryOfContacts[contactName])
			} else {
				fmt.Println("El contacto no existe.")
			}

		case 2: // Creación
			fmt.Println("Introduce un nombre: ")
			fmt.Scan(&contactName)
			fmt.Println("Introduce un número: ")
			fmt.Scan(&contactNumber)

			if verifyIfUserExist(contactName) {
				fmt.Println("Este contacto ya existe, si desea actualizarlo seleccione la opción 3.")
			} else {
				if validatePhoneNumber(contactNumber) {
					convertedNumber, _ := strconv.Atoi(contactNumber)
					directoryOfContacts[contactName] = convertedNumber
					fmt.Printf("Contacto Registrado: %s\n", contactName)
				} else {
					fmt.Println("Número no válido")
				}
			}
		case 3: // Actualización
			fmt.Println("Ingresa el nombre del contacto a actualizar:")
			fmt.Scan(&contactName)

			if verifyIfUserExist(contactName) {
				fmt.Println("Ingresa el nuevo número de contacto: ")
				fmt.Scan(&contactNumber)
				directoryOfContacts[contactName] = convertNumber(contactNumber)
			} else {
				fmt.Println("El contacto no existe.")
			}
		case 4: // Eliminación
			fmt.Println("Ingresa el nombre del contacto a eliminar:")
			fmt.Scan(&contactName)

			if verifyIfUserExist(contactName) {
				delete(directoryOfContacts, contactName)
			} else {
				fmt.Println("Contacto no encontrado")
			}

		case 5: // Listar todos los contactos
			var keys []string
			for k := range directoryOfContacts {
				keys = append(keys, k)
			}

			sort.Strings(keys)

			for _, k := range keys {
				fmt.Printf("%s: %d\n", k, directoryOfContacts[k])
			}
		case 6:
			fmt.Println("Saliendo... ¡Bye!")
			return
		default:
			fmt.Print("")
		}
	}
}

func validatePhoneNumber(s string) bool {

	if len(s) > 11 {
		return false
	}

	for _, r := range s {
		if !unicode.IsDigit(r) {
			{
				return false
			}
		}
	}
	return true
}

func verifyIfUserExist(name string) bool {
	var keys []string
	for k, _ := range directoryOfContacts {
		keys = append(keys, k)
	}

	for _, k := range keys {
		var result = strings.Contains(k, name)
		if result {
			return true
		}
	}
	return false
}

func convertNumber(value string) int {
	cn, _ := strconv.Atoi(value)
	return cn
}
