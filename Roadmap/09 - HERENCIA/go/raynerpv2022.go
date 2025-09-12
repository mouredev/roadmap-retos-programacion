package main

import "fmt"

// /*
//  * EJERCICIO:
//  * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
//  * implemente una superclase Animal y un par de subclases Perro y Gato,
//  * junto con una función que sirva para imprimir el sonido que emite cada Animal.
//  *

type Salvaje interface {
	Sonido()
}
type Animal struct {
	nombre string
}

type Gusano struct {
	Animal
	sonido string
}

type Hormiga struct {
	Animal
	sonido string
}

func (g Gusano) Sonido() {
	fmt.Printf("Me llamo  %s y hago %s\n", g.nombre, g.sonido)
}

func (h Hormiga) Sonido() {
	fmt.Printf("Me llamo  %s y hago %s\n", h.nombre, h.sonido)
}

func AnimalSalvaje(AS Salvaje) {
	AS.Sonido()

}

// ************************************************************
//  * DIFICULTAD EXTRA (opcional):
//  * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
//  * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
//  * Cada empleado tiene un identificador y un nombre.
//  * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
//  * actividad, y almacenan los empleados a su cargo.
//  */

type Empleado struct {
	id              int
	nombre          string
	empleadosACargo []Empleado
}

type Gerente struct {
	Empleado
	proyectos []string
}

type GerenteP struct {
	Empleado
	proyecto string
}

type Programador struct {
	Empleado
	lenguajes []string
}

func (p *Programador) MostrarLenguajes() {
	fmt.Printf("Soy el programador %v y puedo programar en %v \n", p.nombre, p.lenguajes)
}

func (p *Programador) Addlengajes(lenguaje string) {

	p.lenguajes = append(p.lenguajes, lenguaje)
	fmt.Println("Lenguaje guardado")
}

func (p *Programador) MostrarEmpleados() {
	fmt.Printf("Soy el programador %v y no puedo tener empleados a cargo \n", p.nombre)
}

func (g *GerenteP) MostrarEmpleados() {
	fmt.Printf("Soy el Gerente de Proyecto %v \n", g.nombre)
	fmt.Printf("Mis empleados a cargo son  %v \n", g.empleadosACargo)

}

func (g *GerenteP) AddEmpleados(empleado Empleado) {
	g.empleadosACargo = append(g.empleadosACargo, empleado)
	fmt.Println("Empleado guardado")

}

func (g *GerenteP) Mostrarproyecto() {
	fmt.Printf("Soy el Gerente de Proyecto %v \n", g.nombre)
	fmt.Printf("Miproyecto es   %v \n", g.proyecto)
}

func (g *GerenteP) AddProyecto(proyecto string) {
	g.proyecto = proyecto
	fmt.Println("Proyecto guardado")

}

func (g *Gerente) Mostrarproyectos() {
	fmt.Printf("Soy el Gerente   %v \n", g.nombre)
	fmt.Printf("Mis proyecto son   %v \n", g.proyectos)
}

func (g *Gerente) Addproyectos(proyecto string) {
	g.proyectos = append(g.proyectos, proyecto)
	fmt.Println("Proyecto guardado")
}
func (g *Gerente) MostrarEmpleados() {
	fmt.Printf("Soy el Gerente   %v \n", g.nombre)
	fmt.Printf("Mis empleados son   %v \n", g.empleadosACargo)
}

func (g *Gerente) AddEmpleados(empleado Empleado) {
	g.empleadosACargo = append(g.empleadosACargo, empleado)
	fmt.Println("Proyecto guardado")
}
func main() {
	gusanito := Gusano{Animal{"gusi"}, "ffffff"}
	hormiguita := Hormiga{Animal{"hormi"}, "gggggg"}
	AnimalSalvaje(gusanito)
	AnimalSalvaje(hormiguita)

	fmt.Println("************* Extra ************")
	p1 := Programador{
		Empleado{
			9,
			"Pepito",
			nil,
		},
		nil}

	p1.Addlengajes("Java")
	p1.Addlengajes("Python")
	p2 := Programador{
		Empleado{
			8,
			"Juannito",
			nil,
		},
		nil}
	p2.Addlengajes("Golang")
	p2.Addlengajes("C++")

	gp1 := GerenteP{
		Empleado{
			2,
			"kuko",
			nil,
		},
		""}
	gp2 := GerenteP{
		Empleado{
			3,
			"lalo",
			nil,
		},
		""}
	gp1.AddProyecto("Web")
	gp2.AddProyecto("MOngodb")
	gp1.AddEmpleados(p1.Empleado)
	gp2.AddEmpleados(p2.Empleado)
	g := Gerente{
		Empleado{
			1,
			"Jefesito",
			nil,
		},
		nil}
	g.Addproyectos(gp1.proyecto)
	g.Addproyectos(gp2.proyecto)
	g.AddEmpleados(gp1.Empleado)
	g.AddEmpleados(gp2.Empleado)

	p1.MostrarLenguajes()
	p1.MostrarEmpleados()

	p2.MostrarLenguajes()
	p2.MostrarEmpleados()

	gp1.MostrarEmpleados()
	gp1.Mostrarproyecto()

	gp2.MostrarEmpleados()
	gp2.Mostrarproyecto()

	g.MostrarEmpleados()
	g.Mostrarproyectos()

}
