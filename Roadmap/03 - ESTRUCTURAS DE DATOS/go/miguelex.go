package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Contact struct {
	Name  string
	Phone string
}

type Agenda map[string]Contact

func inc(i *int) {
	*i++
}

func searchContact(reader *bufio.Reader, agenda Agenda) {
	fmt.Print("Ingrese el nombre del contacto que desea buscar: ")
	name, _ := reader.ReadString('\n')
	name = strings.TrimSpace(name)

	contact, found := agenda[name]
	if found {
		fmt.Println("Nombre:", contact.Name)
		fmt.Println("Teléfono:", contact.Phone)
	} else {
		fmt.Println("El contacto no existe en la agenda.")
	}
}

func insertContact(reader *bufio.Reader, agenda Agenda) {
	fmt.Print("Ingrese el nombre del nuevo contacto: ")
	name, _ := reader.ReadString('\n')
	name = strings.TrimSpace(name)

	fmt.Print("Ingrese el número de teléfono del nuevo contacto: ")
	phone, _ := reader.ReadString('\n')
	phone = strings.TrimSpace(phone)

	// Verificar si el número de teléfono es válido
	if _, err := strconv.Atoi(phone); err != nil || len(phone) > 11 {
		fmt.Println("Número de teléfono no válido. Debe ser numérico y tener 11 dígitos como máximo.")
		return
	}

	agenda[name] = Contact{Name: name, Phone: phone}
	fmt.Println("Contacto agregado correctamente.")
}

func updateContact(reader *bufio.Reader, agenda Agenda) {
	fmt.Print("Ingrese el nombre del contacto que desea actualizar: ")
	name, _ := reader.ReadString('\n')
	name = strings.TrimSpace(name)

	_, found := agenda[name]
	if !found {
		fmt.Println("El contacto no existe en la agenda.")
		return
	}

	fmt.Print("Ingrese el nuevo número de teléfono: ")
	phone, _ := reader.ReadString('\n')
	phone = strings.TrimSpace(phone)

	// Verificar si el número de teléfono es válido
	if _, err := strconv.Atoi(phone); err != nil || len(phone) > 11 {
		fmt.Println("Número de teléfono no válido. Debe ser numérico y tener 11 dígitos como máximo.")
		return
	}

	agenda[name] = Contact{Name: name, Phone: phone}
	fmt.Println("Contacto actualizado correctamente.")
}

func deleteContact(reader *bufio.Reader, agenda Agenda) {
	fmt.Print("Ingrese el nombre del contacto que desea eliminar: ")
	name, _ := reader.ReadString('\n')
	name = strings.TrimSpace(name)

	_, found := agenda[name]
	if !found {
		fmt.Println("El contacto no existe en la agenda.")
		return
	}

	delete(agenda, name)
	fmt.Println("Contacto eliminado correctamente.")
}

func main() {

	// Arrays
	var arr [5]int
	arr[0] = 1
	arr[1] = 2
	arr[2] = 3
	arr[3] = 4
	arr[4] = 5
	fmt.Println(arr)

	// Slices
	slice := []int{1, 2, 3, 4, 5}
	fmt.Println(slice)
	fmt.Println(slice[2:4])

	// Maps
	m := make(map[string]int)
	m["key1"] = 1
	m["key2"] = 2
	fmt.Println(m)

	// Structs
	type person struct {
		name string
		age  int
	}
	p := person{name: "Miguel", age: 25}
	fmt.Println(p)

	// Pointers
	i := 7
	inc(&i)
	fmt.Println(i)

	// Extra

	agenda := make(Agenda)
	reader := bufio.NewReader(os.Stdin)

	for {
		fmt.Println("\nOperaciones disponibles:")
		fmt.Println("1. Búsqueda de contacto")
		fmt.Println("2. Inserción de contacto")
		fmt.Println("3. Actualización de contacto")
		fmt.Println("4. Eliminación de contacto")
		fmt.Println("5. Salir del programa")

		fmt.Print("\nSeleccione la operación que desea realizar (1-5): ")
		choiceStr, _ := reader.ReadString('\n')
		choiceStr = strings.TrimSpace(choiceStr)
		choice, err := strconv.Atoi(choiceStr)
		if err != nil || choice < 1 || choice > 5 {
			fmt.Println("Por favor, ingrese un número válido entre 1 y 5.")
			continue
		}

		switch choice {
		case 1:
			searchContact(reader, agenda)
		case 2:
			insertContact(reader, agenda)
		case 3:
			updateContact(reader, agenda)
		case 4:
			deleteContact(reader, agenda)
		case 5:
			fmt.Println("Saliendo del programa...")
			return
		}
	}
}
