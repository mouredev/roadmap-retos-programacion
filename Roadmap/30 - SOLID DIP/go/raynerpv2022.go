/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Inversión de Dependencias (Dependency Inversion
 * Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un sistema de notificaciones.
 * Requisitos:
 * 1. El sistema puede enviar Email, PUSH y SMS (implementaciones específicas).
 * 2. El sistema de notificaciones no puede depender de las implementaciones específicas.
 * Instrucciones:
 * 1. Crea la interfaz o clase abstracta.
 * 2. Desarrolla las implementaciones específicas.
 * 3. Crea el sistema de notificaciones usando el DIP.
 * 4. Desarrolla un código que compruebe que se cumple el principio.
 */

package main

import "fmt"

// DIP incorrecto, Suma depende de Calcular, si queremos implementar otra operacion debemos modificar  Calcular
type Suma struct{}

func (s Suma) Execute(n1 int, n2 int) int {
	return n1 + n2
}

type calculator struct{}

func (c calculator) Calcular(op string, n1 int, n2 int) {
	if op == "suma" {
		s := Suma{}
		fmt.Println(s.Execute(n1, n2))
	} else {
		fmt.Println("Operacion aun no implementada")
	}
}

//  DIP Correcto

type VirtualOperation interface {
	Execute(x, y int) int
}

type SUMA struct{}
type RESTA struct{}

func (s SUMA) Execute(x, y int) int {
	return x + y
}

func (r RESTA) Execute(x, y int) int {
	return x - y
}

type Calculadora struct{}

func (c Calculadora) CALCULAR(op VirtualOperation, x, y int) {
	fmt.Println(op.Execute(x, y))
}

// EXTRA
type Virtualnotification interface {
	Print(message string)
}

type ScreenNotification struct{}

type LogNotification struct{}

type MOngoDbNotification struct{}

func (sn ScreenNotification) Print(message string) {
	fmt.Println("Enviando mensaje por pantalla")
	fmt.Println(message)
}

func (lg LogNotification) Print(message string) {
	fmt.Println("Enviando mensaje por Archivo Log")
	fmt.Println(message)
}

func (db MOngoDbNotification) Print(message string) {
	fmt.Println("Enviando mensaje por Base de DAto")
	fmt.Println(message)
}

type VirtualNotification interface {
	SendNotification(buzon string) string
}
type Email struct{}
type Push struct{}
type Sms struct{}

func (e Email) SendNotification(buzon string) string {
	return fmt.Sprintf("Notificacion %s enviada por Email \n", buzon)

}

func (p Push) SendNotification(buzon string) string {
	return fmt.Sprintf("Notificacion %s enviada por Push \n", buzon)
}
func (s Sms) SendNotification(buzon string) string {
	return fmt.Sprintf("Notificacion %s enviada por Sms \n", buzon)
}

type MDeamon struct{}

func (md MDeamon) Notificador(notificador VirtualNotification, typeNotificator Virtualnotification, message string) {
	typeNotificator.Print(notificador.SendNotification(message))

}

func main() {
	fmt.Println("Reto 30, SOLID, inversion de dependencias")

	c := calculator{}
	c.Calcular("suma", 12, 34)
	c.Calcular("sdssd", 12, 34)

	C := Calculadora{}
	r := RESTA{}
	s := SUMA{}
	C.CALCULAR(r, 23, 10)
	C.CALCULAR(s, 23, 10)

	// Extra
	n := MDeamon{}
	n.Notificador(Email{}, LogNotification{}, "Cita mana en el SEPE")
	n.Notificador(Sms{}, MOngoDbNotification{}, " Botar Basura en el Tonel correcto")
	n.Notificador(Push{}, ScreenNotification{}, "TUV presione enter para confirmar")

}
