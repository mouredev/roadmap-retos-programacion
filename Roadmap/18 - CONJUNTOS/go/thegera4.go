package main

import "fmt"

type Conjunto struct {
	elementos []string
}

func (c *Conjunto) añadirElementoFinal(elemento string) {
	c.elementos = append(c.elementos, elemento)
}

func (c *Conjunto) añadirElementoInicio(elemento string) {
	c.elementos = append([]string{elemento}, c.elementos...)
}

func (c *Conjunto) añadirVariosElementosFinal(elementos ...string) { //...string indica que se pueden pasar un numero variable de "elementos"
	c.elementos = append(c.elementos, elementos...)
}

func (c *Conjunto) añadirVariosElementosPosicion(posicion int, elementos ...string) {
	//c.elementos[:posicion] -> elementos desde el inicio hasta la "posicion", excluyendo la "posicion"
	c.elementos = append(c.elementos[:posicion], append(elementos, c.elementos[posicion:]...)...)
	//append(elementos, c.elementos[posicion:]...) -> añade los "elementos" al final de "c.elementos" desde la "posicion"
}

func (c *Conjunto) eliminarElementoPosicion(posicion int) {
	c.elementos = append(c.elementos[:posicion], c.elementos[posicion+1:]...)
}

func (c *Conjunto) actualizarElementoPosicion(posicion int, elemento string) {
	c.elementos[posicion] = elemento
}

func (c *Conjunto) comprobarElemento(elemento string) bool {
	for _, e := range c.elementos {
		if e == elemento {
			return true
		}
	}
	return false
}

func (c *Conjunto) eliminarContenido() {
	c.elementos = []string{}
}

func main() {
	conjunto := Conjunto{}

	conjunto.añadirElementoFinal("naranja")
	fmt.Println(conjunto.elementos)

	conjunto.añadirElementoInicio("manzana")
	fmt.Println(conjunto.elementos)

	conjunto.añadirVariosElementosFinal("pera", "kiwi", "melon")
	fmt.Println(conjunto.elementos)

	conjunto.añadirVariosElementosPosicion(2, "sandia", "uva", "mango")
	fmt.Println(conjunto.elementos)

	conjunto.eliminarElementoPosicion(3)
	fmt.Println(conjunto.elementos)

	conjunto.actualizarElementoPosicion(2, "fresa")
	fmt.Println(conjunto.elementos)

	fmt.Println(conjunto.comprobarElemento("fresa"))
	fmt.Println(conjunto.comprobarElemento("platano"))

	conjunto.eliminarContenido()
	fmt.Println(conjunto.elementos)

	//Extra:

	//Unión
	conjunto1 := Conjunto{}
	conjunto1.añadirVariosElementosFinal("naranja", "manzana")
	conjunto2 := Conjunto{}
	conjunto2.añadirVariosElementosFinal("pera", "uva")
	conjunto1.union(conjunto2)
	fmt.Println("Union: ", conjunto1.elementos)

	//Intersección
	conjunto3 := Conjunto{}
	conjunto3.añadirVariosElementosFinal("naranja", "manzana", "pera")
	conjunto4 := Conjunto{}
	conjunto4.añadirVariosElementosFinal("pera", "uva")
	conjunto3.interseccion(conjunto4)
	fmt.Println("Interseccion: ", conjunto3.elementos)

	//Diferencia
	conjunto5 := Conjunto{}
	conjunto5.añadirVariosElementosFinal("naranja", "manzana", "pera")
	conjunto6 := Conjunto{}
	conjunto6.añadirVariosElementosFinal("pera", "uva")
	conjunto5.diferencia(conjunto6)
	fmt.Println("Diferencia: ", conjunto5.elementos)

	//Diferencia simétrica
	conjunto7 := Conjunto{}
	conjunto7.añadirVariosElementosFinal("naranja", "manzana", "pera")
	conjunto8 := Conjunto{}
	conjunto8.añadirVariosElementosFinal("pera", "uva")
	conjunto7.diferenciaSimetrica(conjunto8)
	fmt.Println("Diferencia simetrica: ", conjunto7.elementos)

}

//Extra:

//Unión
func (c *Conjunto) union(c2 Conjunto) {
	for _, e := range c2.elementos {
		if !c.comprobarElemento(e) {
			c.añadirElementoFinal(e)
		}
	}
}

//Intersección
func (c *Conjunto) interseccion(c2 Conjunto) {
	for i := 0; i < len(c.elementos); i++ {
		if !c2.comprobarElemento(c.elementos[i]) {
			c.eliminarElementoPosicion(i)
			i--
		}
	}
}

//Diferencia
func (c *Conjunto) diferencia(c2 Conjunto) {
	for i := 0; i < len(c.elementos); i++ {
		if c2.comprobarElemento(c.elementos[i]) {
			c.eliminarElementoPosicion(i)
			i--
		}
	}
}

//Diferencia simétrica
func (c *Conjunto) diferenciaSimetrica(c2 Conjunto) {
	// crear conjuntos temporales/auxiliares
	temp1 := make(map[string]bool)
	temp2 := make(map[string]bool)

	// almacenar los elementos unicos del primer conjunto
	for _, e := range c.elementos {
		temp1[e] = true
	}

	// almacenar los elementos unicos del segundo conjunto
	for _, e := range c2.elementos {
		temp2[e] = true
	}

	// crear un nuevo conjunto para almacenar la diferencia simetrica
	diff := Conjunto{}

	// agregar elementos que estan en c pero no en c2
	for e := range temp1 {
		if !temp2[e] {
			diff.añadirElementoFinal(e)
		}
	}

	// agregar elementos que estan en c2 pero no en c
	for e := range temp2 {
		if !temp1[e] {
			diff.añadirElementoFinal(e)
		}
	}

	// actualizar el conjunto original con la diferencia simetrica
	*c = diff
}