package main

/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)"
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
 * cumplir el LSP.
 * Instrucciones:
 * 1. Crea la clase Vehículo.
 * 2. Añade tres subclases de Vehículo.
 * 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
 * 4. Desarrolla un código que compruebe que se cumple el LSP.
 */

import "fmt"

// incorrecto
type vehiculo interface {
	avanzar()
	retroceder()
}

type autobus struct {
}

func (m autobus) avanzar() {
	fmt.Println("avanzar")
}

func (m autobus) retroceder() {
	fmt.Println("retrocediendo")
}

type tranvia struct {
}

func (t tranvia) avanzar() {
	fmt.Println("avanzar")
}

func (m tranvia) retroceder() {
	fmt.Println("retrocediendo")
}

func creartransporte(tt vehiculo) {

	tt.avanzar()
	tt.retroceder()

}

// correcto

type moverAdelante interface {
	adelante()
}

type moverAtras interface {
	atras()
}

type tren struct{}

func (t tren) adelante() {
	fmt.Println("moviendo adelante")
}
func (t tren) atras() {
	fmt.Println("moviendo atras")
}

type tranvia1 struct{}

func (t tranvia1) adelante() {
	fmt.Println("moviendo adelante")
}

func avanceTransporte(t1 moverAdelante) {
	t1.adelante()

}

func retrocesoTransporte(t1 moverAtras) {
	t1.atras()
}

// ***************************** ejercicio

type Freno interface {
	frenar(velo int)
}

type Acelerador interface {
	acelerar(velo int)
}

type bicicleta struct {
	speed int
}
type patinete struct {
	speed int
}
type triciclo struct {
	speed int
}

func (b *bicicleta) frenar(velo int) {
	b.speed -= velo
	fmt.Printf(" Frenando la bici... velocidad :%v \n", b.speed)
}

func (b *bicicleta) acelerar(velo int) {
	b.speed += velo
	fmt.Printf(" Acelerando la bici... velocidad :%v \n", b.speed)
}

func (p *patinete) acelerar(velo int) {
	p.speed += velo
	fmt.Printf(" Acelerando el Patinete... velocidad :%v \n", p.speed)
}

func (p *patinete) frenar(velo int) {
	p.speed -= velo
	fmt.Printf(" Frenado el Patinete... velocidad :%v \n", p.speed)
}

func (t *triciclo) acelerar(velo int) {
	t.speed += velo
	fmt.Printf(" Acelerando el triciclo... velocidad :%v \n", t.speed)
}

func test_acelerar(v Acelerador, vel int) {
	v.acelerar(vel)

}

func test_frenar(v Freno, vel int) {
	v.frenar(vel)

}

func main() {
	fmt.Println("Reto 28 LSP")
	autobus := autobus{}
	tranvia := tranvia{}
	creartransporte((autobus))
	creartransporte((tranvia))

	tren := tren{}
	tranvia1 := tranvia1{}

	avanceTransporte(tren)
	retrocesoTransporte(tren)
	avanceTransporte(tranvia1)

	bici := &bicicleta{}
	pati := &patinete{}
	tri := &triciclo{}

	test_acelerar(bici, 10)
	test_frenar(bici, 3)

	test_acelerar(pati, 4)
	test_frenar(pati, 1)

	test_acelerar(tri, 100)

}
