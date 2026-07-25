
 /* DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let contactos = [
        { nombre: "Marcos", numero: "1234567894" },
        { nombre: "Andrea", numero: "1478523690" },
        { nombre: "Carlos", numero: "4893175451" }
    ];

function menu(){
    rl.question(`Elija una opción:
    1 - Buscar contacto
    2 - Añadir contacto 
    3 - Actualizar contacto
    4 - Eliminar contacto
    5 - Salir
    `, (opcion) => {
        switch(opcion){
            case '1':
                rl.question('Ingrese el nombre que busca:', (busqueda)=>{
                    const contacto = contactos.find(c => c.nombre.toLowerCase() === busqueda.toLowerCase());
                    if(contacto) console.log(`Sí se encuentra ${contacto.nombre}`);
                    else console.log("Contacto no encontrado");
                    menu();
                });
                break;
            case '2':
                rl.question('Ingrese el nombre:', (nombre) => {
                    function pedirNumero() {
                        rl.question('Ingrese el número:', (numero) => {
                            if (!/^\d{1,11}$/.test(numero)) {
                                console.log("Número inválido. Debe ser numérico y hasta 11 dígitos.");
                                pedirNumero();
                            } else {
                                contactos.push({ nombre, numero });
                                console.log(`Contacto agregado: ${nombre} - ${numero}`);
                                menu();
                            }
                        });
                    }
                    pedirNumero();
                });
                break;
            case '3':
                rl.question('Ingrese el nombre del contacto a actualizar:', (nombreBuscado) => {
                    const idx = contactos.findIndex(c => c.nombre.toLowerCase() === nombreBuscado.toLowerCase());
                    if (idx === -1) {
                        console.log('Contacto no encontrado.');
                        menu();
                    } else {
                        function pedirNuevoNumero() {
                            rl.question('Ingrese el nuevo número:', (nuevoNumero) => {
                                if (!/^\d{1,11}$/.test(nuevoNumero)) {
                                    console.log('Número inválido. Debe ser numérico y hasta 11 dígitos.');
                                    pedirNuevoNumero();
                                } else {
                                    contactos[idx].numero = nuevoNumero;
                                    console.log(`Número actualizado para ${contactos[idx].nombre}: ${nuevoNumero}`);
                                    menu();
                                }
                            });
                        }
                        pedirNuevoNumero();
                    }
                });
                break;
            case '4':
                    rl.question('Ingrese el nombre del contacto a eliminar:', (nombreBuscado) => {
                        const contacto = contactos.find(c => c.nombre.toLowerCase() === nombreBuscado.toLowerCase());
                        if (contacto) {
                            contactos = contactos.filter(c => c.nombre.toLowerCase() !== nombreBuscado.toLowerCase());
                            console.log('Contacto eliminado.');
                        } else {
                            console.log('Contacto no encontrado.');
                        }
                        menu();
                    });
                    break;
            case '5':
                rl.close();
                break;
            default:
                console.log("Opción no válida")
                menu();
        }
    });
}
menu();