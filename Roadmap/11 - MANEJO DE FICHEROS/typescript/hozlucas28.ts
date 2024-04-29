import * as fs from 'node:fs'
import * as readline from 'readline-sync'

/*
    Files...
*/

console.log('Files...')

const FILE_PATH: string = 'hozlucas28.txt'

console.log(`\n// Delete file if exist
if (fs.existsSync(FILE_PATH)) fs.rmSync(FILE_PATH)

// Create file with content
const fileContent: string = ['Lucas Hoz', '22', 'TypeScript'].join('\\n')
fs.writeFileSync(FILE_PATH, fileContent, { encoding: 'utf-8' })

// Print file content
const data: string = fs.readFileSync(FILE_PATH, { encoding: 'utf-8' })
console.log(data)

// Delete file
fs.rmSync(FILE_PATH)\n`)

// Delete file if exist
if (fs.existsSync(FILE_PATH)) fs.rmSync(FILE_PATH)

// Create file with content
const fileContent: string = ['Lucas Hoz', '22', 'TypeScript'].join('\n')
fs.writeFileSync(FILE_PATH, fileContent, { encoding: 'utf-8' })

// Print file content
const data: string = fs.readFileSync(FILE_PATH, { encoding: 'utf-8' })
console.log(data)

// Delete file
fs.rmSync(FILE_PATH)

console.log(
	'\n# ---------------------------------------------------------------------------------- #\n'
)

/*
    Additional challenge...
*/

type Operation = Uppercase<
	| 'add'
	| 'delete'
	| 'print'
	| 'total sales by product'
	| 'total sales'
	| 'update'
	| 'exit'
>

type Product = {
	amount: number
	name: string
	price: number
	total: number
}

type Constructor = {
	filePath: string
	products?: Omit<Product, 'total'>[]
}

class SalesFile {
	private _fileDeleted: boolean
	private _filePath: string
	private _products: Product[]

	constructor({ products = [], filePath }: Constructor) {
		const mappedProducts: Product[] = this.mapProducts(products)

		this._fileDeleted = false
		this._filePath = filePath
		this._products = mappedProducts

		this.writeFile()
	}

	public get products(): Product[] {
		return this._products
	}

	private set products(products: Omit<Product, 'total'>[]) {
		const mappedProducts = this.mapProducts(products)
		this._products = mappedProducts
		this.writeFile()
	}

	public getProductByName(productName: string): {
		index: number
	} & Product {
		let productIndex: number = -1
		const product: undefined | Product = this._products.find(
			(product, index) => {
				if (product.name.toUpperCase() === productName.toUpperCase()) {
					productIndex = index
					return true
				}
			}
		)
		if (!product) throw new Error("Product name doesn't exist")

		return {
			amount: product.amount,
			index: productIndex,
			name: product.name,
			price: product.price,
			total: product.total,
		}
	}

	public getTotalSales(): { amount: number; total: number } {
		return this._products.reduce(
			(prev, current) => ({
				amount: prev.amount + current.amount,
				total: prev.total + current.total,
			}),
			{ amount: 0, total: 0 }
		)
	}

	private joinProducts(products: Product[]): Product[] {
		const joinedProducts: Product[] = []

		for (let i = 0; i < products.length; i++) {
			let { amount, name, price, total } = products[i]

			for (let j = i + 1; j < products.length; j++) {
				const {
					amount: nextAmount,
					name: nextName,
					price: nextPrice,
				} = products[j]
				if (name.toUpperCase() === nextName.toUpperCase()) {
					amount += nextAmount
					price = Math.max(price, nextPrice)
					total = price * amount
					products.splice(j, 1)
				}
			}
			joinedProducts.push({ amount, name, price, total })
		}

		return joinedProducts
	}

	private mapProducts(products: Omit<Product, 'total'>[]): Product[] {
		let mappedProducts: Product[] = products.map((product) => ({
			...product,
			total: product.price * product.amount,
		}))
		mappedProducts = this.joinProducts(mappedProducts)

		return mappedProducts
	}

	private parseProducts(products = this._products): string {
		return products.reduce((prevParsedProd, currentProd) => {
			const { amount, name, price } = currentProd
			const parsedProduct: string = `${name}, ${amount}, ${price}`
			return `${prevParsedProd}\n${parsedProduct}`.trim()
		}, '')
	}

	private shouldMethodFail(): never | void {
		if (this._fileDeleted)
			throw new Error(
				'The file was deleted! You should not try any method of this class instance'
			)
	}

	private writeFile(): void {
		fs.writeFileSync(this._filePath, this.parseProducts(this._products), {
			encoding: 'utf-8',
		})
	}

	public appendProducts(products: Omit<Product, 'total'>[]): this | never {
		this.shouldMethodFail()
		this.products = [...this._products, ...products]
		return this
	}

	public deleteFile(): void {
		this.shouldMethodFail()

		fs.rmSync(this._filePath)
		this._fileDeleted = true
	}

	public deleteProduct(productName: string): this | never {
		this.shouldMethodFail()

		const { index } = this.getProductByName(productName)

		this.products = [
			...this._products.slice(0, index),
			...this._products.slice(index + 1),
		]
		return this
	}

	public updateProduct({
		amount,
		name,
		price,
	}: {
		amount?: number
		name: string
		price?: number
	}): this | never {
		this.shouldMethodFail()

		const originalProduct = this.getProductByName(name)
		amount ??= originalProduct.amount
		price ??= originalProduct.price

		const updatedProduct = Object.assign<Product, Partial<Product>>(
			{
				amount: originalProduct.amount,
				name: originalProduct.name,
				price: originalProduct.price,
				total: originalProduct.total,
			},
			{
				amount,
				price,
				total: price * amount,
			}
		)

		this.products = [
			...this._products.slice(0, originalProduct.index),
			updatedProduct,
			...this._products.slice(originalProduct.index + 1),
		]
		return this
	}
}

const salesFile: SalesFile = new SalesFile({ filePath: 'sells.txt' })

let userInput: Operation

do {
	userInput = readline
		.question(
			"Write an operation ('Add', 'Delete', 'Print', 'Total sales by product', 'Total sales', 'Update', or 'Exit'): "
		)
		.toUpperCase() as Operation

	switch (userInput) {
		case 'ADD':
			const newProductName = readline.question('Product name: ')
			if (!newProductName) continue

			const newProductAmount = readline.questionInt('Product amount: ')
			const newProductPrice = readline.questionInt('Product price: ')

			salesFile.appendProducts([
				{
					name: newProductName,
					amount: newProductAmount,
					price: newProductPrice,
				},
			])
			break

		case 'DELETE':
			const productNameToDelete = readline.question('Product name to delete: ')
			if (!productNameToDelete) continue

			salesFile.deleteProduct(productNameToDelete)
			break

		case 'PRINT':
			console.table(salesFile.products)
			break

		case 'TOTAL SALES BY PRODUCT':
			const productNameToGetTotalSales = readline.question(
				'Product name to get total sales: '
			)
			if (!productNameToGetTotalSales) continue

			const product = salesFile.getProductByName(productNameToGetTotalSales)
			console.table({
				amount: product.amount,
				price: product.price,
				total: product.total,
			})
			break

		case 'TOTAL SALES':
			const { amount, total }: { amount: number; total: number } =
				salesFile.getTotalSales()
			console.table({ amount, total })
			break

		case 'UPDATE':
			const productNameToUpdate = readline.question('Product name to update: ')
			if (!productNameToUpdate) continue

			const newAmount = readline.questionInt('New amount for the product: ')
			const newPrice = readline.questionFloat('New price for the product: ')

			salesFile.updateProduct({
				amount: newAmount,
				name: productNameToUpdate,
				price: newPrice,
			})
			break

		case 'EXIT':
			salesFile.deleteFile()
			break

		default:
			console.log('Invalid operation! Try again...')
	}
} while (userInput !== 'EXIT')
