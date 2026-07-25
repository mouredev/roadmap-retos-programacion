// https://go.dev/

//Este es mi primer comentario n_n

/*

	Esto también es un comentario
	             owo
		     
	Formas de declarar variables:	     
		     
*/


package main

import "fmt"

func main(){
	
	var Saludo string = "Qué onda"	// Primer forma
	Saludo = "Hola a todos y todas" // Reasignación
	
	
	
	var Presentacion, MiNombre, MiPais = "Me presento", "Soy Carlos Munguía", "De México" // Segunda forma declaración múltiple (infiere el tipo)
	 
	
	
	MiNivel := "Mi nivel de sensualidad es: " // Tercera forma corta (infiere el tipo) y mi favorita jeje
	

		
	var NivelDeSensualidad int // Cuarta forma con Zero Values
	
	
	
	const SignoZodiacal = "Y mi signo zodíacal siempre será Tauro (Los #1 claro que sí)"
	
	
	
/*

	Tipos de Datos primitivos y última manera para 	declarar variables:	     
		     
*/

	var (
		//booleano
		SoyGuapo bool = true
		
		
		
		//Uint no tiene números negativos
		De0a255 uint8 = 255
		De0a65634 uint16 = 6563
		De0a4294967295 uint32 = 4294967295
		De0aMuchomas uint64 = 18446744073709551615
		
		
		
		//int puede tener negativos
		Menos128a127 int8 = -128
		Menos32768a32767 int16 = -32768
		Menos2147483648 int32 = -2147483648
		Menos9223372036854775808 int64 = -9223372036854775808
		
		
		//float nùmeros con decimales
		
		ConDecimal float32 = 12.121212
		ConDecimalLargo float64 = 21.2121212121212121
		MasPotencia complex64 = 24.24242424
		MasPotenciaAun complex128 = 42.424242424242424242424242
		
		Texto = "A continuaciòn en consola podràn ver algunos ejemplos de variables en Golang: "
		
	)
	
	
	
	fmt.Println(Saludo)
	fmt.Println(Presentacion)
	fmt.Println(MiNombre)
	fmt.Println(MiPais)
	fmt.Println(MiNivel)
	fmt.Println(NivelDeSensualidad)
	fmt.Println(SignoZodiacal)
	
	fmt.Println(Texto)
	
	fmt.Println(SoyGuapo)
	
	fmt.Println(De0a255)
	fmt.Println(De0a65634)
	fmt.Println(De0a4294967295)
	fmt.Println(De0aMuchomas)
	
	fmt.Println(Menos128a127)
	fmt.Println(Menos32768a32767)
	fmt.Println(Menos2147483648)
	fmt.Println(Menos9223372036854775808)
	
	fmt.Println(ConDecimal)
	fmt.Println(ConDecimalLargo)
	fmt.Println(MasPotencia)
	fmt.Println(MasPotenciaAun)
	
	
	
	
	
	
	
	
	
	
	
	
}		     
