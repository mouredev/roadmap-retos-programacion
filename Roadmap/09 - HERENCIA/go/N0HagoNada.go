package main

import "fmt"

/*
En Go, no existe la herencia en la forma tradicional
En su lugar, Go utiliza un sistema de composición e interfaces para lograr una funcionalidad similar a la herencia
En lugar de "heredar" comportamientos y propiedades de una clase base, una "struct" en Go puede incluir (o "componerse de") otras structs. Esto se hace incrustando una struct dentro de otra
A través del uso de interfaces, Go permite un tipo de polimorfismo donde diferentes tipos pueden implementar la misma interfaz pero proporcionar implementaciones distintas para los métodos de la interfaz. Esto no  es sobrescritura en la froma tradicional.
*/

type Animal interface {
	EmitirSonido()
}

/*
La interfaz Animal actua como una clase base abstracta con un contrato EmitirSonido() que las 'subclases' deben implementar.
*/
type Perro struct {
	Nombre string
	Sonido string
}

type Gato struct {
	Nombre string
	Sonido string
}

func (p *Perro) EmitirSonido() {
	fmt.Println("El perro dice: ", p.Sonido)
}
func (g *Gato) EmitirSonido() {
	fmt.Println("El gato dice: ", g.Sonido)
}

/*
La función invocarSonido, que acepta un argumento de tipo Animal, demuestra polimorfismo. Puedes pasar cualquier objeto que implemente la interfaz Animal (como un Perro o un Gato)
*/
func invocarSonido(a Animal) {
	a.EmitirSonido()
}

/********************RETO********************/
// Empleado es la estructura base para todos los tipos de empleados.
type Empleado struct {
	Identificador int
	Nombre        string
}

// Gerente es un tipo de Empleado con empleados a su cargo.
type Gerente struct {
	Empleado
	EmpleadosACargo []Empleado
}

// GerenteDeProyectos es similar a Gerente pero específico de proyectos.
type GerenteDeProyectos struct {
	Empleado
	EmpleadosACargo []Empleado
	ProyectoActual  string
}

// Programador es un empleado sin empleados a su cargo pero con tecnologías específicas.
type Programador struct {
	Empleado
	Tecnologias []string
}

func main() {
	p := &Perro{Nombre: "temur", Sonido: "wof wof wof"}
	g := &Gato{Nombre: "michi", Sonido: "miau miau"}
	invocarSonido(p)
	invocarSonido(g)
	fmt.Println("******************* RETO *******************")
	// Creación de un Gerente
	gerente := Gerente{
		Empleado: Empleado{
			Identificador: 1,
			Nombre:        "Juan Pérez",
		},
		EmpleadosACargo: []Empleado{}, // Inicialmente sin empleados a su cargo
	}

	// Creación de un Gerente de Proyectos
	gerenteDeProyectos := GerenteDeProyectos{
		Empleado: Empleado{
			Identificador: 2,
			Nombre:        "Ana Gómez",
		},
		ProyectoActual:  "Desarrollo de Software",
		EmpleadosACargo: []Empleado{}, // Inicialmente sin empleados a su cargo
	}

	// Creación de un Programador
	programador := Programador{
		Empleado: Empleado{
			Identificador: 3,
			Nombre:        "Carlos López",
		},
		Tecnologias: []string{"Go", "Python", "JavaScript"},
	}

	fmt.Println(gerente)
	fmt.Println(gerenteDeProyectos)
	fmt.Println(programador)
}
