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

func crearFichero() {
	fichero, err := os.Create("FreyFonseca117") //crear fichero con nombre del git
	if err != nil {
		log.Fatal("No se pudo crear el archivo: %v", err) //se usa para terminar el programa
	}
	defer fichero.Close()
	fmt.Printf("El fichero con nombre %s ha sido creado éxitosamente", fichero.Name())
}

func main() {
	crearFichero()
}
