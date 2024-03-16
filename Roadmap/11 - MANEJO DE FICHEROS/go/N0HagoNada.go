package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
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
 * - Cada producto se guarda en una línea del arhivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
 */

func main() {
	// Ejercicio
	tempFile, err := os.Create("N0HagoNada.txt")
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println("Archivo creado con extio: ", tempFile.Name())
	err = tempFile.Close()
	if err != nil {
		fmt.Println(err)
		return
	}
	file, err := os.OpenFile("N0HagoNada.txt", os.O_APPEND|os.O_WRONLY, 0644)
	if err != nil {
		fmt.Println(err)
		return
	}
	_, err = file.WriteString("Nombre: Juan David \n")
	if err != nil {
		fmt.Println(err)
		return
	}
	_, err = file.WriteString("Edad: 31 \n")
	_, err = file.WriteString("Lenguaje de programación favorito: go")
	err = file.Close()
	if err != nil {
		fmt.Println(err)
		return
	}
	file, err = os.Open("N0HagoNada.txt")
	data, err := io.ReadAll(file)
	if err != nil {
		fmt.Println(err)
		return
	}
	content := string(data)
	fmt.Println(content)
	err = file.Close()
	if err != nil {
		fmt.Println(err)
		return
	}
	err = os.Remove(tempFile.Name())
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println("******************************* RETO *************************************************")
	cuentas, err := os.Create("Tienda.txt")
	nombreArchivo := cuentas.Name()
	cuentas.Close()
	if err != nil {
		fmt.Println(err)
		return
	}
	scanner := bufio.NewScanner(os.Stdin)
	for {
		fmt.Println("Bienvenido al inventario para la tienda de la esquina")
		fmt.Println("1. Añadir Producto")
		fmt.Println("2. Consultar producto por nombre")
		fmt.Println("3. Actualizar producto")
		fmt.Println("4. Eliminar producto")
		fmt.Println("Escribe 'exit' para salir")
		fmt.Print("Elige una opción: ")
		scanner.Scan()
		input := strings.TrimSpace(scanner.Text())
		if strings.ToLower(input) == "exit" {
			err := os.Remove(nombreArchivo)
			if err != nil {
				fmt.Println(err)
				return
			}
			break
		}
		switch input {
		case "1":
			// Lógica para agregar producto
			var nombreProducto, cantidadVendiad, precio string
			fmt.Print("Ingresa el nombreProducto: ")
			scanner.Scan()
			nombreProducto = scanner.Text()

			fmt.Print("Ingresa la cantidadVendiad: ")
			scanner.Scan()
			cantidadVendiad = scanner.Text()

			fmt.Print("Ingresa el precio: ")
			scanner.Scan()
			precio = scanner.Text()

			construirLinea := fmt.Sprintf("%s, %s, %s \n", nombreProducto, cantidadVendiad, precio)
			err = agregarProducto(nombreArchivo, construirLinea)
			if err != nil {
				fmt.Println(err)
				return
			}

		case "2":
			// Lógica para consultar
			var nombreProducto string
			fmt.Print("Ingresa el nombreProducto: ")
			scanner.Scan()
			nombreProducto = scanner.Text()
			encontrado, err := consultarProdcuto(nombreArchivo, nombreProducto)
			if err != nil {
				fmt.Println(err)
				continue
			}
			fmt.Println(encontrado)

		case "3":
			// Lógica para actualizar
			var nombreProducto, cantidadVendiad, precio string
			fmt.Print("Ingresa el nombreProducto a actualizar: ")
			scanner.Scan()
			nombreProducto = scanner.Text()
			fmt.Print("Ingresa la cantidadVendiad: ")
			scanner.Scan()
			cantidadVendiad = scanner.Text()

			fmt.Print("Ingresa el precio: ")
			scanner.Scan()
			precio = scanner.Text()
			construirLinea := fmt.Sprintf("%s, %s, %s \n", nombreProducto, cantidadVendiad, precio)
			err := actualizarlineaEnArchivo(nombreArchivo, nombreProducto, construirLinea)
			if err != nil {
				fmt.Println(err)
				return
			}

		case "4":
			// Lógica para eliminar
			var nombreProducto string
			fmt.Print("Ingresa el nombreProducto: ")
			scanner.Scan()
			nombreProducto = scanner.Text()
			err := eliminarLineaenArchivo(nombreArchivo, nombreProducto)
			if err != nil {
				fmt.Println(err)
				return
			}

		default:
			fmt.Println("Opción no válida, por favor intenta de nuevo.")
		}
	}
}

func agregarProducto(nombre string, linea string) error {
	archivo, err := os.OpenFile(nombre, os.O_APPEND|os.O_WRONLY, 0666)
	if err != nil {
		return err
	}
	_, err = archivo.WriteString(linea)
	if err != nil {
		// Manejo del error
		return err
	}
	defer archivo.Close()
	return nil
}
func consultarProdcuto(nombre string, producto string) (string, error) {
	archivo, err := os.OpenFile(nombre, os.O_RDONLY, 0666)
	if err != nil {
		return "", err
	}
	defer archivo.Close()
	scanner := bufio.NewScanner(archivo)
	for scanner.Scan() {
		linea := scanner.Text()
		if strings.Contains(linea, producto) {
			return linea, nil
		}
	}
	return "", fmt.Errorf("no se encontro %s", producto)
}
func actualizarlineaEnArchivo(nombreArchivo, lineaBuscar, lineaNueva string) error {
	archivo, err := os.OpenFile(nombreArchivo, os.O_RDWR, 0666)
	if err != nil {
		return err
	}
	// Crear un archivo temporal
	tempArchivo, err := os.CreateTemp("", "temp")
	if err != nil {
		return err
	}
	scanner := bufio.NewScanner(archivo)
	var lineaActualizada bool

	// Leer y escribir al archivo temporal
	for scanner.Scan() {
		linea := scanner.Text()
		if strings.Contains(linea, lineaBuscar) && !lineaActualizada {
			_, err = tempArchivo.WriteString(lineaNueva + "\n")
			lineaActualizada = true // Asegura que solo se actualice la primera coincidencia
		} else {
			_, err = tempArchivo.WriteString(linea + "\n")
		}
		if err != nil {
			return err
		}
	}
	// Verificar errores al leer el archivo
	if err := scanner.Err(); err != nil {
		return err
	}
	archivo.Close()
	tempArchivo.Close()
	// Reemplazar el archivo original con el archivo temporal
	err = os.Rename(tempArchivo.Name(), nombreArchivo)
	if err != nil {
		return err
	}
	return nil
}

func eliminarLineaenArchivo(nombreArchivo, lineaBuscar string) error {
	archivo, err := os.OpenFile(nombreArchivo, os.O_RDWR, 0666)
	if err != nil {
		return err
	}
	// Crear un archivo temporal
	tempArchivo, err := os.CreateTemp("", "temp")
	if err != nil {
		return err
	}
	scanner := bufio.NewScanner(archivo)

	// Leer y escribir al archivo temporal
	for scanner.Scan() {
		linea := scanner.Text()
		if strings.Contains(linea, lineaBuscar) {
			continue
		} else {
			_, err = tempArchivo.WriteString(linea + "\n")
		}
		if err != nil {
			return err
		}
	}
	// Verificar errores al leer el archivo
	if err := scanner.Err(); err != nil {
		return err
	}
	err = archivo.Close()
	if err != nil {
		return err
	}
	err = tempArchivo.Close()
	if err != nil {
		return err
	}
	// Reemplazar el archivo original con el archivo temporal
	err = os.Rename(tempArchivo.Name(), nombreArchivo)
	if err != nil {
		return err
	}
	return nil
}
