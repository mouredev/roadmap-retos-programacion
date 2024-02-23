package main

import "fmt"

// Definición de la estructura, similar a una "clase"
type Persona struct {
	Nombre    string
	Edad      int
	Domicilio string
}

// Un "constructor" para la estructura Persona
func NuevaPersona(nombre string, edad int, domicilio string) *Persona {
	return &Persona{Nombre: nombre, Edad: edad, Domicilio: domicilio}
}

// Método para imprimir los atributos de la estructura
func (p *Persona) Imprimir() {
	fmt.Printf("Nombre: %s, Edad: %d, Domicilio: %s\n", p.Nombre, p.Edad, p.Domicilio)
}

// Método para modificar los atributos
func (p *Persona) EstablecerNombre(nombre string) {
	p.Nombre = nombre
}

func (p *Persona) EstablecerEdad(edad int) {
	p.Edad = edad
}

func (p *Persona) EstablecerDomicilio(domicilio string) {
	p.Domicilio = domicilio
}

func main() {
	// Crear una nueva "instancia" de Persona
	persona := NuevaPersona("Alice", 30, "Calle Falsa 123")

	// Imprimir los atributos iniciales de la persona
	persona.Imprimir()

	// Modificar los atributos de la persona
	persona.EstablecerNombre("Bob")
	persona.EstablecerEdad(32)
	persona.EstablecerDomicilio("Avenida Siempre Viva 742")

	// Imprimir los atributos modificados
	persona.Imprimir()
}
