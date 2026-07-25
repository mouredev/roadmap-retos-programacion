let contactos : Map<string , number> = new Map();

function pedirNombre() : string {
    let nombre : string | null;
    do {
        nombre = prompt("Ingresa el nombre:  ");
    } while ( !nombre );
    return nombre;
}

function validarNumero(numero: number) : boolean {
    return numero < 10000000000 && numero > 999999999;
}

function crearContacto() {
    let nombre : string | null;
    let numero : number;
    do {
        nombre = prompt("Ingresa el nombre:");
        numero = Number(prompt("ingresa el numero: "));
    } while ( !nombre || isNaN(numero) || !validarNumero(numero));

    return {
        "nombre": nombre.toString(),
        "numero": numero,
    };
}

do {
    let nombre : string;
    let contacto : {nombre : string, numero: number};

    console.log("1. Agregar un contacto");
    console.log("2. Buscar un contacto");
    console.log("3. Eliminar un contacto");
    console.log("4. Actualizar un contacto");
    console.log("5. Ver todos los contactos");
    console.log("6. Salir");

    var operacion : number = Number(prompt(":  "));

    switch (operacion) {
        case 1: 
            contacto = crearContacto(); 
            contactos.set(contacto.nombre, contacto.numero);
            break;
        
        case 2: 
            nombre = pedirNombre();
            if (contactos.get(nombre))
                console.log({"nombre": nombre, "numero": contactos.get(nombre)});
            else 
                console.log("paila");
            break;
        
        case 3: 
            nombre = pedirNombre();
            if (!(contactos.delete(nombre)))
                console.log("paila");
            break;
        
        case 4:
            nombre = pedirNombre();
            if (contactos.get(nombre)) {
                contacto = crearContacto();
                contactos.delete(nombre)
                contactos.set(contacto.nombre, contacto.numero);
            }
            else 
                console.log("paila");
            break;

        case 5:
            console.log(Array.from(contactos.entries()));
            break;
    }

} while ( operacion != null && operacion != 6);
