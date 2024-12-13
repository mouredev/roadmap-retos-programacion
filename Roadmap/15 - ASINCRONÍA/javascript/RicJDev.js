//EJERCICIO
const asyncDisplay = (name, seconds) => {
	console.log(
		`\n${name} empezó a ejecutarse\n(${new Date().toLocaleTimeString()})`
	);
	console.log(`Duración: ${seconds} segundo(s)`);

	return new Promise((resolve, reject) => {
		setTimeout(() => {
			console.log(
				`\n${name} se ha ejecutado\n(${new Date().toLocaleTimeString()})`
			);
			resolve();
		}, seconds * 1000);
	});
};

asyncDisplay('Mi función', 8);

//DIFICULTAD EXTRA
const runAllFuntions = async () => {
	await Promise.all([
		asyncDisplay('Función C', 3),
		asyncDisplay('Función B', 2),
		asyncDisplay('Función A', 1),
	]);

	await asyncDisplay('Función D', 1);
};

runAllFuntions();
