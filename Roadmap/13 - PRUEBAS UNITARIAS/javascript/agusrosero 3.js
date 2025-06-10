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

// EJERCICIO:
const suma = (a, b) => {
  return a + b;
};

result = suma(10, 5);
if (result === 15) {
  console.log("El resultado es correcto!");
} else {
  console.log("El resultado no es el esperado.");
}

// DIFICULTAD EXTRA:
miDiccionario = {
  name: "Hernan",
  age: 23,
  birthDate: "03-08-00",
  programmingLanguages: ["Python", "Javascript"],
};

function testCampos() {
  const campos = ["name", "age", "birthDate", "programmingLanguages"];
  for (const campo of campos) {
    if (campo in miDiccionario) {
      console.log("Todos los campos estan en el diccionario");
      return true;
    }
  }
  console.log("Error uno de los campos no se encuentra en miDiccionario.");
  return false;
}

testCampos();

function isDateValid(dateString) {
  const datePattern = /^\d{2}-\d{2}-\d{2}$/;
  return datePattern.test(dateString);
}

function isProgrammingLanguagesValid(languages) {
  return (
    Array.isArray(languages) &&
    languages.every((lang) => typeof lang === "string")
  );
}

function validarDiccionario(diccionario) {
  if (typeof diccionario.name !== "string" || diccionario.name.trim() === "") {
    console.log("Nombre invalido");
    return false;
  }

  if (typeof diccionario.age !== "number" || diccionario.age <= 0) {
    console.log("Edad invalida");
    return false;
  }

  if (!isDateValid(diccionario.birthDate)) {
    console.log("Fecha invalida");
    return false;
  }

  if (!isProgrammingLanguagesValid(diccionario.programmingLanguages)) {
    console.log("Lenguaje de programacion invalido");
    return false;
  }

  return true;
}

if (validarDiccionario(miDiccionario)) {
  console.log("Todos los datos son correctos.");
} else {
  console.log("Hay datos incorrectos en el diccionario.");
}
