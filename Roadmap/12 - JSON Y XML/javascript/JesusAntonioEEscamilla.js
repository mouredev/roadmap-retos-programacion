/**
 * XML (Extensible Markup Lenguaje), es similar a HTML pero con etiquetas personalizadas.
 * XML tiene una sintaxis estandarizada, lo que permite que los datos compartidos o transmitidos a través de sistemas o plataformas puedan ser analizados por el destinatario.
 * JSON (JavaScript Object Notation), es un formato de texto para datos estructurados en aplicaciones web.
 * El artículo proporciona información sobre cómo trabajar con JSON utilizando JavaScript, incluido el análisis de JSON para acceder a los datos y la creación de JSON.
 */


// Extension para crear los ficheros XML y JSON
const fs = require('fs');

// Expresión del objeto sin estructurar
const dataXML_JSON = {
    'nombre': 'Fatima',
    'edad': 21,
    'fecha_Nacimiento': '30-01-2000',
    'programación_Lenguaje': ['JavaScript', 'Python']
};


//---EJERCIÓ SIMPLE XML ESTRUCTURADO---

// Nombre y Ruta del XML
xmlFile = 'JesusAntonioEEscamilla.xml';

// Creando XML a mano
const xmlObjeto = `
<data>
    <nombre>Jesus Antonio Escamilla Escamilla</nombre>
    <edad>24</edad>
    <fecha_Nacimiento>22-12-1999</fecha_Nacimiento>
    <programación_Lenguaje>
        <item>JavaScript</item>
        <item>Python</item>
        <item>Java</item>
        <item>PHP</item>
    </programación_Lenguaje>
</data>
`;

// Guardar el XML
try {
    // Se crea el fichero XML
    fs.writeFileSync(xmlFile, xmlObjeto);

    // Se lee el fichero XML
    const leerXML = fs.readFileSync(xmlFile, 'utf-8');
    console.log(leerXML);

    // Se elimina el fichero XML
    //fs.unlinkSync(xmlFile);
} catch (error) {
    console.error('Se encontró un error en el XML: ', error);
}


//---EJERCIÓ SIMPLE XML NO ESTRUCTURADO---

const convertToXML = (obj, data = 'data') => {
    let xml = `<${data}>`;
    for (let key in obj){
        if (typeof obj[key] === 'object'){
            xml += convertToXML(obj[key], key);
        } else {
            xml += `<${key}>${obj[key]}</${key}>`;
        }
    }
    xml += `<${data}>`;
    return xml;
};

// Convertir en objeto a XML
const xmlData = convertToXML(dataXML_JSON);

// Crea fichero XML
fs.writeFileSync('Faty.xml', xmlData);

// Se elimina
fs.unlinkSync('Faty.xml');



//---EJERCIÓ SIMPLE JSON ESTRUCTURADO---

// Nombre y Ruta del XML
jsonFile = 'JesusAntonioEEscamilla.json';

// Creando el JSON
const dataJSON = {
    data: {
        nombre: 'Jesus Antonio Escamilla Escamilla',
        edad: 24,
        fecha_Nacimiento: 22-12-1999,
        programación_Lenguaje: ['JavaScript', 'Python', 'Java', 'PHP']
    }
};

// Convetir en formato JSON
const JsonData = JSON.stringify(dataJSON, null, 2);

try {
    // Se crea el fichero JSON
    fs.writeFileSync(jsonFile, JsonData);

    // Se lee en consola
    const leerJSON = fs.readFileSync(jsonFile, 'utf-8');
    console.log(leerJSON);

    // Se elimina el fichero JSON
    // fs.unlinkSync(jsonFile);
} catch (error) {
    console.error('Se encontró un error en el JSON: ', error);
}


//---EJERCIÓ SIMPLE JSON NO ESTRUCTURADO---

// Convertir el objeto a JSON
const jsonData = JSON.stringify(dataXML_JSON, null, 2);

// Se crea el fichero JSON
fs.writeFileSync('Faty.json', jsonData);

// Se elimina el fichero JSON
fs.unlinkSync('Faty.json');



/**-----DIFICULTAD EXTRA-----*/
// Pendiente
/**-----DIFICULTAD EXTRA-----*/