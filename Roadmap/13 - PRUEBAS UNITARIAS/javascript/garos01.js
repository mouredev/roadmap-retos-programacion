// Función para sumar dos números
function sumar(a, b) {
  return a + b;
}

// Función para realizar pruebas
function testSuma() {
  // Caso de prueba 1
  const num1 = 5;
  const num2 = 3;
  const expected = 8;
  const result = sumar(num1, num2);
  if (result === expected) {
    console.log("Caso de prueba 1: Éxito");
  } else {
    console.error("Caso de prueba 1: Falló");
  }

  // Caso de prueba 2
  const num3 = -2;
  const num4 = 10;
  const expected2 = 8;
  const result2 = sumar(num3, num4);
  if (result2 === expected2) {
    console.log("Caso de prueba 2: Éxito");
  } else {
    console.error("Caso de prueba 2: Falló");
  }
}

// Ejecutar las pruebas
testSuma();

// Ejercicio extra

const miPerfil = {
  name: "Oscar Garzon",
  age: 29,
  birth_date: "11-09-1994",
  programming_languages: ["JavaScript", "Python"],
};

// Test para verificar si todos los campos existen
function testExistenciaCampos() {
  const camposRequeridos = [
    "name",
    "age",
    "birth_date",
    "programming_languages",
  ];
  let todosPresentes = true;

  camposRequeridos.forEach((campos) => {
    if (!(campos in miPerfil)) {
      console.error(`Campo ${campos} no encontrado.`);
      todosPresentes = false;
    }
  });

  if (todosPresentes) {
    console.log("Todos los campos están presentes.");
  } else {
    console.error("No se encontraron todos los campos.");
  }
}

// Test para verificar si los datos son correctos
function testDatosCorrectos() {
  let datosCorrectos = true;

  // Verificar edad
  if (typeof miPerfil.age !== "number" || miPerfil.age <= 0) {
    console.error("La edad no es un número válido.");
    datosCorrectos = false;
  }

  // Verificar fecha de nacimiento (formato simplificado)
  const fechaNacimiento = new Date(miPerfil.birth_date);
  if (isNaN(fechaNacimiento.getTime())) {
    console.error("Fecha de nacimiento no válida.");
    datosCorrectos = false;
  }

  // Verificar si el listado de lenguajes de programación es un array
  if (
    !Array.isArray(miPerfil.programming_languages) ||
    miPerfil.programming_languages.length === 0
  ) {
    console.error("Listado de lenguajes de programación no válido.");
    datosCorrectos = false;
  }

  if (datosCorrectos) {
    console.log("Los datos son correctos.");
  } else {
    console.error("Algunos datos no son correctos.");
  }
}

// Ejecutar los tests
testExistenciaCampos();
testDatosCorrectos();
