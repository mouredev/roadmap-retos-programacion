// # #03 ESTRUCTURAS DE DATOS
// > #### Dificultad: Media | Publicación: 15/01/24 | Corrección: 22/01/24

// ## Ejercicio

// ```
// /*
//  * EJERCICIO:
//  * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
//  * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
//  *
//  * DIFICULTAD EXTRA (opcional):
//  * Crea una agenda de contactos por terminal.
//  * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
//  * - Cada contacto debe tener un nombre y un número de teléfono.
//  * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
//  *   los datos necesarios para llevarla a cabo.
//  * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
//  *   (o el número de dígitos que quieras)
//  * - También se debe proponer una operación de finalización del programa.
//  */
// ```
// #### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.

// Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

// > Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.

package main

import (
	"fmt"
	"sort"
)

func array() {
	// array inicial
	ciudades := [3]string{"carora", "barquisimeto", "valencia"}
	fmt.Println("esto es el array inicial ===> ", ciudades)

	//aray despues de modificar
	ciudades[2] = "caracas"
	fmt.Println("esto es el array modificado ===> ", ciudades)
}

func slice() {
	// slice inicial
	paises := []string{"rusia", "china", "venezuela"}
	fmt.Println("esto es el slice inicial ===> ", paises)

	// modificacion del slice
	paises[2] = "venezuela modificada"
	fmt.Println("esto es el slice inicial ===> ", paises)

	//agregando en el slice
	paises = append(paises, "chile", "peru", "argentina")
	fmt.Println("esto es el slice con paises agregados ===> ", paises)

	//quitar elementos en el slice
	// buscando el index de peru
	var index int
	for i, pais := range paises {
		if pais == "peru" {
			index = i
			break
		}
	}
	paises = append(paises[:index], paises[index+1:]...)
	fmt.Println("esto es el slice con paises borrados ===> ", paises)

	//ordenando el slice
	sort.Strings(paises)
	fmt.Println("esto es el slice con paises ordenados ===> ", paises)

	// ordenando el slice de manera descendente
	sort.Sort(sort.Reverse(sort.StringSlice(paises)))
	fmt.Println("esto es el slice con paises ordenados de manera descendente ===> ", paises)

}

func agendaAdicional() {

	// variables y mapas
	agenda := make(map[string]int)
	agenda["frey"] = 957985975
	agenda["zeoly"] = 937639373

	//Ingresar el valor por consola
	var nombre string
	var numero int
	var opcion int

	//verificacion de numero
	validarNumero := func(numero int) bool {
		if numero >= 100000000 && numero <= 999999999 {
			return true
		} else {
			return false
		}
	}

	// opciones que aparecen en la consola
	for {
		// Validación para la opción ingresada
		fmt.Println("Marque una de las siguientes opciones")
		fmt.Println("1. Para buscar un contacto")
		fmt.Println("2. Para modificar un contacto")
		fmt.Println("3. Para agregar un contacto")
		fmt.Println("4. Para eliminar un contacto")
		fmt.Println("5. Para mostrar todos los contactos")
		fmt.Println("6. Para salir")

		// Validar que la opción sea un número entero
		_, err := fmt.Scanln(&opcion)
		if err != nil || opcion < 1 || opcion > 6 {
			fmt.Println("Opción inválida. Por favor ingrese un número entre 1 y 6.")
			continue
		}

		//Buscar contactos registrados
		switch opcion {
		case 1:
			fmt.Println("Por favor ingrese el nombre del contacto que desea buscar")
			fmt.Scanln(&nombre)
			numero, ok := agenda[nombre]
			if ok {
				fmt.Printf("El nombre del contacto es %s y su número es %d \n\n", nombre, numero)
			} else {
				fmt.Printf("El contacto con nombre %s no está registrado\n", nombre)
			}

		//Modificar un contacto
		case 2:
			fmt.Println("Ingrese por favor el nombre del contacto que desea modificar")
			fmt.Scanln(&nombre)
			numero, ok := agenda[nombre]
			if ok {
				fmt.Println("Por favor ingrese el nuevo número")
				// Validación para el nuevo número
				_, err := fmt.Scanln(&numero)
				if err != nil || !validarNumero(numero) {
					fmt.Println("Número incorrecto. Debe ser un número válido de 9 dígitos.")
				} else {
					agenda[nombre] = numero
					fmt.Printf("Se ha actualizado el número de %s \n", nombre)
					fmt.Printf("El nuevo número es: %d \n", numero)
				}
			} else {
				fmt.Printf("El contacto con nombre %s no está registrado \n", nombre)
			}

		// Agregar un contacto
		case 3:
			fmt.Println("Ingrese por favor el nombre del contacto que desea agregar")
			fmt.Scanln(&nombre)
			fmt.Println("Ingrese por favor el número del contacto que desea agregar")
			// Validación para el número
			_, err := fmt.Scanln(&numero)
			if err != nil || !validarNumero(numero) {
				fmt.Println("Número incorrecto. Debe ser un número válido de 9 dígitos.")
			} else {
				agenda[nombre] = numero
				fmt.Printf("Se ha agregado el contacto %s con el número %d \n", nombre, numero)
			}

		// Eliminar un contacto
		case 4:
			fmt.Println("Ingrese por favor el nombre del contacto que desea eliminar")
			fmt.Scanln(&nombre)
			_, ok := agenda[nombre]
			if ok {
				delete(agenda, nombre)
				fmt.Printf("Se ha eliminado el contacto %s \n", nombre)
			} else {
				fmt.Printf("El usuario %s no se encuentra registrado \n", nombre)
			}

		// Mostrar todos los contactos
		case 5:
			if len(agenda) == 0 {
				fmt.Println("La agenda está vacía")
			} else {
				fmt.Println("Estos son los contactos registrados:")
				for nombre, numero := range agenda {
					fmt.Printf("El contacto %s tiene el número %d \n", nombre, numero)
				}
			}

		// Terminar programa
		case 6:
			fmt.Println("Programa finalizado.")
			return

		// Valor por defecto
		default:
			fmt.Println("Por favor ingrese una opción válida.")
		}
	}
}

func main() {
	array()
	slice()
	agendaAdicional()
}
