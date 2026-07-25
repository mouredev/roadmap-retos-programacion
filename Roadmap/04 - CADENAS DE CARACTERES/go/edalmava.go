package main

import (
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
	// Concatenación de cadenas
	cadena1 := "Hola,"
	cadena2 := " mundo"
	resultado := cadena1 + cadena2 // Resultado: "Hola, mundo"
	fmt.Println("Cadena original: ", resultado)

	// El acceso a los caracteres de una cadena se realiza mediante índices
	cadena := "Golang"
	primerCaracter := cadena[0] // 'G'
	fmt.Println("Primer caracter de Golang: ", string(primerCaracter))

	// Iterar sobre una cadena con caracteres UTF-8
	for i, c := range resultado {
		fmt.Printf("Índice: %d, Carácter: %c\n", i, c)
	}

	// Extraer partes de una cadena utilizando un rango de índices
	subcadena := resultado[0:4] // "Hola"
	fmt.Println("Extraer una subcadena: ", subcadena)

	// Longitud de una cadena en bytes
	longitud := len(resultado) // 11
	fmt.Println("Longitud de la cadena: ", longitud)

	// Verificar si una cadena esta vacía
	cadenaVacia := ""
	estaVacia := len(cadenaVacia) == 0 // true
	if estaVacia {
		fmt.Println("La cadena esta vacía")
	}

	// Verificar si una cadena contiene una subcadena
	contiene := strings.Contains(resultado, "mundo")
	fmt.Println("La cadena contiene la palabra mundo: ", contiene)

	// Encontrar el índice de la primera aparición de una subcadena dentro de otra
	indice := strings.Index(resultado, "mundo") // 6
	fmt.Println("Índice de la primera aparición de mundo: ", indice)

	// Para comparar cadenas ignorando diferencias de mayúsculas y minúsculas
	igual := strings.EqualFold("GoLang", "golang") // true
	fmt.Println("Las cadenas son iguales: ", igual)

	// Dividir una cadena en un slice de subcadenas, utilizando un delimitador especificado.
	partes := strings.Split(resultado, ", ") // []string{"Hola", "mundo"}
	fmt.Println(partes[0], partes[1])

	// Para unir un slice de cadenas en una sola cadena con un delimitador.
	unido := strings.Join(partes, ", ") // "Hola, mundo"
	fmt.Println(unido)

	// Covertir a minúsculas y mayúsculas
	minusculas := strings.ToLower(cadena) // "hola, mundo"
	mayusculas := strings.ToUpper(cadena) // "HOLA, MUNDO"
	fmt.Println("Cadena en minúscula: ", minusculas)
	fmt.Println("Cadena en mayúscula: ", mayusculas)

	// Eliminar espacios al principio y al final de la cadena
	cadenaConEspacios := "   Hola, mundo   "
	cadenaLimpia := strings.TrimSpace(cadenaConEspacios) // "Hola, mundo"
	fmt.Println("Cadena sin espacios al principio y al final: ", cadenaLimpia)

	// Reemplazar partes de una cadena
	reemplazada := strings.Replace(resultado, "mundo", "Go", 1) // "Hola, Go"
	fmt.Println("Cadena Reemplazada: ", reemplazada)

	// Repetir una cadena un número n de veces
	repetir := strings.Repeat("*", 10)
	fmt.Println(repetir)

	// Salidas formateadas
	nombre := "Edalmava"
	edad := 30
	/*
		    %s - cadena de texto
			%d - entero decimal
			%f - coma flotante
	*/
	fmt.Printf("Nombre: %s, Edad: %d\n", nombre, edad)

	// Devolver una cadena formateada
	cadenaFormateada := fmt.Sprintf("Nombre: %s, Edad: %d\n", nombre, edad)
	fmt.Println(cadenaFormateada)

	// Enviar salida formateada a un archivo
	archivo, err := os.Create("salida.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer archivo.Close()
	fmt.Fprintf(archivo, "Nombre: %s, Edad: %d\n", nombre, edad)
}
