//EJERCICIO
const { error } = require('node:console');
const fs = require('node:fs');
const { stringify } = require('node:querystring');
const { create } = require('xmlbuilder2');
const { pd } = require('pretty-data');

let fileName1 = 'myJSON.json';

const personData = {
	name: 'Ric',
	age: 21,
	birhtDate: '22/09/2002',
	languages: ['JavaScript', 'HTML'],
};

fs.writeFile(fileName1, JSON.stringify(personData), (error) => {
	console.log('\n---CREANDO JSON---');
	if (error) {
		console.log(`Se produjo un error: ${error}`);
	}
	console.log('Fichero creado!');
	fs.readFile(fileName1, 'utf8', (error, data) => {
		console.log('\n---LEYENDO JSON---');
		if (error) {
			console.log(`Se produjo un error: ${error}`);
		}
		console.log(data);
		fs.unlink(fileName1, (error) => {
			console.log('\n---ELIMINANDO JSON---');
			if (error) {
				console.log(`Se produjo un error: ${error}`);
			}
			console.log('Fichero eliminado!');
		});
	});
});

let fileName2 = 'myXML.xml';

const xml = create({
	encoding: 'utf8',
	version: '1.0',
})
	.ele('raiz')
	.ele('Nombre', 'Ric')
	.up()
	.ele('Edad', 'Veintiuno')
	.up()
	.ele('Lenguajes', 'JavaScript')
	.end({ prettyPrint: true });

let xmlContent = pd.xml(xml);

fs.writeFile(fileName2, xmlContent, (error) => {
	console.log('\n---CREANDO XML---');
	if (error) {
		console.log(`Se produjo un error: ${error}`);
	}
	console.log('Fichero creado!');
	fs.readFile(fileName2, 'utf8', (error, data) => {
		console.log('\n---LEYENDO XML---');
		if (error) {
			console.log(`Se produjo un error: ${error}`);
		}
		console.log(data);
		fs.unlink(fileName2, (error) => {
			console.log('\n---ELIMINANDO XML---');
			if (error) {
				console.log(`Se produjo un error: ${error}`);
			}
			console.log('Fichero eliminado!');
		});
	});
});

//TODO: dificultad extra.