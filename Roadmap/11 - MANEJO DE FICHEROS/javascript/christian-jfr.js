//  #11 MANEJO DE FICHEROS

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
 */

// Modulos fs y readline de nodejs
const readline = require('node:readline');
const fs = require('node:fs');

let FILE_NAME = 'christian-jfr.txt';
const info = {
	name: 'Christian',
	age: '36',
	language: 'JavaScript',
};

function main() {
	createFile();
	setTimeout(() => {
		printFile();
	}, 1000);
	setTimeout(() => {
		deleteFile();
	}, 1500);
}

function createFile() {
	let content = `Name: ${info.name}.\nAge: ${info.age}\nFavorite Programming Language: ${info.language}.`;
	fs.writeFileSync(FILE_NAME, content, 'utf-8');
	console.log(`File ${FILE_NAME} successfully created`);
}

function printFile() {
	fs.readFile(FILE_NAME, 'utf-8', (err, data) => {
		if (err) {
			console.log('file Not found', err);
		} else {
			console.log(data);
		}
	});
}

function deleteFile() {
	fs.unlink(FILE_NAME, (err) => {
		if (err) {
			console.log('file Not found', err);
		} else {
			console.log(`File ${FILE_NAME} successfully deleted`);
		}
	});
}

main();

/** DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un
 * archivo .txt.
 * - Cada producto se guarda en una línea del arhivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
 */
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

const SALES_FILE_NAME = 'sales.txt';

fs.writeFileSync(SALES_FILE_NAME, '', 'utf-8');

salesMain();

function salesMain() {
	console.clear();
	console.log('Sales Management System');
	rl.question(
		'\nWhat you want to do?\n 1. Add\n 2. Consult\n 3. Update\n 4. Delete\n 5. Total sales by product\n 6. Total sales\n 7. Exit\n',
		(answer) => {
			switch (answer) {
				case '1':
					addProduct();
					break;
				case '2':
					checkProduct();
					break;
				case '3':
					updateProduct();
					break;
				case '4':
					deleteProduct();
					break;
				case '5':
					salesByProduct();
					break;
				case '6':
					totalSales();
					break;
				case '7':
					endProgram();
					break;
				case 'ALL':
					allProducts();
					break;

				default:
					console.log('\nInvalid option\n');
					setTimeout(() => {
						salesMain();
					}, 2000);
			}
		}
	);
}

function toMain() {
	rl.question('\nPress enter to continue', () => {
		salesMain();
	});
}

function endProgram() {
	fs.unlink(SALES_FILE_NAME, (err) => {
		if (err) {
			console.log(`\nFile ${SALES_FILE_NAME} Not found`, err);
		} else {
			console.log(`\nFile ${SALES_FILE_NAME} successfully deleted`);
		}
	});
	setTimeout(() => {
		rl.close();
	}, 2000);
}

function addProduct() {
	rl.question('Product Name: ', (name) => {
		rl.question('Quantity Sold: ', (quantity) => {
			rl.question('Price: ', (price) => {
				const newProduct = `\n${name}, ${quantity}, $${price}`;

				fs.appendFile(SALES_FILE_NAME, newProduct, (err) => {
					if (err) {
						console.log(err);
						toMain();
					} else {
						console.log(`\nProduct ${name} successfully added.`);
						toMain();
					}
				});
			});
		});
	});
}

function checkProduct() {
	const productsInfo = fs.readFileSync(SALES_FILE_NAME, 'utf-8');
	const productsArray = productsInfo
		.split('\n')
		.filter((product) => product !== '')
		.map((product) => product.split(', '));

	let foundProduct = null;

	rl.question('Which product do you want to consult?\n', (productName) => {
		if (productName === '') {
			console.log('Please enter a valid product name');
			toMain();
		}

		for (const product of productsArray) {
			if (product[0].includes(productName)) {
				foundProduct = product;
				break;
			}
		}

		if (!foundProduct) {
			console.log(`${productName} not found`);
		} else {
			console.log(foundProduct.join(', '));
		}
		toMain();
	});
}

function updateProduct() {
	let productsArray;

	fs.readFile(SALES_FILE_NAME, 'utf-8', (err, products) => {
		if (err) {
			console.log(err);
			return toMain();
		}

		productsArray = products
			.split('\n')
			.filter((product) => product !== '')
			.map((product) => product.split(', '));
	});

	let foundProduct = null;

	rl.question('Which product do you want to update?\n', (productName) => {
		if (productName === '') {
			console.log('Please enter a valid product name');
			toMain();
		}

		for (const product of productsArray) {
			if (product[0].includes(productName)) {
				foundProduct = product;
				break;
			}
		}

		if (!foundProduct) {
			console.log(`${productName} not found`);
			toMain();
		} else {
			rl.question(`Update ${productName} quantity: `, (newquantity) => {
				foundProduct[1] = newquantity;
				rl.question(`Update ${productName} price: `, (newprice) => {
					foundProduct[2] = `$${newprice}`;

					const productUpdated = productsArray
						.map((product) => {
							return product === foundProduct
								? foundProduct.join(', ')
								: product.join(', ');
						})
						.join('\n');

					fs.writeFile(SALES_FILE_NAME, productUpdated, (err) => {
						if (err) {
							console.log(err);
						} else {
							console.log(`\nProduct ${productName} successfully updated.`);
							toMain();
						}
					});
				});
			});
		}
	});
}

function deleteProduct() {
	const productsInfo = fs.readFileSync(SALES_FILE_NAME, 'utf-8');
	const productsArray = productsInfo
		.split('\n')
		.filter((product) => product !== '')
		.map((product) => product.split(', '));

	let foundProduct = null;

	rl.question('Which product do you want to delete?\n', (productName) => {
		if (productName === '') {
			console.log('Please enter a valid product name');
			return toMain();
		}

		for (const product of productsArray) {
			if (product[0].includes(productName)) {
				foundProduct = product;
				break;
			}
		}

		if (!foundProduct) {
			console.log(`${productName} not found`);
			toMain();
		} else {
			const filteredProducts = productsArray.filter(
				(product) => product !== foundProduct
			);

			const productString = filteredProducts.join('\n');

			fs.writeFile(SALES_FILE_NAME, productString, (err) => {
				if (err) {
					console.log(err);
				} else {
					console.log(`\nProduct ${productName} successfully deleted.`);
					toMain();
				}
			});
		}
	});
}

function salesByProduct() {
	const productsInfo = fs.readFileSync(SALES_FILE_NAME, 'utf-8');
	const productsArray = productsInfo
		.split('\n')
		.filter((product) => product !== '')
		.map((product) => product.split(', '));

	let foundProduct = null;

	rl.question('Which product do you want to consult?\n', (productName) => {
		if (productName === '') {
			console.log('Please enter a valid product name');
		} else {
			for (const product of productsArray) {
				if (product[0].includes(productName)) {
					foundProduct = product;
					break;
				}
			}

			if (!foundProduct) {
				console.log(`${productName} not found`);
			} else {
				const quantity = parseInt(foundProduct[1]);
				const price = parseFloat(foundProduct[2].substring(1));
				const totalByProduct = quantity * price;

				console.log(
					`\nTotal sales by product ${productName}: $${totalByProduct}`
				);
			}
		}
		toMain();
	});
}

function totalSales() {
	const productsInfo = fs.readFileSync(SALES_FILE_NAME, 'utf-8');
	const productsArray = productsInfo
		.split('\n')
		.filter((product) => product !== '')
		.map((product) => product.split(', '));

	let totalSales = 0;

	for (const product of productsArray) {
		const quantity = parseInt(product[1]);
		const price = parseFloat(product[2].substring(1));
		totalSales += quantity * price;
	}

	console.log(`\nTotal sales: $${totalSales}`);

	toMain();
}

function allProducts() {
	const productsInfo = fs.readFileSync(SALES_FILE_NAME, 'utf-8');
	const productsArray = productsInfo
		.split('\n')
		.filter((product) => product !== '')
		.map((product) => product.split(', '));

	for (const product of productsArray) {
		console.log(product.join(', '));
	}

	toMain();
}
