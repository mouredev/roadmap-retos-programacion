package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// Con el paquete "os" podemos manejar la apertura, el cierre, la lectura y escritura de archivos,
// así como la obtención y configuración de atributos de los mismos.

func main() {
	// filename Constante que contiene el nombre del archivo.
	const fileName = "MiguelP-Dev.txt"
	message := []byte("Miguel\n 31 Años.\n Golang.")

	// Creamos el archivo para su uso
	file, err := os.Create(fileName)
	if err != nil {
		fmt.Println("Error al crear el archivo.", fileName)
		return
	}

	// Garanticemos que el archivo se cierre enventualmente
	defer file.Close()

	// Apertura del archivo con permisos de escritura
	file, err = os.OpenFile(fileName, os.O_RDWR, 0644)
	if err != nil {
		fmt.Println("Error abriendo el archivo:", err)
		return
	}

	// Escribir contenido en el archivo
	_, writeError := file.Write(message)
	if writeError != nil {
		fmt.Println("Error al escribir en el archivo:", writeError)
		return
	}

	// Leer el archivo desde el principio
	file.Seek(0, 0)
	buffer := make([]byte, len(message))
	_, readError := file.Read(buffer)
	if readError != nil {
		fmt.Println("Error al leer el archivo:", readError)
		return
	}
	fmt.Println("Contenido del archivo:", string(buffer))

	// Eliminamos el archivo
	err = os.Remove(fileName)
	if err != nil {
		fmt.Println("error al eliminar el archivo")
		return
	}

	// Extra
	// Creamos el archivo y controlamos el posible error
	file, err = os.OpenFile(productsFile, os.O_APPEND|os.O_CREATE, 0644)
	if err != nil {
		fmt.Println("Error al crear el archivo Main():", err)
		return
	}

	err = file.Close()
	if err != nil {
		fmt.Println("Error al cerrar el archivo Main(): ", err)
	}

	var productName string
	var productQuantity string
	var productPrice string
	var option uint

	for {
		fmt.Println("Selecciona una de las opciones: ")
		fmt.Println("1. Añadir un Producto")
		fmt.Println("2. Consultar un producto")
		fmt.Println("3. Consultar lista de productos")
		fmt.Println("4. Consultar venta total por producto")
		fmt.Println("5. Consultar venta total")
		fmt.Println("6. Actualizar un producto")
		fmt.Println("7. Eliminar un producto")
		fmt.Println("8. Salir")
		fmt.Scan(&option)

		switch option {
		case 1:
			fmt.Printf("Ingresa el nombre del producto: ")
			fmt.Scan(&productName)
			fmt.Printf("Ingresa la cantidad: ")
			fmt.Scan(&productQuantity)
			fmt.Printf("Ingresa el valor: ")
			fmt.Scan(&productPrice)
			err := pro.AddingProduct(productName, productQuantity, productPrice)
			if err != nil {
				fmt.Println("Error AddingProduct(): ", err)
			}
		case 2:
			fmt.Printf("Ingresa el nombre del producto: ")
			fmt.Scan(&productName)
			err := pro.searchProduct(productName)
			if err != nil {
				fmt.Println("Error searchProduct(): ", err)
			}
		case 3:
			err := pro.listOfProducts()
			if err != nil {
				fmt.Println("Error listOfProducts(): ", err)
			}
		case 4:
			fmt.Println("Ingresa el nombre del producto: ")
			fmt.Scan(&productName)
			err := pro.totalSaleByProduct(productName)
			if err != nil {
				fmt.Println("Error totalSaleByProduct(): ", err)
			}
		case 5:
			err := pro.totalSaleAmount()
			if err != nil {
				fmt.Println("Error totalSaleAmount(): ", err)
			}
		case 6:
			fmt.Printf("Ingresa el nombre del producto: ")
			fmt.Scan(&productName)
			fmt.Printf("Ingresa la cantidad: ")
			fmt.Scan(&productQuantity)
			fmt.Printf("Ingresa el valor: ")
			fmt.Scan(&productPrice)
			err := pro.updateProduct(productName, productQuantity, productPrice)
			if err != nil {
				fmt.Println("Error updateProduct(): ", err)
			}
		case 7:
			fmt.Println("Ingresa el nombre del producto a eliminar: ")
			fmt.Scan(&productName)
			pro.deleteProduct(productName)
		case 8:
			err := os.Remove(productsFile)
			if err != nil {
				fmt.Println("Error al eliminar el archivo:", err)
				return
			}
			os.Exit(0)
		default:
			fmt.Println("Selecciona una opcion correcta\n")
		}
	}
}

var productsFile = "Productos.txt"
var tmpFile = "tmp.txt"

type products struct {
	name     string
	quantity string
	price    string
}

var pro = products{}

func (p *products) AddingProduct(name, quantity, price string) error {

	products, err := search(productsFile)
	if err != nil {
		return err
	}

	err = os.Remove(productsFile)
	if err != nil {
		return err
	}

	file, err := os.Create(productsFile)
	if err != nil {
		return err
	}
	defer file.Close()

	if len(products) > 0 {
		for _, product := range products {
			_, err = file.WriteString(product + "\n")
			if err != nil {
				return err
			}
		}
	}

	newProduct := strings.ToLower(name) + ", " + quantity + ", " + price + "\n"
	_, err = file.WriteString(newProduct)
	if err != nil {
		return err
	}

	err = file.Sync()
	if err != nil {
		return err
	}
	return nil
}

func (p *products) searchProduct(name string) error {
	products, err := search(productsFile)
	if err != nil {
		return err
	}

	for _, product := range products {
		split := strings.Split(product, ", ")
		if strings.ToLower(split[0]) == strings.ToLower(name) {
			fmt.Printf("Nombre: %s, Cantidad: %s, Valor: %s.\n", split[0], split[1], split[2])
			return nil
		}
	}
	fmt.Printf("Producto %s no encontrado.\n", strings.ToUpper(name))
	return nil
}

func (p *products) listOfProducts() error {
	products, err := search(productsFile)
	if err != nil {
		return err
	}

	for _, product := range products {
		split := strings.Split(product, ", ")
		fmt.Printf("Nombre: %s, Cantidad: %s, Valor: %s.\n", split[0], split[1], split[2])
	}
	return nil
}

func (p *products) deleteProduct(name string) error {
	products, err := search(productsFile)
	if err != nil {
		return err
	}

	var newProducts = []string{}
	for _, product := range products {
		splited := strings.Split(product, ", ")
		if strings.ToLower(splited[0]) != strings.ToLower(name) {
			newProducts = append(newProducts, splited[0]+", "+splited[1]+", "+splited[2])
		}
	}

	err = os.Remove(productsFile)
	if err != nil {
		return err
	}

	file, err := os.Create(productsFile)
	if err != nil {
		return err
	}
	defer file.Close()

	for i := 0; i <= len(newProducts)-1; i++ {
		file.WriteString(newProducts[i] + "\n")
	}
	file.Sync()

	return nil
}

func (p *products) updateProduct(name, quantity, price string) error {
	products, err := search(productsFile)
	if err != nil {
		return err
	}

	var newProducts = []string{}
	for _, product := range products {
		splited := strings.Split(product, ", ")
		if strings.ToLower(splited[0]) != strings.ToLower(name) {
			newProducts = append(newProducts, splited[0]+", "+splited[1]+", "+splited[2])
		} else if strings.ToLower(splited[0]) == strings.ToLower(name) {
			newProducts = append(newProducts, name+", "+quantity+", "+price)
		}
	}

	err = os.Remove(productsFile)
	if err != nil {
		return err
	}

	file, err := os.Create(productsFile)
	if err != nil {
		return err
	}
	defer file.Close()

	for i := 0; i <= len(newProducts)-1; i++ {
		file.WriteString(newProducts[i] + "\n")
	}
	file.Sync()

	return nil
}

func (p *products) totalSaleAmount() error {
	products, err := search(productsFile)
	if err != nil {
		return err
	}
	amounts := []string{}
	quantity := 0
	for _, product := range products {
		split := strings.Split(product, ", ")
		amounts = append(amounts, split[2])
		number, _ := strconv.Atoi(split[1])
		quantity += number
	}

	var total float64
	for i := 0; i <= len(amounts)-1; i++ {
		conversion, err := strconv.ParseFloat(amounts[i], 64)
		if err != nil {
			return err
		}
		total += conversion * float64(quantity)
	}
	fmt.Printf("Total vendido: %v\n", total)
	return nil
}

func (p *products) totalSaleByProduct(productName string) error {
	products, err := search(productsFile)
	if err != nil {
		return err
	}

	var total float64
	for _, product := range products {
		splittedProduct := strings.Split(product, ", ")

		if productName == splittedProduct[0] {

			quantity, err := strconv.Atoi(splittedProduct[1])
			if err != nil {
				return err
			}

			price, err := strconv.ParseFloat(splittedProduct[2], 64)
			if err != nil {
				return err
			}

			total = price * float64(quantity)
		}
	}

	fmt.Printf("Producto: %s, Venta total: %v\n", productName, total)
	return nil
}

func search(filename string) ([]string, error) {
	file, err := os.OpenFile(filename, os.O_RDONLY, 0644)
	if err != nil {
		return []string{}, err
	}
	defer file.Close()

	var products = []string{}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		products = append(products, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		return []string{}, err
	}

	return products, nil
}
