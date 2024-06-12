/*
---PRUEBAS UNITARIAS CON JEST---

1. Instalar Jest (npm):
  npm i --save-dev jest
  npm i jest -D

2. Crear un package json:
  npm init --yes

3. En el package.json cambiar esto:

{
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
}

Por esto: 

{
  "scripts": {
    "test": "jest"
  },
}

4. Crear fichero con la extensión .test.js para escribir los test. Ejemplo: pruebasUnitarias.test.js

5. Ejecutar los test:
  npm run test
  npm test
  jest

* Nota: para este ejercicio usé el mismo fichero para las pruebas. Es necesario agregar la extensión .test.js al archivo para testear este código.
*/

function sum(a, b) {
	return a + b;
}

const myself = {
	name: 'Ric',
	age: 21,
	birthDate: '22/09/2002',
	programmingLanguages: ['JavaScript', 'HTML'],
};

//---EJERCICIO---

describe('Test de suma', () => {
	test('First test', () => {
		expect(sum(4, 5)).toBe(9);
	});
	test('Second test', () => {
		expect(sum(67, 23)).toBe(90);
	});
	test('Third test', () => {
		expect(sum(-20, 23)).toBe(3);
	});
});

//---EXTRA---

describe('Primer test de diccionario', () => {
	test('Check elements', () => {
    expect(Object.keys(myself).length).toBe(4)
  });
});

describe('Segundo test de diccionario', () => {
	test('Check name', () => {
		expect(myself.name).toBe('Ric');
	});
	test('Check age', () => {
		expect(myself.age).toBe(21);
	});
	test('Check birth date', () => {
		expect(myself.birthDate).toBe('22/09/2002');
	});
	test('Check programming languages', () => {
		expect(myself.programmingLanguages).toStrictEqual(['JavaScript', 'HTML']);
	});
});
