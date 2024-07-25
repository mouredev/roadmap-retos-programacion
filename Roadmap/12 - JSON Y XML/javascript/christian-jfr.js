// #12 JSON Y XML

/*
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
 * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
 * - Nombre
 * - Edad
 * - Fecha de nacimiento
 * - Listado de lenguajes de programación
 * Muestra el contenido de los archivos.
 * Borra los archivos.
 */

const fs = require('node:fs');

const dataJSON = {
	name: 'Christian',
	age: 21,
	birthdate: {
		day: 1,
		month: 5,
		year: 2003,
	},
	programmingLanguages: ['JavaScript', 'Python', 'C#', 'Java', 'C++'],
};
const dataXML = `
<?xml version="1.0" encoding="UTF-8"?>
<data>
    <name>${dataJSON.name}</name>
    <age>${dataJSON.age}</age>
    <birthdate>
      <day>${dataJSON.birthdate.day}</day>
      <month>${dataJSON.birthdate.month}</month>
      <year>${dataJSON.birthdate.year}</year>
    </birthdate>
    <programmingLanguages>
      <language>${dataJSON.programmingLanguages[0]}</language>
      <language>${dataJSON.programmingLanguages[1]}</language>
      <language>${dataJSON.programmingLanguages[2]}</language>
      <language>${dataJSON.programmingLanguages[3]}</language>
      <language>${dataJSON.programmingLanguages[4]}</language>
    </programmingLanguages>
</data>
`;

main();

function main() {
	setTimeout(createJSONFile, 1000, dataJSON);
	setTimeout(createXMLFile, 1500, dataXML);
	// setTimeout(deleteFiles, 2000);
}

function createJSONFile(data) {
	const toJSON = JSON.stringify(data);
	fs.writeFile('data.json', toJSON, (err) => {
		if (err) {
			console.error(err);
		} else {
			console.log('\n✅ JSON file has been created:\n');

			fs.readFile('data.json', 'utf8', (err, data) => {
				if (err) {
					console.error(err);
				} else {
					console.log(data);
				}
			});
		}
	});
}

function createXMLFile(data) {
	fs.writeFile('data.xml', data, (err) => {
		if (err) {
			console.error(err);
		} else {
			console.log('\n✅ XML file has been created:');

			fs.readFile('data.xml', 'utf8', (err, data) => {
				if (err) {
					console.error(err);
				} else {
					console.log(data);
				}
			});
		}
	});
}

function deleteFiles() {
	fs.unlink('data.json', (err) => {
		if (err) {
			console.error(err);
		} else {
			console.log('⚠️ JSON file has been deleted');
		}
	});
	fs.unlink('data.xml', (err) => {
		if (err) {
			console.error(err);
		} else {
			console.log('⚠️ XML file has been deleted');
		}
	});
}

/*
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
 */

class Data {
	constructor(name, age, birthdate, programmingLanguages) {
		this.name = name;
		this.age = age;
		this.birthdate = birthdate;
		this.programmingLanguages = programmingLanguages;
	}
}

setTimeout(() => {
	fs.readFile('data.json', 'utf8', (err, data) => {
		if (err) {
			console.error(err);
		} else {
			try {
				const jsonData = JSON.parse(data);

				const jsonClass = new Data(
					jsonData.name,
					jsonData.age,
					jsonData.birthdate,
					jsonData.programmingLanguages
				);

				console.log('JSON to Class:\n', jsonClass);
			} catch (error) {
				console.error(error);
			}
		}
	});
}, 2000);

setTimeout(() => {
	fs.readFile('data.xml', 'utf8', (err, data) => {
		if (err) {
			console.error(err);
		} else {
			try {
				const matchName = data.match(/<name>(.*?)<\/name>/);
				const name = matchName ? matchName[1] : '';

				const matchAge = data.match(/<age>(.*?)<\/age>/);
				const age = matchAge ? parseInt(matchAge[1]) : 0;

				const matchBirthdate = data.match(
					/<birthdate>\s*<day>(\d+)<\/day>\s*<month>(\d+)<\/month>\s*<year>(\d+)<\/year>\s*<\/birthdate>/
				);
				const birthdate = matchBirthdate
					? {
							day: parseInt(matchBirthdate[1]),
							month: parseInt(matchBirthdate[2]),
							year: parseInt(matchBirthdate[3]),
					  }
					: {};

				const matchLanguages = data.match(
					/<programmingLanguages>([\s\S]*?)<\/programmingLanguages>/
				);
				const programmingLanguages = matchLanguages
					? matchLanguages[1]
							.match(/<language>(.*?)<\/language>/g)
							.map(
								(language) => language.match(/<language>(.*?)<\/language>/)[1]
							)
					: [];

				const xmlCLass = new Data(name, age, birthdate, programmingLanguages);
				console.log('XML to Class:\n', xmlCLass);
			} catch (error) {
				console.error(error);
			}
		}
	});
}, 2500);

setTimeout(deleteFiles, 3000);
