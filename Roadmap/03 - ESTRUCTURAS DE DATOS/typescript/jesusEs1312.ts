/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */

// Arrays
let stringArray: string[]   = ["Spider Man", "Batman"];// Type String
let numberArray: number[]   = [1, 2, 3, 4, 5];// Type number
let booleanArray: boolean[] = [true, false];// Type boolean
let readOnlyArray: readonly string[] = ["Hello", "World"];// Type ReaonlyArray<string>
let obj: any = { x:0 };// Type Any (Special Type)

console.log("Array inicial: " + stringArray);

//--- push (Add new element to the end)
stringArray.push("Super Man");
console.log("Agregar un elemento (push): " + stringArray);

//--- Pop (Removes the last element from an array and returns it)
console.log("Eliminar un elemento (pop): " + stringArray.pop()); 

//--- sort
stringArray.sort();
console.log("Array ordenado (sort): " + stringArray);

//--- Tuple Type
type stringNumberPair = [string, number];// Tuple type of string and number 

function doSomething(stringNumberPair: [string, number]): string {
    const a = stringNumberPair[0];// const a: string
    const b = stringNumberPair[1];// const b: number
    return a + b;
}

console.log(
    doSomething(["Hello ", 13])
);

/**
 * StringNumberBooleans describes a tuple whose first two elements are string and number respectively, 
 * but which may have any number of booleans following.
 */
type StringNumberBooleans = [string, number, ...boolean[]];
const a: StringNumberBooleans = ["hello", 1];
const b: StringNumberBooleans = ["beautiful", 2, true];
const c: StringNumberBooleans = ["world", 3, true, false, true, false, true];
    
console.log(a);

//--- Set
const setA: Set<number> = new Set([1,2,3]);
const setB: Set<number> = new Set([4,5,3]);

//--- Map
const mapA: Map<number, string> = new Map([
    [1, "one"],
    [2, "two"],
    [4, "four"]
]);

//--- EXTRA
const numberRegexp = /^[0-9]+$/;

interface NumberValidation {
    isAcceptable(s: string): boolean;
}

export class Contact implements NumberValidation{
    public name: string | null = "";
    public cel:  string | null = "";
    
    isAcceptable(s: string | null): boolean {
        return (s?.length == 11 || s?.length == 10) && numberRegexp.test(s);
    }


}

//Map de contactos
let contacts: Map<string | null, Contact> = new Map();

//--- Agregar contacto
function addContact(): void {
    let name: string | null = "" ; 
    let cel:  string | null = "";
    let contact = new Contact();

    name = prompt("Escribe el nombre del contacto:");
    
    do{
        if(cel != ""){
            alert("El celular no es correcto, intenta de nuevo");
        }
        cel  = prompt("Escribe el celular del contacto (Solo numeros y menos de 11 digitos)");
    } while(!contact.isAcceptable(cel));
    

    contact.name = name;
    contact.cel  = cel;
    contacts.set(name, contact);//Agregamos el contacto
    alert("¡Se agrego el contacto exitosamente!");
    console.log(contacts);
}

//--- Encontrar contacto por nombre
function findContactByName(): void {
    let nameFind: string | null;
    let contactFind: Contact | undefined = new Contact();
    nameFind = prompt("Ingresa el nombre del contacto a buscar:");
    contactFind = contacts.get(nameFind);
    if (contactFind == undefined) {
        alert("¡No se encontro el nombre!");
    } else {
        alert(
            "Nombre: " + contactFind.name?.concat(" \n") +
            "Celular: " + contactFind.cel
        );
    }
}

function updateContactByName(): void {
    //Contacto a actualizar
    let contactUpdate: Contact = new Contact();
    let nameUpdate: string | null = "";
    let celUpdate: string | null = "";
    let nameFind: string | null = "";
    let contactFind: Contact | undefined = new Contact();

    nameFind = prompt("Ingresa el nombre del contacto que quieres actualizar:");
    contactFind = contacts.get(nameFind);
    if(contactFind == undefined){
        alert("¡No se encontro el nombre del contacto");
    } else {
        nameUpdate = prompt("Ingresa el nuevo nombre:");
        do{
            if(celUpdate != ""){
                alert("El celular no es correcto, intenta de nuevo");
            }
            celUpdate  = prompt("Escribe el celular del contacto (Solo numeros y menos de 11 digitos)");
        } while(!contactFind.isAcceptable(celUpdate));

        contactUpdate.name = nameUpdate;
        contactUpdate.cel  = celUpdate;
        contacts.set(nameUpdate, contactUpdate);
        contacts.delete(nameFind);
        alert("¡Contacto actualizado exitosamente!");
    }
}

function deleteContactByName(): void {
    let nameFind: string | null = "";
    nameFind = prompt("Ingresa el nombre a eliminar:");
    if(contacts.delete(nameFind)){
        alert(`¡El contacto ${nameFind} se elimino exitosamente!`);
    } else {
        alert(`¡El contacto ${nameFind} no existe¡`);
    }
}

function findAllContacts(): void {
    let numberContact: number = 1;
    contacts.forEach((contact) => {
        alert(
            numberContact + ".-\n" + 
            "Name: " + contact.name + "\n" +
            "Cel: "  + contact.cel + "\n"
        );
        numberContact++;
    });
}

function agendaApp(): void {
    let option: string | null= "";
    const menu: string = "Menu: \n 1. Agregar \n 2. Buscar \n 3. Actualizar \n 4. Eliminar \n 5. Listar contactos \n 6. Salir";

    while(option !== '6') {
        option = prompt(menu);
        switch(option){
            case '1':
                addContact();
                break;
            case '2':
                findContactByName();
                break;
            case '3':
                updateContactByName();
                break;
            case '4':
                deleteContactByName();
                break;
            case '5':
                findAllContacts();
                break;
            case '6':
                alert("Bye");
                break;
            default:
                alert("¡Opcion no valida!");
                break;
        }
    }
}

agendaApp();

























