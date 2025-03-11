//#41 - CAMISETA RAR
/*
 * EJERCICIO:
 * ¿Has visto la camiseta.rar?
 * https://x.com/MoureDev/status/1841531938961592740
 *
 * Crea un programa capaz de comprimir un archivo 
 * en formato .zip (o el que tú quieras).
 * - No subas el archivo o el zip.
 */

//We will use JSZip library, which allows us to create and manipulate ZIP files in the browser or in a Node.js environment. 

let log = console.log;

const JSZip = require('jszip');
const fs = require('fs');

// Function to compress a file
async function compressFile(inputFilePath, outputZipPath) {
    const zip = new JSZip();

    // Read the file to be compressed
    const fileData = fs.readFileSync(inputFilePath);
    
    // Add the file to the zip
    zip.file(inputFilePath.split('/').pop(), fileData);

    // Generate the zip file
    const zipContent = await zip.generateAsync({ type: 'nodebuffer' });

    // Write the zip file to the output path
    fs.writeFileSync(outputZipPath, zipContent);
    log(`File compressed and saved as ${outputZipPath}`);
}

const inputFilePath = 'C:/Users/Niko Zen/Documents/a Nany.docx'; // Replace with the file path to compress
const outputZipPath = 'test_output.zip'; // Desired output zip file name

compressFile(inputFilePath, outputZipPath)
    .then(() => log('Compression complete!'))
    .catch(err => error('Error during compression:', err));

// Possible output: 
//File compressed and saved as test_output.zip
//Compression complete!