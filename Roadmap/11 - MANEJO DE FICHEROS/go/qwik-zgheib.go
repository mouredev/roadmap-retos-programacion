package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

/* extra */
const filename = "sales.txt"

type Product struct {
	Name   string
	Amount int
	Price  float64
}

func addProduct() {
	fmt.Print("Enter product name: ")
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	name := scanner.Text()

	fmt.Print("Enter amount sold: ")
	var amount int
	fmt.Scan(&amount)

	fmt.Print("Enter price: ")
	var price float64
	fmt.Scan(&price)

	product := fmt.Sprintf("%s, %d, %.2f\n", name, amount, price)
	file, err := os.OpenFile(filename, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		fmt.Println("Error adding product:", err)
		return
	}
	defer file.Close()

	_, err = file.WriteString(product)
	if err != nil {
		fmt.Println("Error writing to file:", err)
	}
}

func viewProducts() {
	file, err := os.Open(filename)
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		fmt.Println(scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error scanning file:", err)
	}
}

func updateProduct() {
	products, err := readProducts()
	if err != nil {
		fmt.Println("Error reading products:", err)
		return
	}

	fmt.Print("Enter product name to update: ")
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	name := scanner.Text()

	for i, product := range products {
		if product.Name == name {
			fmt.Print("Enter new amount sold: ")
			var amount int
			fmt.Scan(&amount)

			fmt.Print("Enter new price: ")
			var price float64
			fmt.Scan(&price)

			products[i].Amount = amount
			products[i].Price = price

			if err := writeProducts(products); err != nil {
				fmt.Println("Error updating product:", err)
			} else {
				fmt.Println("Product updated successfully.")
			}
			return
		}
	}
	fmt.Println("Product not found.")
}

func deleteProduct() {
	products, err := readProducts()
	if err != nil {
		fmt.Println("Error reading products:", err)
		return
	}

	fmt.Print("Enter product name to delete: ")
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	name := scanner.Text()

	for i, product := range products {
		if product.Name == name {
			products = append(products[:i], products[i+1:]...)
			if err := writeProducts(products); err != nil {
				fmt.Println("Error deleting product:", err)
			} else {
				fmt.Println("Product deleted successfully.")
			}
			return
		}
	}
	fmt.Println("Product not found.")
}

func totalSales() {
	products, err := readProducts()
	if err != nil {
		fmt.Println("Error reading products:", err)
		return
	}

	var total float64
	for _, product := range products {
		total += float64(product.Amount) * product.Price
	}
	fmt.Printf("Total Sales: $%.2f\n", total)
}

func salesByProduct() {
	products, err := readProducts()
	if err != nil {
		fmt.Println("Error reading products:", err)
		return
	}

	for _, product := range products {
		total := float64(product.Amount) * product.Price
		fmt.Printf("%s: $%.2f\n", product.Name, total)
	}
}

func exitProgram() {
	err := os.Remove(filename)
	if err != nil {
		fmt.Println("Error deleting file:", err)
	} else {
		fmt.Println("File deleted successfully.")
	}
}

func readProducts() ([]Product, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var products []Product
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Split(line, ", ")
		if len(parts) != 3 {
			continue
		}

		amount, err := strconv.Atoi(parts[1])
		if err != nil {
			continue
		}

		price, err := strconv.ParseFloat(parts[2], 64)
		if err != nil {
			continue
		}

		product := Product{
			Name:   parts[0],
			Amount: amount,
			Price:  price,
		}
		products = append(products, product)
	}

	if err := scanner.Err(); err != nil {
		return nil, err
	}
	return products, nil
}

func writeProducts(products []Product) error {
	file, err := os.OpenFile(filename, os.O_TRUNC|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		return err
	}
	defer file.Close()

	for _, product := range products {
		line := fmt.Sprintf("%s, %d, %.2f\n", product.Name, product.Amount, product.Price)
		_, err := file.WriteString(line)
		if err != nil {
			return err
		}
	}
	return nil
}

func main() {
	username := "qwik-zgheib"
	filename := fmt.Sprintf("%s.txt", username)
	content := "Name: Isaias\nAge: 22\nFavorite Programming Language: Go\n"

	err := os.WriteFile(filename, []byte(content), 0644)
	if err != nil {
		fmt.Println("Error creating file:", err)
		return
	}

	data, err := os.ReadFile(filename)
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}
	fmt.Println("File Content:")
	fmt.Println(string(data))

	err = os.Remove(filename)
	if err != nil {
		fmt.Println("Error deleting file:", err)
		return
	}
	fmt.Println("File deleted successfully.")

	/* extra */
	for {
		fmt.Println("1. Add Product")
		fmt.Println("2. View Products")
		fmt.Println("3. Update Product")
		fmt.Println("4. Delete Product")
		fmt.Println("5. Total Sales")
		fmt.Println("6. Sales by Product")
		fmt.Println("7. Exit")
		fmt.Print("Choose an option: ")

		var option int
		fmt.Scan(&option)

		switch option {
		case 1:
			addProduct()
		case 2:
			viewProducts()
		case 3:
			updateProduct()
		case 4:
			deleteProduct()
		case 5:
			totalSales()
		case 6:
			salesByProduct()
		case 7:
			exitProgram()
			return
		default:
			fmt.Println("Invalid option. Please try again.")
		}
	}
}
