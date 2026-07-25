/*
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un diccionario con las siguientes claves y valores:
 * "name": "Tu nombre"
 * "age": "Tu edad"
 * "birth_date": "Tu fecha de nacimiento"
 * "programming_languages": ["Listado de lenguajes de programación"]
 * Crea dos test:
 * - Un primero que determine que existen todos los campos.
 * - Un segundo que determine que los datos introducidos son correctos.
 */

function sum(a, b) {
  return a + b;
}

function sumTest() {
  const resultado = sum(3, 5);
  const esperado = 8;

  if (resultado !== esperado) {
    throw new Error(`Error: ${resultado} es distinto de ${esperado}`);
  } else {
    console.log("!Test OK");
  }
}

try {
  sumTest();
} catch (error) {
  console.error(error.message);
}

const user = {
  name: "Jose",
  age: 25,
  birth_date: "05/11/98",
  programming_languages: ["javaScript", "Python", "Go", "C#"],
};

function userTest() {
  const userDate = ["name", "age", "birth_date", "programming_languages"];

  userDate.forEach((element) => {
    if (!(element in user)) {
      throw new Error(`Error: El campo ${element} no existe en el objeto user`);
    }

    console.log("Todos los campos existen en el objeto user!");
  });
}

function dataTest() {
  if (typeof user.name !== "string" || user.name.trim() === "") {
    throw new Error(
      `Error: el campo ${user.name} deber ser un string no vacio.`
    );
  }

  if (typeof user.age !== "number" || user.age < 0) {
    throw new Error(`Error: el campo ${user.age} debe ser un numero valido`);
  }

  if (typeof user.birth_date !== "string" || user.name.trim() === "") {
    throw new Error(
      `Error: el campo ${user.birth_date} deber ser un string no vacio.`
    );
  }

  if (!Array.isArray(user.programming_languages)) {
    throw new Error(
      `Error: el campo ${user.programming_languages} debe ser un array.`
    );
  }

  user.programming_languages.forEach((language) => {
    if (typeof language !== "string") {
      throw new Error(
        `Error: Cada lenguaje en ${user.programming_languages} debe ser un string`
      );
    }
  });

  console.log("Datos correctos");
}

try {
  userTest();
  dataTest();
} catch (err) {
  console.error(err.message);
}
