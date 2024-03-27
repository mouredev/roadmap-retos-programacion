function suma (a, b) {
    return a + b
}

//Test
function testSuma(){
        const resultado1 = suma(2, 2);
        console.log(resultado1 === 4 ? "Funciona" : "No funciona");
}
testSuma();

//EXTRA
const misDatos = {};

misDatos["name"] = "Maria";
misDatos["age"] = 33;
misDatos["birth_date"] = "8 de Diciembre de 1990";
misDatos["programming_languages"] = ["HTML", "CSS", "JavaScript"];

function testCampos() {
    const campos = ["name", "age", "birth_date", "programming_languages"];
    for(let campo of campos) {
        if (!(campo in misDatos)) {
            console.log(`Falta el campo "${campo}" en el diccionario.`);
            return false;
        }
    }
    console.log("Todos los campos existen en el diccionario.");
    return true;
}

function testDatos() {
    if (typeof misDatos.name !== "string" || misDatos.name === "") {
        console.error("El nombre no es válido.");
        return false;
    }
    if (isNaN(misDatos.age) || misDatos.age === "") {
        console.error("Edad no válida");
    }
    if (typeof misDatos.birth_date !== "string" || misDatos.birth_date === "") {
        console.error("Fecha no válida");
    }
    if (!Array.isArray(misDatos.programming_languages) || misDatos.programming_languages.length === 0) {
        console.error("Lenguajes no válidos");
        return false;
    }
    console.log("Datos correctos")
    return true;
}

testCampos();
testDatos();