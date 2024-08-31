package main

import (
	"fmt"
	"sort"
)

func main() {

	// Slice (Array / Lista)
	var slice []int

	//Agregar
	slice = append(slice, 1) 
	slice = append(slice, 2) // Cada que se inserta un dato se inserta al final
	fmt.Println("Slice inicial con datos: ",slice)

	slice = append([]int{0}, slice...) //si queremos agregar al principio
	fmt.Println("Slice con dato agregado en el primer indice: ",slice)

	slice = append(slice[:1], append([]int{3}, slice[1:]...)...) //para agregar en un indice especifico: agregar el 3 en el indice 1
	fmt.Println("Slice con dato agregado en el indice 1: ",slice)

	//Eliminar
	slice = append(slice[:1], slice[2:]...) //para eliminar un elemento desde posicion 1 hasta 2 no inclusive, osea solo el "1"
	fmt.Println("Slice con dato eliminado: ",slice)

	//Actualizar
	slice[0] = 10
	fmt.Println("Slice con dato actualizado: ",slice)

	//Buscar
	for i := 0; i < len(slice); i++ {
		if slice[i] == 10 {
			fmt.Println("El dato se encuentra en el indice: ", i)
		}
	}

	//Ordenar
	slice = append(slice, 5)
	sort.Ints(slice)
	fmt.Println("Slice ordenado ascendente: ",slice)
	sort.Sort(sort.Reverse(sort.IntSlice(slice)))
	fmt.Println("Slice ordenado descendente: ",slice)

	//Mapa
	var mapa = make(map[string]int) //mapa con llave string y valor int
	mapa["Juan"] = 12345678900
	mapa["Pedro"] = 12345678911
	mapa["Maria"] = 12345678922
	fmt.Println("Mapa inicial: ", mapa)

	//Agregar
	mapa["Jose"] = 12345678933
	fmt.Println("Mapa con dato agregado: ", mapa)

	//Eliminar
	delete(mapa, "Jose")
	fmt.Println("Mapa con dato eliminado: ", mapa)

	//Actualizar
	mapa["Juan"] = 12345678999
	fmt.Println("Mapa con dato actualizado: ", mapa)

	//Buscar
	telefono, ok := mapa["Juan"]
	if ok {
		fmt.Println("El teléfono del contacto es: ", telefono)
	} else {
		fmt.Println("El contacto no existe")
	}

	//Ordenar
	var keys []string
	for k := range mapa {
		keys = append(keys, k)
	}
	sort.Strings(keys)
	fmt.Println("Mapa ordenado: ", mapa)

	//Dificultad extra
	AgendaExtra()

}

func AgendaExtra() {
	var agenda = make(map[string]int) //mapa con llave string y valor int
	agenda["Juan"] = 12345678900
	agenda["Pedro"] = 12345678911
	agenda["Maria"] = 12345678922
	var opcion int
	var nombre string
	var telefono int
	var invalidTel bool

	for {
		fmt.Println("******Bienvenido a la agenda de contactos******")
		fmt.Println("Por favor, selecciona una opción:")
		fmt.Println("1  Agregar contacto")
		fmt.Println("2  Buscar contacto")
		fmt.Println("3  Actualizar contacto")
		fmt.Println("4  Eliminar contacto")
		fmt.Println("5  Mostrar todos los contactos")
		fmt.Println("6  Salir")
		fmt.Scanln(&opcion)

		switch opcion {
		case 1:
			fmt.Println("Ingresa el nombre del contacto a agregar:")
			fmt.Scanln(&nombre)
			fmt.Println("Ingrese el teléfono del contacto:")
			fmt.Scanln(&telefono)
			invalidTel = CheckTelInvalid(telefono)
			if invalidTel {
				fmt.Println("El teléfono ingresado no es válido")
				break
			}
			agenda[nombre] = telefono
			fmt.Println("Contacto agregado exitosamente")
		case 2:
			fmt.Println("Ingrese el nombre del contacto a buscar")
			fmt.Scanln(&nombre)
			telefono, ok := agenda[nombre]
			if ok {
				fmt.Println("El teléfono del contacto es: ", telefono)
			} else {
				fmt.Println("El contacto no existe")
			}
		case 3:
			fmt.Println("Ingrese el nombre del contacto a actualizar: ")
			fmt.Scanln(&nombre)
			fmt.Println("Ingrese el nuevo teléfono del contacto:")
			fmt.Scanln(&telefono)
			invalidTel = CheckTelInvalid(telefono)
			if invalidTel {
				fmt.Println("El teléfono ingresado no es válido")
				break
			}
			agenda[nombre] = telefono
			fmt.Println("Contacto actualizado exitosamente")
		case 4:
			fmt.Println("Ingrese el nombre del contacto a eliminar:")
			fmt.Scanln(&nombre)
			delete(agenda, nombre)
			fmt.Println("Contacto eliminado exitosamente")
		case 5:
			fmt.Println("Contactos guardados:")
			for k, v := range agenda {
				fmt.Println(k, v)
			}
		case 6:
			fmt.Println("Gracias por usar la agenda")
			return
		default:
			fmt.Println("Opción no válida")
		}
	}

}

func CheckTelInvalid (telefono int) bool {
	if telefono < 10000000000 {
		return false
	} else {
		return true
	}
}