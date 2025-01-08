package main

import (
	"fmt"
	"sort"
	"strings"
)

func main() {
	// Operaciones básicas sobre cadenas de texto
	texto := "Hola, mundo!"

	// Interpolación de cadenas (uso de plantillas de cadena)
	nombre := "Migue"
	lenguaje := "PHP"
	mensaje := fmt.Sprintf("Hola, me llamo %s y trabajo con %s años.", nombre, lenguaje)
	fmt.Println(mensaje)

	// Longitud de la cadena
	longitud := len(texto)
	fmt.Printf("La longitud de la cadena %s es %d caracteres\n", texto, longitud)

	// Obtener el carácter en una posición específica
	primerCaracter := string(texto[0])
	fmt.Printf("El primer carácter de %s es %s\n", texto, primerCaracter)

	// Concatenar dos cadenas
	nuevaCadena := texto + " Go"
	fmt.Printf("La nueva cadena de unir %s con Go es %s\n", texto, nuevaCadena)

	// Convertir la cadena a minúsculas
	minusculas := strings.ToLower(texto)
	fmt.Printf("%s en minúsculas es %s\n", texto, minusculas)

	// Convertir la cadena a mayúsculas
	mayusculas := strings.ToUpper(texto)
	fmt.Printf("%s en mayúsculas es %s\n", texto, mayusculas)

	// Obtener una subcadena
	subcadena := texto[0:4]
	fmt.Printf("La subcadena de %s entre las posiciones 0 y 4 es %s\n", texto, subcadena)

	// Reemplazar parte de la cadena
	reemplazada := strings.Replace(texto, "Hola", "Saludos", 1)
	fmt.Printf("Vamos a reemplazar Hola por Saludos: %s\n", reemplazada)

	// Operaciones adicionales sobre cadenas de texto
	textoConEspacios := "   Hola,      mundo!   "

	// Eliminar espacios en blanco al principio y al final
	sinEspaciosExtremos := strings.TrimSpace(textoConEspacios)
	fmt.Printf("Cadena sin espacios al principio y al final: %s\n", sinEspaciosExtremos)

	// Eliminar todos los espacios en blanco
	sinEspacios := strings.ReplaceAll(textoConEspacios, " ", "")
	fmt.Printf("Cadena sin espacios: %s\n", sinEspacios)

	// Unión de dos cadenas
	cadena1 := "Moure"
	cadena2 := "Dev"
	unionCadenas := fmt.Sprintf("%s %s", cadena1, cadena2)
	fmt.Printf("La unión de las cadenas %s y %s es %s\n", cadena1, cadena2, unionCadenas)

	// Intersección de dos cadenas (caracteres comunes)
	interseccionCadenas := interseccionDeCadenas(cadena1, cadena2)
	fmt.Printf("Intersección de las cadenas %s y %s es %s\n", cadena1, cadena2, interseccionCadenas)

	// Acceso a caracteres específicos (por posición)
	tercerCaracter := string(texto[2])
	fmt.Printf("El tercer carácter de %s es %s\n", texto, tercerCaracter)

	// Repetición de una cadena
	cadenaRepetida := strings.Repeat("Hola ", 3)
	fmt.Printf("Cadena Hola repetida 3 veces queda %s\n", cadenaRepetida)

	// Recorrido de una cadena (usando un bucle)
	for i, char := range texto {
		fmt.Printf("Carácter en posición %d: %c\n", i, char)
	}

	// Conversión a título (primera letra en mayúscula)
	titulo := strings.Title(strings.ToLower(texto))
	fmt.Printf("La cadena %s como título %s\n", texto, titulo)

	// División de una cadena en un array de substrings
	palabras := strings.Fields(texto)
	fmt.Printf("Palabras en la cadena %s son %v\n", texto, palabras)

	// Verificación de si una cadena comienza o termina con ciertos caracteres
	comienzaCon := strings.HasPrefix(texto, "Hola")
	fmt.Printf("¿La cadena %s comienza con 'Hola'? %t\n", texto, comienzaCon)

	terminaCon := strings.HasSuffix(texto, "mundo!")
	fmt.Printf("¿La cadena %s termina con 'mundo!'? %t\n", texto, terminaCon)

	// Verificar si una cadena es palíndromo
	fmt.Printf("¿Es '%s' un palíndromo? %t\n", texto, esPalindromo(texto))
	fmt.Printf("¿Es 'Ana' un palíndromo? %t\n", esPalindromo("Ana"))

	// Verificar si una cadena es un anagrama
	fmt.Printf("¿Es 'listen' un anagrama de 'silent'? %t\n", esAnagrama("listen", "silent"))

	// Verificar si una cadena es un isograma
	fmt.Printf("¿Es 'programming' un isograma? %t\n", esIsograma("programming"))
}

// Función para la intersección de dos cadenas (caracteres comunes)
func interseccionDeCadenas(cadena1, cadena2 string) string {
	set1 := make(map[rune]struct{})
	set2 := make(map[rune]struct{})

	for _, char := range cadena1 {
		set1[char] = struct{}{}
	}

	for _, char := range cadena2 {
		set2[char] = struct{}{}
	}

	var interseccion []rune
	for char := range set1 {
		if _, exists := set2[char]; exists {
			interseccion = append(interseccion, char)
		}
	}

	sort.Slice(interseccion, func(i, j int) bool {
		return interseccion[i] < interseccion[j]
	})

	return string(interseccion)
}

// Función para verificar si una cadena es palíndromo
func esPalindromo(cadena string) bool {
	sinEspacios := strings.Join(strings.Fields(cadena), "")
	invertida := invertirCadena(sinEspacios)
	return strings.ToLower(sinEspacios) == strings.ToLower(invertida)
}

// Función para invertir una cadena
func invertirCadena(cadena string) string {
	runes := []rune(cadena)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

// Función para verificar si una cadena es un anagrama
func esAnagrama(cadena1, cadena2 string) bool {
	limpiaCadena := func(cadena string) string {
		return strings.Join(strings.Fields(cadena), "")
	}

	limpiaCadena1 := limpiaCadena(cadena1)
	limpiaCadena2 := limpiaCadena(cadena2)

	return ordenarCadena(limpiaCadena1) == ordenarCadena(limpiaCadena2)
}

// Función para ordenar una cadena
func ordenarCadena(cadena string) string {
	runes := []rune(cadena)
	sort.Sort(sortRunes(runes))
	return string(runes)
}

// Tipo de datos para ordenar los runes
type sortRunes []rune

func (s sortRunes) Len() int           { return len(s) }
func (s sortRunes) Less(i, j int) bool { return s[i] < s[j] }
func (s sortRunes) Swap(i, j int)      { s[i], s[j] = s[j], s[i] }

// Función para verificar si una cadena es un isograma
func esIsograma(cadena string) bool {
	caracteres := make(map[rune]struct{})

	for _, char := range cadena {
		if _, exists := caracteres[char]; exists {
			return false
		}
		caracteres[char] = struct{}{}
	}

	return true
}
