// El archivo utiliza Jest. Su uso:
// 1º Se debe de ejecutar el comando "npm i --save-dev jest"
// 2º En la lista de scripts dentro de package-lock.json, incluir "test": "jest"
// 3º Para probar los test, cambiar el nombre del archivo a "IgleDev.test.ts".
// 4º Para ejecutar el test ejecutar el siguiente comando: "npm test"
    
// 1º Ejercicio
    let suma = (a, b) => {  // En jest no podemos indicar el tipo que es debido a que el ':' no lo reconoce
        return a + b
    }

    test('Función suma', () => {
        expect(suma(5, 5)).toBe(10);
    });

// DIFICULTAD EXTRA
    let diccionario = {
        name: 'Adrián', 
        age: 19,
        birth_date: '03/11/2004',
        programming_languages: [
          'TypeScript', 'JavaScript', 'HTML', 'CSS'
        ]
    };

    test('Existen los campos', () => {
        let keys = Object.keys(diccionario);
        expect(keys).toContain('name');
        expect(keys).toContain('age');
        expect(keys).toContain('birth_date');
        expect(keys).toContain('programming_languages');
    });

    test('Datos introducidos correctos', () =>{
        let datos = Object.values(diccionario);
        expect(datos).toContain('Adrián');
        expect(datos).toContain(19);
        expect(datos).toContain('03/11/2004');
        expect(datos[3]).toEqual([
            'TypeScript', 'JavaScript', 'HTML', 'CSS'
        ]);
    });