const sumar = (n1, n2) => n1 + n2

// Pruebas manuales
console.log(sumar(2, 3) === 5); // true
console.log(sumar(-1, 1) === 0); // true
console.log(sumar(0, 0) === 0); // true


// Testing Automatizado (sin framework)
const assert = (description, result) => {
  if (result) {
    console.log(`✔️  ${description}`);
  } else {
    console.error(`❌  ${description}`);
  }
};

const tests = () => {
  assert("Suma de 2 y 3 es 5", sumar(2, 3) === 5);
  assert("Suma de -1 y 1 es 0", sumar(-1, 1) === 0);
  assert("Suma de 0 y 0 es 0", sumar(0, 0) === 0);
};

tests();


// Dificultad extra
const persona = {
  name: "7R0N1X",
  age: "25",
  birth_date: "30-08-1999",
  programming_languages: ["HTML", "CSS", "JS"]
};

const testCamposExistentes = (persona) => {
  const expectedFields = ["name", "age", "birth_date", "programming_languages"];
  return expectedFields.every(field => field in persona);
};

// Test
console.log(testCamposExistentes(persona) ? "✔️ Todos los campos existen" : "❌ Faltan campos");


const testDatosCorrectos = (persona) => {
  return (
    persona.name === "7R0N1X" &&
    persona.age === "25" &&
    persona.birth_date === "30-08-1999" &&
    Array.isArray(persona.programming_languages) &&
    persona.programming_languages.length > 0
  );
};

// Test
console.log(testDatosCorrectos(persona) ? "✔️ Los datos son correctos" : "❌ Los datos no son correctos");
