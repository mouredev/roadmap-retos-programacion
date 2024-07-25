// Ejercicio 1º

    let texto : string = 'Buenas días! Hoy hacen 25º Grados en pleno 16 de Abril de 2024';

    let expresionRegular = /\d+/g;

    let numeros = texto.match(expresionRegular);

    if(numeros !== null){
        console.log(`Números encontrados: ${numeros}`);
    }else{
        console.log(`No hay números`);
    }

// Ejercicio Extra
    // GMAIL
        let expresionGmail = /^[a-zA-Z0-9._%+-]+@gmail\.com$/;
        let correoElectronico = 'adri.iglesias.fernandez@gmail.com';

        if (expresionGmail.test(correoElectronico)) {
            console.log('El correo electrónico es válido.');
        } else {
            console.log('El correo electrónico no es válido.');
        }

    // Nº Telefono - Versión España
        let expresionTelefono = /^\+34\s?(\d{3}\s?){3}$/;
        let numeroTelefono = '+34 123 456 789';
        
        if (expresionTelefono.test(numeroTelefono)) {
            console.log('El número de teléfono es válido.');
        } else {
            console.log('El número de teléfono no es válido.');
        }
    
    // URL
        let expresionURL = /^(http|https):\/\/[a-zA-Z0-9]+(\.[a-zA-Z]{2,}){1,}$/;
        let url = 'https://igledev.netlify.app';
        
        if (expresionURL.test(url)) {
            console.log('La URL es válida.');
        } else {
            console.log('La URL no es válida.');
        }