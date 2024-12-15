package main

import (
	"fmt"
)

/*
En 'Golang' no existe la herencia como en otros lenguajes, pero existe la composición.
Esto no es un problema de diseño, el lenguaje está diseñado de esta manera
en parte para evitar las jerarquías de tipo y evitar realizar un sobrediseño temprano en la solución.
así evitamos hacerla más compleja(pero no más funcional).

Composición: Facil de testear, DI/DIP(Inyección de dependencias/Principio de inversión  de dependencias).
Golang nos ofrece caracteristicas que van más allá:
- Métodos que pueden usarse en diferentes tipos declarados.(maps, structs, slices, y otros tipos)
- Interfaces implicitas: No necesitamos usar la palabra reservada 'Implements', ya que golang verifica si nuesto tipo
tiene los métodos que requiere la interface y esto es muy util ya que varios tipos puenden satisfacer a una interface
y no hace falta especificar que el tipo 'X' implementa a las interfaces '1', '2', '3', etc...
- Incrustación de cammpos: Permite integrar tipos en otros tipos y esto no es analogo a las clases, pero no es idéntico.

Golang no posee las funciones setter y getter aunque estas se pueden diseñar de manera simple com métodos.

Tipos: En golang existen muchos tipos; como los predeclarados: string, float, int, etc...
también los tipos compuestos como los arreglos, maps, slice, estructs, etc...
Pero adicionalmente existen tipos compuestos, estos tienen ciertas condiciones como ser referenciados en el mismo
paquete en que los declaramos.
por eso no podemos añadir funcionalidades a los tipos predeclarados, pero lo que si podemos es construir un nuevo tipo a partir de uno
predeclarado y añadirle nuevas funcionalidades

Golang tampoco posee sobreescritura de métodos, en cambio tiene ocultación de métodos, aunque hay que tener cuidado cone esto
porque pueden generarse conflictos.

por ejemplo cuando tienes un capo de nombre en dos estructuras "Humano y Empleado" y embebemos empleado en humano para obtener sus métodos
y atributos, puede haber conflicto al llamar el nombre, esto se soluciona llamando el nombre espesificando si lo queremos de la clase humano o
la clase empleado.

fmt.Println(e.Human.age) o fmt.Println(e.Employee.age) dependiendo desde de clase se requiera.
*/

// newBool nuevo tipo a partir de un tipo predeclarado
type newBool bool

// String es el método de un nuevo tipo a partir de uno predeclarado
func (b newBool) String() string {
	if b {
		return "VERDADERO"
	}
	return "FALSO"
}

// Composición de estructuras.
// character es una clase padre
type character struct {
	name  string
	race  string
	atack bool
}

// animal es la clase padre
type animal struct {
	animalType string
	sound      string
}

// sound es método de la clase padre animal
func (a animal) makeSound() {
	fmt.Println(a.animalType, " dice: ", a.sound)
}

// instancias con asignación directa de la clase padre "animal"
var cat = animal{animalType: "Gato", sound: "Miau"}
var dog = animal{animalType: "Perro", sound: "Guau"}

// NewCharacter es el constructor de caracteres
func NewCharacter(name, animalType string, atack bool) character {
	return character{name, animalType, atack}
}

// Extra

// employee es la clase padre del ejercio extra
type employee struct {
	id       int
	name     string
	position string
}

// manager es una subclase de empleado
type manager struct {
	employee
	employees []employee
}

// projectManager es una subclase de empleado
type projectManager struct {
	manager
	projects []string
}

// programmer es la subclase de empleado
type programmer struct {
	employee
	languages []string
}

func main() {
	monster := NewCharacter("Golg", "Dragon", true)
	fmt.Println("Nombre: ", monster.name)
	fmt.Println("Raza: ", monster.race)
	fmt.Println("¿Ataca?: ", monster.atack)

	// Método impresor de sonido de los nimales
	cat.makeSound()
	dog.makeSound()

	// Extra
	employee1 := employee{id: 1, name: "Miguel", position: "Programmer"}
	employee2 := employee{id: 2, name: "Ricardo", position: "Manager"}
	employee3 := employee{id: 3, name: "Vicente", position: "Project Manager"}
	manager1 := manager{employee: employee1, employees: []employee{employee2, employee3}}
	projectManager1 := projectManager{manager: manager1, projects: []string{"Project 1", "Project 2"}}
	programmer1 := programmer{employee: employee1, languages: []string{"Go", "Python", "Java"}}
	programmer2 := programmer{employee: employee3, languages: []string{"Java", "C#"}}

	fmt.Println("Employee 1: ", employee1)
	fmt.Println("Employee 2: ", employee2)
	fmt.Println("Employee 3: ", employee3)
	fmt.Println("Manager 1: ", manager1)
	fmt.Println("Project Manager 1: ", projectManager1)
	fmt.Println("Programmer 1: ", programmer1)
	fmt.Println("Programmer 2: ", programmer2)

	// nuevo tipo a partir de uno predeclarado y con nueva funcionalidad(Simple)
	var b newBool = true
	fmt.Println(b.String())
	b = false
	fmt.Println(b.String())

}
