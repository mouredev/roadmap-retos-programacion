package main

import (
	"bufio"
	"errors"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Product struct {
	amount int
	name   string
	price  float32
}

type TotalSales struct {
	amount int
	price  float32
}

/* -------------------------------------------------------------------------- */
/*                             SALES FILE (CLASS)                             */
/* -------------------------------------------------------------------------- */

type SalesFile struct {
	__amountOfProducts int
	__isDeleted        bool
	__path             string
}

func NewSalesFile(path string, initialProducts []Product) (*SalesFile, error) {
	_, statErr := os.Stat(path)
	if statErr == nil {
		removeErr := os.Remove(path)
		if removeErr != nil {
			return nil, removeErr
		}
	}

	file, createErr := os.Create(path)
	if createErr != nil {
		return nil, createErr
	}

	closeErr := file.Close()
	if closeErr != nil {
		return nil, closeErr
	}

	var salesFile SalesFile = SalesFile{
		__amountOfProducts: 0,
		__isDeleted:        false,
		__path:             path,
	}

	if len(initialProducts) > 0 {
		salesFile.appendProducts(initialProducts)
	}

	return &salesFile, nil
}

func (salesFile *SalesFile) getProduct(productName string) (Product, error) {
	var productFound Product

	if salesFile.__isDeleted {
		return productFound, errors.New("The file was deleted! Invalid operation")
	}

	products, productsErr := salesFile.getProducts()
	if productsErr != nil {
		return productFound, nil
	}

	for i := 0; i < len(products); i++ {
		var product Product = products[i]
		if strings.ToUpper(product.name) == strings.ToUpper(productName) {
			productFound.amount = product.amount
			productFound.name = product.name
			productFound.price = product.price
			break
		}
	}

	return productFound, nil
}

func (salesFile *SalesFile) getProducts() ([]Product, error) {
	var products []Product = []Product{}

	if salesFile.__isDeleted {
		return products, errors.New("The file was deleted! Invalid operation")
	}

	content, readErr := os.ReadFile(salesFile.__path)
	if readErr != nil {
		return products, readErr
	}

	productArr := strings.Split(string(content), "\n")

	for i := 0; i < len(productArr); i++ {
		var productInfo []string = strings.Split(productArr[i], ", ")

		productAmount, atoiErr := strconv.Atoi(productInfo[1])
		if atoiErr != nil {
			return products, atoiErr
		}

		productPrice, parseFloatErr := strconv.ParseFloat(productInfo[2], 32)
		if parseFloatErr != nil {
			return products, parseFloatErr
		}

		products = append(products, Product{
			name:   productInfo[0],
			amount: productAmount,
			price:  float32(productPrice),
		})
	}

	return products, nil
}

func (salesFile *SalesFile) getTotalSales() (TotalSales, error) {
	var totalSales TotalSales

	if salesFile.__isDeleted {
		return totalSales, errors.New("The file was deleted! Invalid operation")
	}

	products, productsErr := salesFile.getProducts()
	if productsErr != nil {
		return totalSales, productsErr
	}

	for i := 0; i < len(products); i++ {
		var product Product = products[i]
		totalSales.amount += product.amount
		totalSales.price += float32(product.amount) * product.price
	}

	return totalSales, nil
}

func (salesFile *SalesFile) getProductTotalSales(productName string) (TotalSales, error) {
	var totalSales TotalSales

	if salesFile.__isDeleted {
		return totalSales, errors.New("The file was deleted! Invalid operation")
	}

	products, productsErr := salesFile.getProducts()
	if productsErr != nil {
		return totalSales, productsErr
	}

	for i := 0; i < len(products); i++ {
		var product Product = products[i]
		if strings.ToUpper(product.name) == strings.ToUpper(productName) {
			totalSales.amount += product.amount
			totalSales.price += float32(product.amount) * product.price
		}
	}

	return totalSales, nil
}

func (salesFile *SalesFile) appendProducts(products []Product) error {
	if salesFile.__isDeleted {
		return errors.New("The file was deleted! Invalid operation")
	}

	file, openErr := os.OpenFile(salesFile.__path, os.O_APPEND, os.ModeAppend)
	if openErr != nil {
		return openErr
	}

	var lineBreak string = ""
	if salesFile.__amountOfProducts > 0 {
		lineBreak = "\n"
	}

	var firstProduct Product = products[0]
	var firstProductStr string = fmt.Sprintf("%s%s, %d, %.2f", lineBreak, firstProduct.name, firstProduct.amount, firstProduct.price)

	_, writeErr := file.WriteString(firstProductStr)
	if writeErr != nil {
		return writeErr
	}

	salesFile.__amountOfProducts++

	for i := 1; i < len(products); i++ {
		var product Product = products[i]
		var productStr string = fmt.Sprintf("\n%s, %d, %.2f", product.name, product.amount, product.price)

		_, writeErr := file.WriteString(productStr)
		if writeErr != nil {
			return writeErr
		}

		salesFile.__amountOfProducts++
	}

	closeErr := file.Close()
	if closeErr != nil {
		return closeErr
	}

	return nil
}

func (salesFile SalesFile) deleteFile() error {
	if salesFile.__isDeleted {
		return errors.New("The file was deleted! Invalid operation")
	}

	removeErr := os.Remove(salesFile.__path)
	if removeErr != nil {
		log.Fatal(removeErr)
	}

	return nil
}

func (salesFile *SalesFile) deleteProduct(productName string) error {
	if salesFile.__isDeleted {
		return errors.New("The file was deleted! Invalid operation")
	}

	products, productsErr := salesFile.getProducts()
	if productsErr != nil {
		return productsErr
	}

	var sanitizedProducts []Product

	for i := 0; i < len(products); i++ {
		var product Product = products[i]
		if strings.ToUpper(product.name) != strings.ToUpper(productName) {
			sanitizedProducts = append(sanitizedProducts, product)
		}
	}

	nSalesFile, nSalesFileErr := NewSalesFile(salesFile.__path, sanitizedProducts)
	if nSalesFileErr != nil {
		return nSalesFileErr
	}

	salesFile = nSalesFile

	return nil
}

func (salesFile *SalesFile) updateProduct(productName string, newAmount int, newPrice float32) error {
	if salesFile.__isDeleted {
		return errors.New("The file was deleted! Invalid operation")
	}

	products, productsErr := salesFile.getProducts()
	if productsErr != nil {
		return productsErr
	}

	for i := 0; i < len(products); i++ {
		var product *Product = &products[i]
		if strings.ToUpper(product.name) == strings.ToUpper(productName) {
			if newAmount > 0 {
				product.amount = newAmount
			}

			if newPrice > 0 {
				product.price = newPrice
			}

		}
	}

	nSalesFile, nSalesFileErr := NewSalesFile(salesFile.__path, products)
	if nSalesFileErr != nil {
		return nSalesFileErr
	}

	salesFile = nSalesFile

	return nil
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

func main() {
	/*
		Files...
	*/

	fmt.Println("Files...")

	const filePath string = "hozlucas28.txt"

	if _, statErr := os.Stat(filePath); statErr == nil {
		removeErr := os.Remove(filePath)
		if removeErr != nil {
			log.Fatal(removeErr)
		}
	}

	file, fileErr := os.Create(filePath)
	if fileErr != nil {
		log.Fatal(fileErr)
	}

	const newContent string = "Lucas Hoz\n22\nGo"
	_, writeErr := file.WriteString(newContent)
	if writeErr != nil {
		log.Fatal(writeErr)
	}

	file.Close()

	readContent, readErr := os.ReadFile(filePath)
	if readErr != nil {
		log.Fatal(readErr)
	}

	fmt.Printf("\n%s\n", string(readContent))

	if _, statErr := os.Stat(filePath); statErr == nil {
		removeErr := os.Remove(filePath)
		if removeErr != nil {
			log.Fatal(removeErr)
		}
	}

	/*
		Additional challenge...
	*/

	fmt.Println("\n# ---------------------------------------------------------------------------------- #\n")

	fmt.Println("Additional challenge...")

	const salesFilePath string = "sales.txt"

	salesFile, salesFileErr := NewSalesFile(salesFilePath, []Product{
		{
			amount: 100,
			name:   "Apple",
			price:  199.99,
		},
	})
	if salesFileErr != nil {
		log.Fatal(salesFileErr)
	}

	var shouldExit bool
	reader := bufio.NewReader(os.Stdin)

	for !shouldExit {
		fmt.Print("\nSelect an operation (Add, Delete, Get, Get total sales, Get total sales of a product, Print, Update, or Exit): ")
		operation, readErr := reader.ReadString('\n')
		if readErr != nil {
			operation = ""
		}

		var operationFmt string = strings.ToUpper(strings.TrimSpace(operation))

	operationActions:
		switch operationFmt {
		case "ADD":
			var newProduct Product

			fmt.Print("\nProduct name: ")
			_, nameErr := fmt.Scanf("%s\n", &newProduct.name)
			if nameErr != nil {
				fmt.Println("\nInvalid name!")
				break operationActions
			}

			fmt.Print("Product amount: ")
			_, amounErr := fmt.Scanf("%d\n", &newProduct.amount)
			if amounErr != nil {
				fmt.Println("\nInvalid amount!")
				break operationActions
			}

			fmt.Print("Product price: ")
			_, priceErr := fmt.Scanf("%f\n", &newProduct.price)
			if priceErr != nil {
				fmt.Print("\nInvalid price!")
				break operationActions
			}

			appendErr := salesFile.appendProducts([]Product{newProduct})
			if appendErr != nil {
				log.Fatal(appendErr)
			}

		case "DELETE":
			var product Product

			fmt.Print("\nProduct name: ")
			_, nameErr := fmt.Scanf("%s\n", &product.name)
			if nameErr != nil {
				fmt.Println("\nInvalid name!")
				break operationActions
			}

			deleteErr := salesFile.deleteProduct(product.name)
			if deleteErr != nil {
				log.Fatal(deleteErr)
			}

		case "GET":
			var productName string

			fmt.Print("\nProduct name: ")
			_, nameErr := fmt.Scanf("%s\n", &productName)
			if nameErr != nil {
				fmt.Println("\nInvalid name!")
				break operationActions
			}

			product, productErr := salesFile.getProduct(productName)
			if productErr != nil {
				log.Fatal(productErr)
			}

			fmt.Printf("\nName: %s\nAmount: %d\nPrice: $%.2f\n", product.name, product.amount, product.price)

		case "GET TOTAL SALES":
			totalSales, totalSalesErr := salesFile.getTotalSales()
			if totalSalesErr != nil {
				log.Fatal(totalSalesErr)
			}

			fmt.Printf("\nAmount: %d\nTotal: $%.2f\n", totalSales.amount, totalSales.price)

		case "GET TOTAL SALES OF A PRODUCT":
			var productName string

			fmt.Print("\nProduct name: ")
			_, nameErr := fmt.Scanf("%s\n", &productName)
			if nameErr != nil {
				fmt.Println("\nInvalid name!")
				break operationActions
			}

			totalSales, totalSalesErr := salesFile.getProductTotalSales(productName)
			if totalSalesErr != nil {
				log.Fatal(totalSalesErr)
			}

			fmt.Printf("\nAmount: %d\nTotal: $%.2f\n", totalSales.amount, totalSales.price)

		case "PRINT":
			products, productsErr := salesFile.getProducts()
			if productsErr != nil {
				log.Fatal(productsErr)
			}

			for i := 0; i < len(products); i++ {
				var product Product = products[i]
				fmt.Printf("\nName: %s\nAmount: %d\nPrice: $%.2f\n", product.name, product.amount, product.price)
			}

		case "UPDATE":
			var product Product

			fmt.Print("\nProduct name: ")
			_, nameErr := fmt.Scanf("%s\n", &product.name)
			if nameErr != nil {
				fmt.Println("\nInvalid name!")
				break operationActions
			}

			fmt.Print("New amount (optional): ")
			fmt.Scanf("%d\n", &product.amount)

			fmt.Print("New price (optional): ")
			fmt.Scanf("%f\n", &product.price)

			updateErr := salesFile.updateProduct(product.name, product.amount, product.price)
			if updateErr != nil {
				log.Fatal(updateErr)
			}

		case "EXIT":
			deleteErr := salesFile.deleteFile()
			shouldExit = true

			if deleteErr != nil {
				log.Fatal(deleteErr)
			}

		default:
			fmt.Println("\nInvalid operation! Try again...")
		}
	}
}
