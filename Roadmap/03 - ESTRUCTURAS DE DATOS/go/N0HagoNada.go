package main

import (
	"bufio"
	"errors"
	"fmt"
	"os"
	"regexp"
	"sort"
	"unicode"
)

// Estructrua de Contacto
type Contacto struct {
	Nombre string
	Tel    string
	Correo string
}

func (c *Contacto) ActualizarEmail(nuevoEmail string) {
	c.Correo = nuevoEmail
}
func (c *Contacto) ActualizarTel(nuevoTel string) {
	c.Tel = nuevoTel
}

func (c *Contacto) ActualizarNombre(nuevoNombre string) {
	c.Nombre = nuevoNombre
}

var agenda []Contacto

func main() {
	estructurasEnGo()
	// Alamcenamiento, incializado
	scanner := bufio.NewScanner(os.Stdin)
	for {
		fmt.Println("Agenda de Contactos")
		fmt.Println("1. Agregar Contacto")
		fmt.Println("2. Buscar Contacto")
		fmt.Println("3. Actualizar Contacto")
		fmt.Println("4. Eliminar Contacto")
		fmt.Println("Escribe 'exit' para salir")
		fmt.Print("Elige una opción: ")

		scanner.Scan()
		entrada := scanner.Text()

		if entrada == "exit" {
			break
		}

		switch entrada {
		case "1":
			// Lógica para agregar contacto
			var nombre, telefono, correo string
			fmt.Print("Ingresa el nombre del contacto: ")
			scanner.Scan()
			nombre = scanner.Text()

			fmt.Print("Ingresa el teléfono del contacto: ")
			scanner.Scan()
			telefono = scanner.Text()

			fmt.Print("Ingresa el correo electrónico del contacto: ")
			scanner.Scan()
			correo = scanner.Text()

			// Aquí llamamos a la función para agregar el contacto.
			// Suponiendo que tu función se llama agregarContacto y devuelve un error si falla.
			err := agregarContacto(&agenda, nombre, telefono, correo)
			if err != nil {
				fmt.Println("Error al agregar contacto:", err)
			} else {
				fmt.Println("Contacto agregado exitosamente: ", agenda)
			}
		case "2":
			// Lógica para buscar contacto
			var correo string
			fmt.Print("Ingresa el correo electrónico del contacto: ")
			scanner.Scan()
			correo = scanner.Text()
			_, contactoNuevo, err := busquedaContacto(agenda, correo)
			if err != nil {
				fmt.Println("Error al buscar contacto:", err)
			} else {
				fmt.Println("Nombre: "+contactoNuevo.Nombre, "Telefono: "+contactoNuevo.Tel)
			}
		case "3":
			var nombre, telefono, correo string
			fmt.Print("Ingresa el nombre del contacto: ")
			scanner.Scan()
			nombre = scanner.Text()

			fmt.Print("Ingresa el teléfono del contacto: ")
			scanner.Scan()
			telefono = scanner.Text()

			fmt.Print("Ingresa el correo electrónico del contacto: ")
			scanner.Scan()
			correo = scanner.Text()
			err := ActualizarContacto(&agenda, nombre, telefono, correo)
			if err != nil {
				fmt.Println("Error al Actualizar contacto:", err)
			} else {
				fmt.Println("Contacto actualizado")
			}
		case "4":
			var correo string
			fmt.Print("Ingresa el correo electrónico del contacto: ")
			scanner.Scan()
			correo = scanner.Text()
			err := eliminarContacto(&agenda, correo)
			if err != nil {
				fmt.Println("Error al eliminar contacto:", err)
			} else {
				fmt.Println("Contacto eliminado")
			}
		default:
			fmt.Println("Opción no válida, por favor intenta de nuevo.")
		}
	}
}

func agregarContacto(agenda *[]Contacto, nombre, telefono, correo string) error {
	// Validación del nombre
	if nombre == "" {
		return errors.New("el nombre no puede estar vacío")
	}

	// Validación del teléfono
	if len(telefono) >= 9 {
		return errors.New("el teléfono debe tener menos de 9 dígitos")
	}
	for _, c := range telefono {
		if !unicode.IsDigit(c) {
			return errors.New("el teléfono solo debe contener dígitos")
		}
	}

	// Validación del correo electrónico
	re := regexp.MustCompile(`^[a-z0-9._%+\-]+@[a-z0-9.\-]+\.[a-z]{2,4}$`)
	if !re.MatchString(correo) {
		return errors.New("formato de correo electrónico inválido")
	}

	// Agregar el contacto
	nuevoContacto := Contacto{Nombre: nombre, Tel: telefono, Correo: correo}
	*agenda = append(*agenda, nuevoContacto)

	return nil
}

func busquedaContacto(agenda []Contacto, correo string) (int, *Contacto, error) {
	for i, contacto := range agenda {
		if contacto.Correo == correo {
			return i, &contacto, nil
		}
	}
	return -1, nil, errors.New("Correo no se encuentra en la lista de contacto")
}
func eliminarContacto(agenda *[]Contacto, correo string) error {
	indice, _, err := busquedaContacto(*agenda, correo)
	if err != nil {
		return err
	}

	*agenda = append((*agenda)[:indice], (*agenda)[indice+1:]...)
	return nil
}
func ActualizarContacto(agenda *[]Contacto, nombre, telefono, correo string) error {
	indice, _, err := busquedaContacto(*agenda, correo)
	if err != nil {
		return err
	}
	(*agenda)[indice].Nombre = nombre
	(*agenda)[indice].Tel = telefono
	return errors.New("No es posible actualizar contacto")
}

func estructurasEnGo() {
	var miArray [5]int // Array de 5 enteros
	miArray[0] = 100
	miArray[1] = 200
	// Acceder a los elementos: miArray[0], miArray[1], etc.
	miSlice := []int{10, 20, 30, 40, 50}
	miSlice = append(miSlice, 60) // Añadir un elemento al final
	// Acceder a los elementos: miSlice[0], miSlice[1], etc.
	slice := []int{3, 1, 4, 1}
	sort.Ints(slice)
	// Ahora slice está ordenado
	sliceStrings := []string{"z", "a", "b"}
	sort.Strings(sliceStrings)
	// Ahora slice está ordenado
	sort.Slice(slice, func(i, j int) bool {
		return slice[i] < slice[j] // Criterio de comparación
	})
	// Ahora slice está ordenado según tu criterio
	fmt.Println(slice)
	miMap := make(map[string]int)
	miMap["clave1"] = 100
	miMap["clave2"] = 200
	// Acceder a los valores: miMap["clave1"], miMap["clave2"]
	user := Contacto{"Juan", "02123112111", "user@user.com"}
	fmt.Println(user)
}
