package main

import "fmt"

// Como vimos en el reto anterior, en Go el concepto de clases es algo distinto a otros lenguajes.

type Animal interface {
	sonido()
}

type Perro struct {
	nombre string
	sound  string
}

type Gato struct {
	nombre string
	sound  string
}

func (perro *Perro) sonido() {
	fmt.Println("El perro de nombre " + perro.nombre + " emite el sonido " + perro.sound)
}

func (gato *Gato) sonido() {
	fmt.Println("El gato de nombre " + gato.nombre + " emite el sonido " + gato.sound)
}

type Empleado struct {
	Identificador int
	Nombre        string
}

type Gerente struct {
	Empleado  // Incorpora todos los campos de Empleado en Gerente
	Empleados []string
}

type GerenteP struct {
	Empleado      // Incorpora todos los campos de Empleado en GerenteP
	Programadores []string
}

type Programador struct {
	Empleado  // Incorpora todos los campos de Empleado en Programador
	Lenguajes []string
}

func (gerente *Gerente) gestiona() {
	fmt.Println("El gerente de proyectos " + gerente.Nombre + " gestiona a los empleados " + fmt.Sprint(gerente.Empleados))
}

func (gerenteP *GerenteP) gestiona() {
	fmt.Println("El gerente " + gerenteP.Nombre + " gestiona a los programadores " + fmt.Sprint(gerenteP.Programadores))
}

func (programador *Programador) programa() {
	fmt.Println("El programador " + programador.Nombre + " programa en los lenguajes " + fmt.Sprint(programador.Lenguajes))
}

func main() {
	perro := Perro{"Milu", "Guau, guau"}
	gato := Gato{"Garfield", "Miauuuuuuu"}

	perro.sonido()
	gato.sonido()

	// Extra

	gerente := Gerente{
		Empleado: Empleado{
			Identificador: 1,
			Nombre:        "Migue",
		},
		Empleados: []string{"Fran", "Maria", "Ana"},
	}

	gerenteP := GerenteP{
		Empleado: Empleado{
			Identificador: 2,
			Nombre:        "Fran",
		},
		Programadores: []string{"Pablo", "Rafa", "Carlos"},
	}

	programador := Programador{
		Empleado: Empleado{
			Identificador: 3,
			Nombre:        "Carlos",
		},
		Lenguajes: []string{"Go", "Python", "Java"},
	}

	gerente.gestiona()
	gerenteP.gestiona()
	programador.programa()

}
