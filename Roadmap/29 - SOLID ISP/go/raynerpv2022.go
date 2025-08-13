package main

import "fmt"

/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Segregación de Interfaces (Interface Segregation Principle, ISP)"
 * y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta.
 *

 */

// Imagina que estás diseñando un sistema para distintos tipos de trabajadores en una empresa:

//     Trabajador oficina

//     Trabajador remoto

//     Robot de fábrica

// Tu interfaz base (o clase abstracta) define:

//     trabajar()

//     asistir_a_reunion()

//     comer_en_cafeteria()

// ❌ Problema:

//     El Robot también hereda esta interfaz.

//     Pero... ¿tiene sentido que un robot tenga que:

//         asistir a reuniones

//         o comer en la cafetería?

// ¡No!, pero el diseño lo obliga a implementar esos métodos.

// Incorrect
type Task interface {
	Working()
	Meeting()
	Eating()
}

type OfficeWorker struct{}

func (OW *OfficeWorker) Working() {
	fmt.Println("Trabajando...soy un trabajador de oficina")
}

func (OW *OfficeWorker) Meeting() {
	fmt.Println("Asistiendo a reunion...soy un trabajador de oficina")
}

func (OW *OfficeWorker) Eating() {
	fmt.Println("Comiendo en cafeteria...soy un trabajador de oficina")
}

type RemoteWorker struct{}

func (RW *RemoteWorker) Working() {
	fmt.Println("Trabajando...soy un trabajador remoto")
}

func (OW *RemoteWorker) Meeting() {
	fmt.Println("Asistiendo a reunion...soy un trabajador remoto")
}

func (OW *RemoteWorker) Eating() {
	fmt.Println("Comiendo en cafeteria...soy un trabajador remoto")
}

type RobotFabric struct{}

func (RB *RobotFabric) Working() {
	fmt.Println("Trabajando...soy un robot")
}

func (RB *RobotFabric) Meeting() {
	fmt.Println("Asistiendo a reunion... pero no puedo, me obligas a hacerlo, soy un robot")
}

func (OW *RobotFabric) Eating() {
	fmt.Println("Comiendo en cafeteria...pero no puedo, me obligas a hacerlo, soy un robot")
}

func Orquester(w Task) {
	w.Working()
	w.Meeting()
	w.Eating()
}

// correcto

type workingVirtual interface {
	working()
}
type eatingVirtual interface {
	eating()
}
type meetingVirtual interface {
	meeting()
}

type WorkerOficce struct{}

func (wo *WorkerOficce) working() {
	fmt.Println("Trabajando...soy un trabajador de oficina")
}

func (wo *WorkerOficce) eating() {
	fmt.Println("Comiendo...soy un trabajador de oficina")
}

func (wo *WorkerOficce) meeting() {
	fmt.Println("En Reunion...soy un trabajador de oficina")
}

type WorkerRemote struct{}

func (wo *WorkerRemote) working() {
	fmt.Println("Trabajando...soy un trabajador   Remoto")
}

func (wo *WorkerRemote) eating() {
	fmt.Println("Comiendo...soy un trabajador   Remoto")
}

func (wo *WorkerRemote) meeting() {
	fmt.Println("En Reunion...soy un trabajador   Remoto")
}

type WorkerRobot struct{}

func (wo *WorkerRobot) working() {
	fmt.Println("Trabajando...soy un Robot")
}

func AllWorking(w workingVirtual) {
	w.working()
}

func AllMeeting(w meetingVirtual) {
	w.meeting()
}

func AllEating(w eatingVirtual) {
	w.eating()
}

func Orquester1(o interface{}) {
	w, ok := o.(workingVirtual)
	if ok {
		AllWorking(w)
	}

	if w, ok := o.(meetingVirtual); ok {
		AllMeeting(w)
	}

	if w, ok := o.(eatingVirtual); ok {
		AllEating(w)
	}
}

// * DIFICULTAD EXTRA (opcional):
//  * Crea un gestor de impresoras.
//  * Requisitos:
//  * 1. Algunas impresoras sólo imprimen en blanco y negro.
//  * 2. Otras sólo a color.
//  * 3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
//  * Instrucciones:
//  * 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
//  * 2. Aplica el ISP a la implementación.
//  * 3. Desarrolla un código que compruebe que se cumple el principio.

type impresionBN interface {
	PrintBn()
}
type impresionColor interface {
	PrintColor()
}
type scanner interface {
	Scaner()
}
type fax interface {
	Fax()
}

type epsonBN struct{}

func (e *epsonBN) PrintBn() {
	fmt.Println("Soy Epson que imprime solo en Blanco y Negro")
}

type hPcolor struct{}

func (e *hPcolor) PrintColor() {
	fmt.Println("Soy HP que imprime En color")
}

type multiFunction struct{}

func (m *multiFunction) PrintBn() {
	fmt.Println("Soy Multi funcion que ahora imprime en Blanco y Negro ")
}

func (m *multiFunction) PrintColor() {
	fmt.Println("Soy Multi funcion que ahora imprime a Color ")
}

func (m *multiFunction) Scaner() {
	fmt.Println("Soy Multi funcion que ahora Scanea  ")
}

func (m *multiFunction) Fax() {
	fmt.Println("Soy Multi funcion que ahora envia Fax  ")
}

func ExecutePrintBN(bn impresionBN) {
	bn.PrintBn()
}

func ExecutePrintColor(pc impresionColor) {
	pc.PrintColor()
}

func ExecuteScanner(s scanner) {
	s.Scaner()
}

func ExecuteFaxer(f fax) {
	f.Fax()
}

// func ExtraOrquester(o interface{}, action int) {

// 	if bn, ok := o.(impresionBN); ok {

// 		PrintBN(bn)
// 	}

// 	if cl, ok := o.(impresionColor); ok {
// 		PrintColor(cl)
// 	}

// 	if action == 1 {
// 		if pnt, ok := o.(impresionBN); ok {
// 			PrintBN(pnt)
// 		}
// 	}

// 	if action == 2 {
// 		if c, ok := o.(impresionColor); ok {
// 			PrintColor(c)
// 		}
// 	}

// 	if action == 3 {
// 		if scan, ok := o.(scanner); ok {
// 			Scanner(scan)
// 		}
// 	}

// 	if action == 4 {
// 		if fax, ok := o.(fax); ok {
// 			Faxer(fax)
// 		}
// 	}

func main() {
	fmt.Println("ISP Solid")

	fmt.Println("Mal Disenno")

	ow := &OfficeWorker{}
	rw := &RemoteWorker{}
	rf := &RobotFabric{}
	Orquester(ow)
	Orquester(rw)
	Orquester(rf)

	fmt.Println("Buen Disenno")

	wo := &WorkerOficce{}
	wr := &WorkerRemote{}
	fr := &WorkerRobot{}
	Orquester1(wo)
	Orquester1(wr)
	Orquester1(fr)

	fmt.Println("Extra")

	epson := &epsonBN{}
	hp := &hPcolor{}
	mf := &multiFunction{}

	ExecutePrintBN(epson)
	ExecuteScanner(mf)
	ExecuteFaxer(mf)
	ExecutePrintBN(mf)
	ExecutePrintColor(hp)
	ExecutePrintColor(mf)

}
