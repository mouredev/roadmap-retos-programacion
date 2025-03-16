package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

/*
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo que se llame como
 * tu usuario de GitHub y tenga la extensión .txt.
 * Añade varias líneas en ese fichero:
 * - Tu nombre.
 * - Edad.
 * - Lenguaje de programación favorito.
 * Imprime el contenido.
 * Borra el fichero.
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un
 * archivo .txt.
 * - Cada producto se guarda en una línea del archivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
 */
func CreateFile(name string) {

	file, err := os.Create(name)
	if err != nil {
		fmt.Printf("Error creando el archivo %v\n", name)
		return
	}
	defer file.Close()

	fmt.Printf("Archivo creado: %v\n", file.Name())
	file.WriteString("nombre : Rayner\n")
	file.WriteString("edad : 45\n")
	file.WriteString("Lenguaje favorito : Python y Go\n")

}

func ReadFile(name string) {

	file, err := os.Open(name)
	if err != nil {
		fmt.Printf("Error abriendo el archivo %v\n  ", name)
		return
	}
	defer file.Close()
	datos, err := io.ReadAll(file)
	if err != nil {
		fmt.Printf("Error leyendo el archivo %v", file.Name())
	}
	fmt.Printf("Datos del archivo %v\n", file.Name())
	fmt.Println(string(datos))
}

func RemoveFile(name string) {
	err := os.Remove((name))
	if err != nil {
		fmt.Printf("Error eliminando el archivo %v\n", name)
		return
	}

	fmt.Printf("Archivo eliminado %v\n", name)

}

//                      EXTRA

func CrearProducto(name string) {
	scanProductos := bufio.NewScanner(os.Stdin)

	f, err := os.OpenFile(name, os.O_RDWR|os.O_APPEND, 0666)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer f.Close()

	fmt.Print("Nombre del Producto : ")
	scanProductos.Scan()
	nameP := scanProductos.Text()

	fmt.Print("Cantidad   : ")
	scanProductos.Scan()
	amountP := scanProductos.Text()

	fmt.Print("Precio   : ")
	scanProductos.Scan()
	priceP := scanProductos.Text()

	_, err = f.WriteString(fmt.Sprintf("%v, %v, %v\n", nameP, amountP, priceP))
	if err != nil {
		fmt.Println(err)
	}

}

func MostrarTodo(name string) {

	f, err := os.Open(name)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer f.Close()
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		fmt.Println(scanner.Text())
	}

}

func BUscarProducto(source string, prod string) string {

	if strings.Contains(source, prod) {
		return source

	} else {
		return ""
	}
}

func ConsultarProducto(name string) {
	f, err := os.Open(name)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer f.Close()

	scanProductos := bufio.NewScanner(os.Stdin)
	fmt.Print("Nombre del Producto : ")
	scanProductos.Scan()
	nameP := scanProductos.Text()

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		FoundP := BUscarProducto(scanner.Text(), nameP)
		if FoundP != "" {
			fmt.Println(FoundP)
			return
		}

	}
	fmt.Println("Producto no encontrado")

}

// misma fun para actualizar y eliminar, opcion 4 es actualizar y 5 eleminar
func ActualizarP(name string, opcion int) {
	f1, err := os.Open(name)
	if err != nil {
		fmt.Println(err)
	}

	scanner := bufio.NewScanner(f1)

	f2, err := os.OpenFile("TempF.txt", os.O_RDWR|os.O_CREATE, 0666)
	if err != nil {
		fmt.Println(err)
		return
	}

	scanProductos := bufio.NewScanner(os.Stdin)
	fmt.Print("Nombre del Producto : ")
	scanProductos.Scan()
	nameP := scanProductos.Text()
	PF := false
	for scanner.Scan() {
		FoundP := BUscarProducto(scanner.Text(), nameP)
		if FoundP == "" {

			f2.WriteString(fmt.Sprintf("%v\n", scanner.Text()))
		} else {

			// si opcion es 4 actualiza
			if opcion == 4 {

				PF = true
				fmt.Print("Cantidad   : ")
				scanProductos.Scan()
				amountP := scanProductos.Text()

				fmt.Print("Precio   : ")
				scanProductos.Scan()
				priceP := scanProductos.Text()

				_, err = f2.WriteString(fmt.Sprintf("%v, %v, %v\n", nameP, amountP, priceP))
				if err != nil {
					fmt.Println(err)
				}
			} else {
				// si opcion no es 4 entonces no escribe nada, elimina el que encontro
				continue
			}

		}
	}
	if !PF {
		fmt.Println("Producto No encontrado")
	}
	f1.Close()
	f2.Close()

	err1 := os.Rename(f2.Name(), f1.Name())
	if err1 != nil {
		fmt.Println(err)
	}
}

func Ventas(name string) {
	f, err := os.Open(name)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer f.Close()
	scanner := bufio.NewScanner(f)
	total := 0
	for scanner.Scan() {
		amount, _ := strconv.Atoi(strings.Split(scanner.Text(), ", ")[1])
		price, _ := strconv.Atoi(strings.Split(scanner.Text(), ", ")[2])
		total += amount * price

	}
	fmt.Println("Ventas totales   : ", total)
}

func VentasP(name string) {
	f, err := os.Open(name)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer f.Close()
	scanner := bufio.NewScanner(f)
	scanProductos := bufio.NewScanner(os.Stdin)
	fmt.Print("Nombre del Producto : ")
	scanProductos.Scan()
	nameP := scanProductos.Text()
	for scanner.Scan() {
		found := BUscarProducto(scanner.Text(), nameP)
		if found != "" {
			amount, _ := strconv.Atoi(strings.Split(scanner.Text(), ", ")[1])
			price, _ := strconv.Atoi(strings.Split(scanner.Text(), ", ")[2])
			fmt.Printf("Ventas totales del Producto %v : %v\n", nameP, amount*price)
			return
		}

	}
	fmt.Println("Producto no encontrado")

}

func Gestion() {
	name_file := "gestion.txt"
	for {

		fmt.Println("*********** Gestión de Ventas por Productos ***********")
		fmt.Println("1 - Añadir")
		fmt.Println("2 - Consultar un producto")
		fmt.Println("3 - Mostrar todos")
		fmt.Println("4 - Actualizar")
		fmt.Println("5 - Eliminar")
		fmt.Println("6 - Ventas totales")
		fmt.Println("7 - Ventas totales por producto")
		fmt.Println("8 - Salir")
		scannerOp := bufio.NewScanner(os.Stdin)
		scannerOp.Scan()
		op := strings.TrimSpace(scannerOp.Text())
		switch op {
		case "1":
			fmt.Println("Añadir producto")
			fmt.Println()
			CrearProducto(name_file)

		case "2":
			fmt.Println("Consultar un producto")
			fmt.Println()
			ConsultarProducto((name_file))

		case "3":
			fmt.Println("Mostrar todos")
			fmt.Println()
			MostrarTodo((name_file))

		case "4":
			fmt.Println("Actualizar")
			fmt.Println()

			ActualizarP(name_file, 4)

		case "5":
			fmt.Println("Eliminar")
			fmt.Println()
			ActualizarP(name_file, 5)

		case "6":
			fmt.Println("Ventas totales")
			fmt.Println()
			Ventas(name_file)

		case "7":
			fmt.Println("Ventas totales por producto")
			fmt.Println()
			VentasP(name_file)

		case "8":
			fmt.Println("Salir")
			fmt.Println()
			fmt.Println("Se eliminara el archivo creado")
			// err := os.Remove(name_file)
			// if err != nil {
			// 	fmt.Println(err)

			// }

			return
		default:
			fmt.Println("Opción inválida, por favor seleccione una opción entre 1 y 8.")
		}

		fmt.Println()
	}

}
func main() {
	fmt.Println("EJERCICIO RETO 11, MANEJO ARCHIVOS")
	fmt.Println()
	name := "raynerpv2022.txt"
	CreateFile(name)
	ReadFile(name)
	RemoveFile(name)

	Gestion()
}
