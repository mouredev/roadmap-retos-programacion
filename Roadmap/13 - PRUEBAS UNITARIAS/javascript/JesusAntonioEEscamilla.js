/** #13 - JavaScript ->Jesus Antonio Escamilla */
//---EJERCIÓ---

// Función de suma
function sumar(num1, num2) {
    return num1 + num2;
}

// Función TEST
function test_Suma() {
    const resultado = sumar(3, 7);
    console.log(resultado === 10
        ? 'El test funciona'
        : 'Algo fallo en el test');
}

// Se Ejecuta el test y la suma
test_Suma();



/**-----DIFICULTAD EXTRA-----*/

//  Se crea un el diccionario de la claves y valores
const informaciónPersonal = {
    'name': 'Jesus Antonio Escamilla',
    'age': 24,
    'birth_date': 22-12-1999,
    'programming_languages': ['JavaScript', 'Python', 'Java', 'PHP']
}

//  Se crea un test para checa los campos del diccionario
function test_ExisteCampos() {
    const camposEsperado = ["name", "age", "birth_date", "programming_languages"];
    const camposExisten = Object.keys(informaciónPersonal);

    let todosLosCamposPresentes = true;
    camposEsperado.forEach(campo => {
        if (!camposExisten.includes(campo)) {
        console.error(`Campo faltante: ${campo}`);
        todosLosCamposPresentes = false;
        }
    });

    console.log(todosLosCamposPresentes 
        ? "Test de campos: CORRECTO" 
        : "Test de campos: FALLO");
}

//  Se crea un test para checa que si son correctos los campos del diccionario
function test_DatosCorrectos() {
    const nombreEsperado = 'Jesus Antonio Escamilla';
    const edadEsperado = 24;
    const fechaNacimientoEsperado = 22-12-1999;
    const lenguajesEsperados = ['JavaScript', 'Python', 'Java', 'PHP'];

    const nombre = informaciónPersonal.name;
    const edad = informaciónPersonal.age;
    const fechaNacimiento = informaciónPersonal.birth_date;
    const lenguajes = informaciónPersonal.programming_languages;

    const datosCorrectos = 
        nombre === nombreEsperado &&
        edad === edadEsperado &&
        fechaNacimiento === fechaNacimientoEsperado &&
        JSON.stringify(lenguajes) === JSON.stringify(lenguajesEsperados);

    console.log(datosCorrectos 
        ? "Test de datos correctos: CORRECTOS"
        : "Test de datos correctos: FALLO");

}

// Se utiliza los test aquí
test_ExisteCampos()
test_DatosCorrectos()

/**-----DIFICULTAD EXTRA-----*/