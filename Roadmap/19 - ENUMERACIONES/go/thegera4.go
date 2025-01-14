package main

import "fmt"

// No existe la estructura de enumeraciones en Go, pero se puede simular con constantes
// Primero creamos un tipo de dato para representar, en este caso, los días de la semana (este paso es opcional)
type DiaSemana string

// Luego creamos las constantes con su valor, que representan los días de la semana
const (
	Lunes DiaSemana = "Lunes"
	Martes DiaSemana = "Martes"
	Miercoles DiaSemana = "Miercoles"
	Jueves DiaSemana = "Jueves"
	Viernes DiaSemana = "Viernes"
	Sabado DiaSemana = "Sabado"
	Domingo DiaSemana = "Domingo"
)

// Creamos una función que recibe un entero y devuelve el día de la semana correspondiente
func DiaSemanaFromInt(dia int) DiaSemana {
	switch dia {
	case 1:
		return Lunes
	case 2:
		return Martes
	case 3:
		return Miercoles
	case 4:
		return Jueves
	case 5:
		return Viernes
	case 6:
		return Sabado
	case 7:
		return Domingo
	default:
		return "No existe"
	}
}

func main() {
	fmt.Println(DiaSemanaFromInt(1))
	fmt.Println(DiaSemanaFromInt(2))
	fmt.Println(DiaSemanaFromInt(3))
	fmt.Println(DiaSemanaFromInt(4))
	fmt.Println(DiaSemanaFromInt(5))
	fmt.Println(DiaSemanaFromInt(6))
	fmt.Println(DiaSemanaFromInt(7))
	fmt.Println(DiaSemanaFromInt(8))

	//Extra:

	p1 := Pedido{id: 1, status: PENDIENTE}
	p2 := Pedido{id: 2, status: ENVIADO}
	p3 := Pedido{id: 3, status: ENTREGADO}
	p4 := Pedido{id: 4, status: CANCELADO}

	fmt.Println("Pedido 1:")
	fmt.Println(p1)
	p1.Enviar()
	fmt.Println(p1)
	p1.Cancelar()
	fmt.Println(p1)

	fmt.Println("Pedido 2:")
	fmt.Println(p2)
	p2.Cancelar()
	fmt.Println(p2)
	p2.Entregar()
	fmt.Println(p2)

	fmt.Println("Pedido 3:")
	fmt.Println(p3)
	p3.Enviar()
	p3.Cancelar()

	fmt.Println("Pedido 4:")
	fmt.Println(p4)
	p4.Entregar()

}

//Extra:

type EstadoPedido int

const (
	PENDIENTE EstadoPedido = iota
	ENVIADO
	ENTREGADO
	CANCELADO
)

type Pedido struct {
	id     int
	status EstadoPedido
}

func (p *Pedido) Enviar() {
	if(p.status == ENVIADO){
		fmt.Println("El pedido ya ha sido enviado")
	} else if (p.status == ENTREGADO) {
		fmt.Println("El pedido ya ha sido entregado")
	} else if (p.status == PENDIENTE) {
		p.status = ENVIADO
	} else {
		fmt.Println("No se puede enviar un pedido que no está pendiente")
	}
}

func (p *Pedido) Cancelar() {
	if p.status == CANCELADO {
		fmt.Println("El pedido ya ha sido cancelado")
	} else if p.status == ENTREGADO {
		fmt.Println("El pedido ya ha sido entregado")
	} else if p.status == PENDIENTE {
		p.status = CANCELADO
	} else {
		fmt.Println("No se puede cancelar un pedido que no está pendiente")
	}
}

func (p *Pedido) Entregar() {
	if p.status == ENTREGADO {
		fmt.Println("El pedido ya ha sido entregado")
	} else if p.status == CANCELADO {
		fmt.Println("El pedido ya ha sido cancelado")
	} else if p.status == ENVIADO {
		p.status = ENTREGADO
	} else {
		fmt.Println("No se puede entregar un pedido que no está enviado")
	}
}

func (p *Pedido) Estado() string {
	switch p.status {
	case PENDIENTE:
		return "Pedido pendiente"
	case ENVIADO:
		return "Pedido enviado"
	case ENTREGADO:
		return "Pedido entregado"
	case CANCELADO:
		return "Pedido cancelado"
	default:
		return "Estado desconocido"
	}
}

func (p *Pedido) String() string {
	return fmt.Sprintf("Pedido %d: %s", p.id, p.Estado())
}