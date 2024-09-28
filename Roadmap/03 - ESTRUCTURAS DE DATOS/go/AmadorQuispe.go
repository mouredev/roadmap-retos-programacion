package main

import (
	"bufio"
	"errors"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	//inserción, borrado, actualización y ordenación
	//==>Arrays, son estáticos y son del mismo tipo
	arr := [5]int{4, 2, 1, 3}
	fmt.Println("Array de tamaño 5 => ", arr)
	//borrado, actualización
	arr[4] = 5
	// Ordenación
	sort.Ints(arr[:])
	fmt.Println("Array de tamaño 5 ordenada => ", arr)

	//==>Matrices
	matrix := [2][3]int{{1, 2, 3}, {4, 5, 6}}
	fmt.Println("matriz de 2 x 3 => ", matrix)

	//==>Slices, son dinámicos
	slice := []int{1, 2, 3, 4, 5}
	fmt.Println("Slice => ", slice)
	//insertar
	slice = append(slice, 6)
	fmt.Println("Con agregado al final => ", slice)
	//Modificación
	indexToUpdate := 2
	slice[indexToUpdate] = 89
	fmt.Println("Con el indice 2 actualizado =>", slice)
	//Eliminación
	indexToRemove := 2
	slice = append(slice[:indexToRemove], slice[indexToRemove+1:]...)
	fmt.Println("Con el indice 2 eliminado =>", slice)

	//Maps, clave : valor
	weekdays := map[int]string{1: "Lunes", 2: "Martes", 3: "Miércoles", 4: "Jueves", 5: "Viernes", 6: "Sábado", 7: "Domingo"}
	fmt.Println("Mapa => ", weekdays)

	//Structs, estructura de datos que nos permite agrupar datos de diferentes tipos
	type person struct {
		name string
		age  int
	}
	p1 := person{"Amador", 32}
	fmt.Println("Struct => ", p1)

	//EXTRA
	reader := bufio.NewReader(os.Stdin)
	agenda := NewAgenda()

	for {
		fmt.Println("==============================")
		fmt.Println("Agenda de Contactos")
		fmt.Println("0. Listar Contactos")
		fmt.Println("1. Agregar Contacto")
		fmt.Println("2. Buscar Contacto")
		fmt.Println("3. Actualizar Contacto")
		fmt.Println("4. Eliminar Contacto")
		fmt.Println("Escribe 'exit' para salir")
		fmt.Println("==============================")
		fmt.Print("Ingresa una opción: ")
		option, _ := reader.ReadString('\n')
		option = strings.TrimSpace(option)
		if option == "exit" {
			break
		}
		switch option {
		case "0":
			fmt.Println("LISTA CONTACTOS :")
			for key, contact := range agenda.contacts {
				fmt.Println(key, "->", contact)
			}
		case "1":
			fmt.Println("AGREGAR CONTACTO :")
			var name, phone string
			fmt.Print("Ingresa el nombre: ")
			name, _ = reader.ReadString('\n')
			name = strings.TrimSpace(name)
			fmt.Print("Ingresa el # celular: ")
			phone, _ = reader.ReadString('\n')
			phone = strings.TrimSpace(phone)
			err := agenda.addContact(name, phone)
			if err != nil {
				fmt.Println(err)
			} else {
				fmt.Println("Contacto agregado !")
			}

		case "2":
			fmt.Println("BUSCAR CONTACTO :")
			fmt.Print("Ingresa el nombre de contacto a buscar: ")
			inputSearch, _ := reader.ReadString('\n')
			inputSearch = strings.TrimSpace(inputSearch)
			phone, err := agenda.searchByName(inputSearch)
			if err != nil {
				fmt.Println("El contacto", inputSearch, "no se encuentra registrada")
			} else {
				fmt.Println("Contacto encontrado : Nombre =", inputSearch, " Celular  =", phone)
			}
		case "3":
			fmt.Println("ACTUALIZAR CONTACTO :")
			fmt.Print("Ingresa el nombre del contacto a actualizar: ")
			contactToUpdate, _ := reader.ReadString('\n')
			contactToUpdate = strings.TrimSpace(contactToUpdate)
			_, err := agenda.searchByName(contactToUpdate)
			if err != nil {
				fmt.Println("El contacto", contactToUpdate, "no se encuentra registrada")
				break
			}
			fmt.Print("Ingresa el # celular del contacto a actualizar: ")
			phoneToUpdate, _ := reader.ReadString('\n')
			phoneToUpdate = strings.TrimSpace(phoneToUpdate)
			err = agenda.addContact(contactToUpdate, phoneToUpdate)
			if err != nil {
				fmt.Println(err)
			} else {
				fmt.Println("Contacto agregado !")
			}
		case "4":
			fmt.Println("ELIMINAR CONTACTO :")
			fmt.Print("Ingresa el nombre del contacto a eliminar: ")
			contactToDelete, _ := reader.ReadString('\n')
			contactToDelete = strings.TrimSpace(contactToDelete)
			_, err := agenda.searchByName(contactToDelete)
			if err != nil {
				fmt.Println("El contacto", contactToDelete, "no se encuentra registrada")
				break
			}
			agenda.removeContact(contactToDelete)
			fmt.Println("Contacto eliminado !")
		}
	}
}

// IMPLEMENTACIÓN DE AGENDA

type agenda struct {
	contacts map[string]string
}

func NewAgenda() *agenda {
	return &agenda{
		contacts: map[string]string{},
	}
}

func (a *agenda) addContact(name, phone string) error {
	if _, err := a.searchByName(name); err == nil {
		return errors.New("el contacto ya se encuentra registrada")
	}

	if _, err := strconv.Atoi(phone); err != nil || len(phone) > 9 {
		return errors.New("número de teléfono no válido, debe ser numérico y tener máximo 9 dígitos")
	}
	a.contacts[name] = phone
	return nil
}

func (a *agenda) searchByName(name string) (string, error) {
	phone, ok := a.contacts[name]
	if ok {
		return phone, nil
	} else {
		return "", errors.New("contacto no encontrado")
	}
}

func (a *agenda) removeContact(name string) {
	delete(a.contacts, name)
}
