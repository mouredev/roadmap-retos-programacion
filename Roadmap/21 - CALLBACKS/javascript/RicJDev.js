//EJERCICIO
function callbackFunction1(callback) {
	callback();
	console.log('\nSe ejecuta la primera función');
}

callbackFunction1(() => {
	console.log('\nSe ejecuta la primera callback');
});

function callbackFunction2(callback) {
	console.log('\nSe ejecuta la segunda función');
	callback();
}

callbackFunction2(() => {
	console.log('\nSe ejecuta la segunda callback');
});

//EXTRA
function setRandomTime(callback) {
	let randomNum = Math.floor(Math.random() * 11);

	return new Promise((resolve) => {
		setTimeout(() => {
			callback();
			console.log(`Ejecutado en ${randomNum} segundo(s)`);
			resolve();
		}, randomNum * 1000);
	});
}

async function orderDish(order, confirm, getReady, deliver) {
	console.log(`\nProcesando pedido ${order}`);

	await setRandomTime(() => {
		confirm(order);
	});

	await setRandomTime(() => {
		getReady(order);
	});

	await setRandomTime(() => {
		deliver(order);
	});
}

let myOrder = 'pizza con piña';

orderDish(
	myOrder,
	(order) => {
		console.log(`\nConfirma el pedido: ${order}`);
	},
	(order) => {
		console.log(`\nEl pedido ${order} está listo!`);
	},
	(order) => {
		console.log(`\nEl pedido ${order} ha sido entregado!`);
	}
);
