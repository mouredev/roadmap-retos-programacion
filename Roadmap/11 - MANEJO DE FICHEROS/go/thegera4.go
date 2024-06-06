package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"time"
)

func main() {

	crearLeerBorrarArchivo()

	//Extra: Programa de gestión de ventas
	gestionVentas()
}

func crearLeerBorrarArchivo() {
	// Crear el archivo con el nombre de usuario de GitHub
	file, err := os.Create("thegera4.txt")
	if err != nil {
		fmt.Println("Error al crear el archivo:", err)
		return
	}

	// Escribimos en el archivo
	_, err = file.WriteString("Hola, mi nombrer es Gerardo.\n")
	if err != nil {
		fmt.Println("Error al escribir en el archivo:", err)
		return
	}
	_, err = file.WriteString("Tengo 36 años.\n")
	if err != nil {
		fmt.Println("Error al escribir en el archivo:", err)
		return
	}
	_, err = file.WriteString("Mi lenguaje favorito al dia de hoy es Go.\n")
	if err != nil {
		fmt.Println("Error al escribir en el archivo:", err)
		return
	}

	file.Close() // Cerramos el archivo

	// Leemos el archivo
	file, err = os.Open("thegera4.txt")
	if err != nil {
		fmt.Println("Error al abrir el archivo:", err)
		return
	}

	// Imprimimos el contenido
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		fmt.Println(scanner.Text())
	}

	file.Close() // Cerramos el archivo despues de leerlo y mostrarlo para poder borrarlo, si no lo cerramos no se puede borrar.

	// Borramos el archivo al teclear una tecla
	fmt.Println("Pulsa cualquier tecla y luego 'Enter' para borrar el archivo...")
	fmt.Scanln()

	err = os.Remove("thegera4.txt")
	if err != nil {
		fmt.Println("Error al borrar el archivo:", err)
		return
	}

	fmt.Println("Archivo borrado con éxito.")

	// Esperamos 2 segundos antes de finalizar el programa
	time.Sleep(2 * time.Second)

	fmt.Println("Programa finalizado.")
}

func gestionVentas() { 

	//si no existe el archivo "ventas.txt" lo crea
	if _, err := os.Stat("ventas.txt"); os.IsNotExist(err) {
		crearArchivoVentas()
	}

	for{
		var opcion int

		fmt.Println("Bienvenido al sistema de gestión de ventas. Porfavor selecciona una opción:")
		fmt.Println("1. Añadir producto")
		fmt.Println("2. Consultar ventas")
		fmt.Println("3. Actualizar ventas")
		fmt.Println("4. Eliminar producto")
		fmt.Println("5. Venta total")
		fmt.Println("6. Venta por producto")
		fmt.Println("7. Salir")

		fmt.Scanln(&opcion)

		switch opcion {
				case 1:
					agregarProducto()
				case 2:
					consultarVentas()
				case 3:
					actualizarVentas()
				case 4:
					borrarVenta()
				case 5:
					calcularVentaTotal()
				case 6:
					calcularVentaPorProducto()
				case 7:
					cerrarBorrarArchivo()
				default:
					fmt.Println("Opción no válida")
		}
	}
}

func crearArchivoVentas() {
	file, err := os.Create("ventas.txt")
	if err != nil {
		fmt.Println("Error al crear el archivo:", err)
		return
	}
	file.Close()
}

func agregarProducto() {
	file, err := os.OpenFile("ventas.txt", os.O_APPEND|os.O_WRONLY, 0644)
	if err != nil {
		fmt.Println("Error al abrir el archivo:", err)
		return
	}
	defer file.Close()

	var nombre string
	var cantidad int
	var precio float64

	fmt.Println("Introduce el nombre del producto:")
	fmt.Scanln(&nombre)

	fmt.Println("Introduce la cantidad vendida:")
	fmt.Scanln(&cantidad)

	fmt.Println("Introduce el precio:")
	fmt.Scanln(&precio)

	_, err = file.WriteString(fmt.Sprintf("%s, %d, %.2f\n", nombre, cantidad, precio))
	if err != nil {
		fmt.Println("Error al escribir en el archivo:", err)
		return
	}

	fmt.Println("Producto añadido con éxito")
}

func consultarVentas() {
	fmt.Println("Productos vendidos:")

	file, err := os.Open("ventas.txt")
	if err != nil {
		fmt.Println("Error al abrir el archivo:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		fmt.Println(scanner.Text())
	}
}

func actualizarVentas() {
	fmt.Println("Introduce el nombre del producto a actualizar:")
	var nombre string
	fmt.Scanln(&nombre)

	// Abrir el archivo para lectura y escritura
	file, err := os.OpenFile("ventas.txt", os.O_RDWR, 0644)
	if err != nil {
		fmt.Println("Error al abrir el archivo:", err)
		return
	}
	defer file.Close()

	// Leer todas las líneas y actualizar la línea correspondiente
	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		linea := scanner.Text()
		datos := strings.Split(linea, ", ")
		if len(datos) >= 3 && datos[0] == nombre {
			fmt.Println("Venta encontrada:", linea)

			var cantidad int
			var precio float64

			fmt.Println("Introduce la nueva cantidad vendida:")
			fmt.Scanln(&cantidad)

			fmt.Println("Introduce el nuevo precio:")
			fmt.Scanln(&precio)

			// Actualizar la línea
			linea = fmt.Sprintf("%s, %d, %.2f", nombre, cantidad, precio)
		}
		lines = append(lines, linea)
	}

	// Rebobinar el archivo y truncar para escribir desde el principio
	file.Seek(0, 0)
	file.Truncate(0)

	// Escribir todas las líneas actualizadas al archivo
	for _, line := range lines {
		_, err := file.WriteString(line + "\n")
		if err != nil {
			fmt.Println("Error al escribir en el archivo:", err)
			return
		}
	}

	fmt.Println("Venta actualizada con éxito")
}

func borrarVenta() {
	fmt.Println("Introduce el nombre del producto:")
	var nombre string
	fmt.Scanln(&nombre)

	// Abrir el archivo para lectura y escritura
	file, err := os.OpenFile("ventas.txt", os.O_RDWR, 0644)
	if err != nil {
		fmt.Println("Error al abrir el archivo:", err)
		return
	}
	defer file.Close()

	// Leer todas las líneas y eliminar la línea correspondiente
	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		linea := scanner.Text()
		datos := strings.Split(linea, ", ")
		if len(datos) >= 3 && datos[0] == nombre {
			fmt.Println("Venta encontrada y eliminada:", linea)
			continue
		}
		lines = append(lines, linea)
	}

	// Rebobinar el archivo y truncar para escribir desde el principio
	file.Seek(0, 0)
	file.Truncate(0)

	// Escribir todas las líneas actualizadas al archivo
	for _, line := range lines {
		_, err := file.WriteString(line + "\n")
		if err != nil {
			fmt.Println("Error al escribir en el archivo:", err)
			return
		}
	}

	fmt.Println("Venta eliminada con éxito")
}

func calcularVentaTotal() {
	file, err := os.Open("ventas.txt")
	if err != nil {
		fmt.Println("Error al abrir el archivo:", err)
		return
	}
	defer file.Close()

	var total float64
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		linea := scanner.Text()
		datos := strings.Split(linea, ", ")
		if len(datos) >= 3 {
			cantidad := 0
			precio := 0.0
			fmt.Sscanf(datos[1], "%d", &cantidad)
			fmt.Sscanf(datos[2], "%f", &precio)
			total += float64(cantidad) * precio
		}
	}

	fmt.Printf("Venta total actual: %.2f\n", total)
}

func calcularVentaPorProducto() {
	fmt.Println("Introduce el nombre del producto:")
	var nombre string
	fmt.Scanln(&nombre)

	file, err := os.Open("ventas.txt")
	if err != nil {
		fmt.Println("Error al abrir el archivo:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		linea := scanner.Text()
		datos := strings.Split(linea, ", ")
		if len(datos) >= 3 && datos[0] == nombre {
			cantidad := 0
			precio := 0.0
			fmt.Sscanf(datos[1], "%d", &cantidad)
			fmt.Sscanf(datos[2], "%f", &precio)
			fmt.Printf("Venta de %s: %.2f\n", nombre, float64(cantidad) * precio)
			return
		}
	}

	fmt.Println("Producto no encontrado")
}

func cerrarBorrarArchivo() {
	fmt.Println("Estas seguro de que deseas salir? s/n")

	var respuesta string
	fmt.Scanln(&respuesta)

	if respuesta != "s" {
		return
	}

	err := os.Remove("ventas.txt")
	if err != nil {
		fmt.Println("Error al borrar el archivo:", err)
		return
	}

	fmt.Println("Archivo borrado con éxito...Cerrando el programa...")
	os.Exit(0)
}