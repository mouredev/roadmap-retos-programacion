/**
 * Usando Node para poder realizar los ficheros en JavaScript
 */

//---EJERCIÓ SIMPLE---
// Extension de para realizar el archivo plano
const fs = require('fs');

// El contenido del archivo de texto
const nombre = "Jesus Antonio Escamilla Escamilla";
const edad = "24";
const lenguajeP = "JavaScript, Python, Java y C#"
const contenido = `Mi nombre es ${nombre} y mi edad es ${edad} y mi lenguaje de programación favorito es: ${lenguajeP}`;

// La Ruta y Nombre del archivo plano
const rutaArchivo = 'JesusAntonioEEscamilla.txt';

// Aquí hacemos un try-catch para evitar los errores
try {
    //  Aquí creamos el archivo con el contenido
    fs.writeFileSync(rutaArchivo, contenido);
    console.log('Archivo creado exitosamente el archivo plano.');

    //  Aquí lo eliminamos el archivo plano
    fs.unlinkSync(rutaArchivo);
    console.log('Archivo eliminado correctamente el archivo plano.');
} catch (error) {
    console.error('Error al crear el archivo:', error);
}



/**-----DIFICULTAD EXTRA-----*/
//Pendientes
/**-----DIFICULTAD EXTRA-----*/