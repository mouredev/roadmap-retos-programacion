package main

import (
	"fmt"
	"time"
)

//	/*
//
// #  * EJERCICIO:
// #  * Empleando tu lenguaje, explora la definición del tipo de dato
// #  * que sirva para definir enumeraciones (Enum).
// #  * Crea un Enum que represente los días de la semana del lunes
// #  * al domingo, en ese orden. Con ese enumerado, crea una operación
// #  * que muestre el nombre del día de la semana dependiendo del número entero
// #  * utilizado (del 1 al 7).
type WeekDay int

const (
	monday WeekDay = iota
	tuesday
	wednesday
	thrusday
	friday
	saturday
	sunday
)

func (w WeekDay) String() string {
	days := [...]string{"", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
	return days[w]
}

func getDay(index int) WeekDay {
	return WeekDay(index)
}

type Estado int

const (
	PENDIENTE Estado = iota + 1
	ENVIADO
	ENTREGADO
	CANCELADO
)

func (e Estado) String() string {
	switch e {
	case PENDIENTE:
		return "PENDIENTE"
	case ENVIADO:
		return "ENVIADO"
	case ENTREGADO:
		return "ENTREGADO"
	case CANCELADO:
		return "CANCELADO"
	default:
		return "UNKNOWN"
	}
}

type Pedido struct {
	Serial string
	ID     Estado
}

func (p *Pedido) Enviar() {
	if p.ID == PENDIENTE {
		p.ID = ENVIADO
		fmt.Printf("Pedido %s ha sido enviado\n", p.Serial)
	} else if p.ID == CANCELADO {
		fmt.Printf("Pedido %s está Cancelado\n", p.Serial)
	} else {
		fmt.Printf("Pedido %s no puede ser Enviado porque no está pendiente\n", p.Serial)
	}
}

func (p *Pedido) MostrarEstado() string {
	return fmt.Sprintf("El estado actual del pedido %s es: %s", p.Serial, p.ID)
}

func (p *Pedido) Cancelar() {
	if p.ID == CANCELADO {
		fmt.Printf("Pedido %s ya está Cancelado\n", p.Serial)
	} else if p.ID != ENTREGADO {
		p.ID = CANCELADO
		fmt.Printf("Pedido %s ha sido Cancelado\n", p.Serial)
	} else {
		fmt.Printf("Pedido %s no puede ser Cancelado porque ya se entregó\n", p.Serial)
	}
}

func (p *Pedido) Entregar() {
	if p.ID == ENVIADO {
		p.ID = ENTREGADO
		fmt.Printf("Pedido %s ha sido Entregado\n", p.Serial)
	} else if p.ID == CANCELADO {
		fmt.Printf("Pedido %s está Cancelado\n", p.Serial)
	} else {
		fmt.Printf("Pedido %s no puede ser Entregado porque no se ha enviado\n", p.Serial)
	}
}

func clearScreen() {
	// Clear the screen (works for Unix-like systems)
	fmt.Print("\033[H\033[J")
}

func buscarPedido(pedidos []*Pedido, serial string) int {
	for i, pedido := range pedidos {
		if pedido.Serial == serial {
			return i
		}
	}
	return -1
}
func seleccionarProducto(pedidos []*Pedido, serial string) {
	index := buscarPedido(pedidos, serial)
	if index == -1 {
		fmt.Println("Pedido no encontrado")
		return
	}

	clearScreen()
	eliminar := false
	for {
		fmt.Println("1 - Ver Estado", serial)
		fmt.Println("2 - Enviar Pedido", serial)
		fmt.Println("3 - Cancelar Pedido", serial)
		fmt.Println("4 - Entregar Pedido", serial)
		fmt.Println("5 - Salir del Producto", serial)

		var s string
		fmt.Scanln(&s)
		switch s {
		case "1":
			fmt.Println("Mostrando Estado")
			fmt.Println(pedidos[index].MostrarEstado())
		case "2":
			fmt.Println("Enviando Producto")
			pedidos[index].Enviar()
		case "3":
			fmt.Println("Cancelando Producto")
			pedidos[index].Cancelar()
			eliminar = true
		case "4":
			fmt.Println("Entregando Producto")
			pedidos[index].Entregar()
		case "5":
			fmt.Println("Saliendo del Producto")
			if eliminar {
				fmt.Printf("Pedido %s Eliminado\n", pedidos[index].Serial)
				fmt.Println(pedidos[:index])
				fmt.Println(pedidos[index+1:])

				pedidos = append(pedidos[:index], pedidos[index+1:]...) //bug al eliminar repite el ultimo elemento
			}
			break
		default:
			fmt.Println("Opción Inválida")
		}

		if s == "5" {
			break
		}
	}
}
func main() {
	pedidos1 := []int{0, 1, 2, 3, 4, 5}
	index := 3
	pedidos1 = append(pedidos1[:index], pedidos1[index+1:]...)
	fmt.Println(pedidos1)

	fmt.Println(getDay(7))

	fmt.Println("EXTRA")

	var pedidos []*Pedido
	serial := 100

	for {
		fmt.Println("Seleccione opción")
		fmt.Println("1 - Crear Pedido")
		fmt.Println("2 - Mostrar todos Pedidos")
		fmt.Println("3 - Seleccionar Pedido")
		fmt.Println("4 - Salir")

		var op string
		fmt.Scanln(&op)

		switch op {
		case "1":
			serial++
			pedidos = append(pedidos, &Pedido{
				Serial: fmt.Sprintf("%dA", serial),
				ID:     PENDIENTE,
			})
		case "2":
			fmt.Println("Mostrando Todos los Pedidos")
			for _, pedido := range pedidos {
				fmt.Printf("Pedido: %s Estado: %s\n", pedido.Serial, pedido.ID)
			}
		case "3":
			fmt.Println("Indique serial del pedido")
			var serialInput string
			fmt.Scanln(&serialInput)
			seleccionarProducto(pedidos, serialInput)
		case "4":
			fmt.Println("Saliendo...")
			for i := 10; i > 0; i-- {
				fmt.Print(i, " ")
				time.Sleep(time.Second)
			}
			fmt.Println("\nPrograma terminado")
			return
		default:
			fmt.Println("Opción no válida, 1-4")
		}
	}

}
