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

package main

import (
	"fmt"
	"log"
	"os"
)

// constantes para usar
const fichero string = "FreyFonseca117.txt"

type Usuario struct {
	nombre   string
	edad     int
	lenguaje string
}

func crearFichero() {
	file, err := os.Create(fichero) //crear fichero con nombre del git
	if err != nil {
		log.Fatalf("No se pudo crear el archivo: %v", err) //se usa para terminar el programa
	}
	defer file.Close()
	fmt.Printf("El fichero con nombre %s ha sido creado exitosamente\n", file.Name()) // Salto de línea agregado
}

func agregarDatos(u Usuario) {
	file, err := os.OpenFile(fichero, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0600) // Se usa para abrir el fichero o crearlo en caso que no exista y darle los permisos
	if err != nil {
		log.Fatalf("No se pudo agregar los datos al fichero: %v", err) // Mejor manejo de errores
	}
	defer file.Close()

	// Escribir los datos en el archivo
	datos := fmt.Sprintf("nombre:%s\nedad:%d\nlenguaje:%s\n", u.nombre, u.edad, u.lenguaje)
	_, err = file.WriteString(datos)
	if err != nil {
		log.Fatalf("No se pudieron escribir los datos en el archivo: %v", err) // Mejor manejo de errores
	}
	fmt.Println("Los datos se han agregado correctamente\n") // Salto de línea agregado
}

// imprimir el contenido
func imprimir() {
	file, err := os.ReadFile(fichero)
	if err != nil {
		log.Fatal("no se puedre abrir el fichero\n")
	}
	fmt.Println(string(file))
}

// Borrar el archivo
func borrar() {
	err := os.Remove(fichero)
	if err != nil {
		log.Fatal("No se ha podido borrar el fichero")
	}
	fmt.Println("se ha borrado el archivo con éxito")
}

// Actividad adicional
const ventas string = "ventas.txt"

// estructura de productos para agregar.
type producto struct {
	nombreProducto  string
	cantidadVendida int
	precio          float64
}

func menu() {
	fmt.Println("==== REGISTRO DE VENTAS =====")
	fmt.Println("==== POR FAVOR SELECCIONE UNA OPCION =====")
	fmt.Println("==== 1 PARA CONSULTAR PRODUCTO =====")
	fmt.Println("==== 2 PARA AÑADIR PRODUCTO =====")
	fmt.Println("==== 3 PARA ACTUALIZAR PRODUCTO =====")
	fmt.Println("==== 4 PARA ELIMINAR PRODUCTO =====")
	fmt.Println("==== 5 PARA SALIR =====")

}

func main() {
	crearFichero()
	u := Usuario{
		nombre:   "Jeffrey",
		edad:     34,
		lenguaje: "GO",
	}
	agregarDatos(u)
	imprimir()
	borrar()
}
