// ** EJERCICIO

function sum(num1, num2) {
    try {
        if (typeof num1 === 'number' && isFinite(num1) && typeof num2 === 'number' && isFinite(num2)) {
            return num1 + num2;
        } else {
            console.error('Introduzca un número válido');
            return null;
        }
    } catch (err) {
        console.error('No se ha podido realizar la suma', err);
        return null;
    }
}


// ** DIFICULTAD EXTRA ** ----------------------------------------------------------------------------------------------------------------------------------------------------

let diccionario = {
    name: 'Bernat',
    age: 88,
    birth_date: '2000-01-01',
    programming_languages: ['List1', 'List2', 'List3']
}

function test1() {
    if ('name' in diccionario && 'age' in diccionario && 'birth_date' in diccionario && 'programming_languages' in diccionario) {
        console.log('Diccionario completo')
    } else {
        console.log('Diccionario incompleto')
    }
}

test1()

function test2() {
    if (
        typeof(diccionario.name) === 'string' && 
        typeof(diccionario.age) === 'number' && 
        /^\d{4}-\d{2}-\d{2}$/.test(diccionario.birth_date) && 
        Array.isArray(diccionario.programming_languages)
    ) {
        console.log('Los datos son correctos')
    } else {
        console.log('Los datos NO son correctos')
    }
}

test2()