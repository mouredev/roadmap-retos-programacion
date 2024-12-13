const { error } = require('node:console');
const fs = require('node:fs');


let fileName = 'RicMonster.txt';
let content = 'Nombre: Ricardo\nEdad: 21\nLenguaje favorito: JavaScript';

fs.writeFile(fileName, content, (error) => {
	console.log('\n---CREANDO EL FICHERO---');
	if (error) {
		console.log(`Error: ${error}`);
	}
	console.log(`${fileName} ha sido creado de manera exitosa!`);
	
	fs.readFile(fileName, 'utf8', (error, data) => {
		console.log('\n---LEYENDO EL FICHERO---');
		if (error) {
			console.log(`Error: ${error}`);
		}
		console.log(`Contenido de ${fileName}:\n${data}`);
		
		fs.unlink(fileName, (error) => {
			console.log('\n---ELIMINANDO EL FICHERO---');
			if (error) {
				console.log(`Error: ${error}`);
			}
			console.log(`${fileName} ha sido eliminado de manera exitosa`);
		});
	});
});
