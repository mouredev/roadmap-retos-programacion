//Pagina oficial del lenguaje: https://go.dev/

//comentario en linea

/*
comentario en varias lineas
*/

//declaración del paquete principal para que funcione go
package main
//importar paquete fmt para impresiones por consola
import "fmt"


//Crea una variable (y una constante si el lenguaje lo soporta).
var miVariable int
const miConstate  = "Stiware"


/*
la forma para definir varibles más llamativa en go es con := 
pero esta solo se puede utilizar dentro de funciones así
*/
func main(){
	otraVariable := "hola"
	fmt.Println("Otra forma de definir una variable: ",otraVariable)
	fmt.Println("Tipos de datos primitivos")
	//llamada a la funcion para mostrar los tipos de datos basicos
	tiposPrimitivos()

	//llamada a la función para presentarme
	presentacion()
}


//Crea variables representando todos los tipos de datos primitivos
func tiposPrimitivos(){
	var boleano bool // valores posibles: verdadero o falso
	var textos string// cualquier cadena de texto como las que mostramos por consola
	var entero int // número enteros (es decir sin decimales), su tamaño depende de si el SO es de 32 o 64 bits
	var flotante float32 // números más grandes y con decimales, tambien esta el float64 que abarca numeros aun más grandes

	fmt.Println("Boleano",boleano)
	fmt.Println("Strings",textos)
	fmt.Println("Entero",entero)
	fmt.Println("Flotante",flotante)

}

func presentacion(){
	// El comodín %s me sirve para indicar que ahí se reemplazará un dato string que le enviaré después
	fmt.Printf("!Hola, GO. Me llamo %s!",miConstate)
}