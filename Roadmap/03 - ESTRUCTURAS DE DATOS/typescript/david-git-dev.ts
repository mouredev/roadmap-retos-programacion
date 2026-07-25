/*
  EJERCICIO:
  - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
    en tu lenguaje.
  - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 */
//arrays
const array:string[]=[];
array.push('comienzo'); // operacion de insercion
array[0] ='actualizacion';//operacion de actualizacion
array.push('medio');
array.push('final');
array.push('error');
array.pop()//operacion de borrado
array.sort();//operacion de ordenamiento
//tuplas
const tupla: [number,string]=[0,'zero']// en la practica son para datos que no van a cambiar pero por alguna extraña razon todavia se puede usar push sobre tuplas y el editor no genera problema.
tupla.push(1,'as')//operacion de agregacion
tupla[0] = 999 //operacion de actualizacion
tupla.pop()//operacion de borrado
//--> todas las operaciones anteriores sobre la tupla no son recomendadas de hacer porque ese no es el sentido de la tupla pero se pueden hacer
//enums
const enum States{Incoming , Loading , Success}// no se pueden realizar operaciones de modificacion con esta estructura
//Set
let dontRepeatYourSelf = new Set([1,2,3,4]) // sobre esta estructura no se puede modificar directamente un valor ya introducido, ademas no permite datos repetidos.
dontRepeatYourSelf.add(5) // agregacion
dontRepeatYourSelf.delete(3)//borrado
//ejemplo de como podria hacerse una operacion de 'ordenacion' sobre un set
dontRepeatYourSelf = new Set([...dontRepeatYourSelf].sort((a,b)=>b-a))
//mapas
const map = new Map()
map.set('clave','valor')//agregacion
map.set('clave','actualizacion')//actualizacion
map.delete('clave')//borrado
//objetos
const objeto: { [key: string]: any } = {};
objeto.propiedadUno = "propiedad1"; //operaciones de agregacion
objeto.propiedadDos = "propiedad2";
delete objeto.propiedadUno;//operaciones de borrado
objeto.propiedadDos = "actualizacion"; //operaciones de actualizacion

/* DIFICULTAD EXTRA (opcional):*/
console.log(`
  Hola, bienvenido a tu agenda de contactos
    ¿Que deseas realizar?
    1- Agregar contacto
    2- Actualizar contacto
    3- Eliminar contacto
    ?- Buscar contacto
  Deja la respuesta vacia para salir de la agenda-->
    `);
  type Contacto = {
    nombre: string;
    numero: number;
  };
  type Agenda = {
    [key: string]: Contacto;
  };
  const agenda: Agenda = {};
  let opcion: string | null;
  do {
    let id: string | null;

    let informacion: string | null;
    opcion = prompt(`
    1- Agregar contacto
    2- Actualizar contacto
    3- Eliminar contacto
    ?- Buscar contacto
    Deja la respuesta vacia para salir de la agenda-->
    `);

    switch (opcion) {
      case "1":
        informacion = prompt(
          "Introduce el nombre y el telefono separados por una coma para cada par de (nombre,telefono) campo(ej): juan perez,4612349178"
        );
        if (informacion) agregar(informacion);
        break;
      case "2":
        id = prompt(
          "Introduce el nombre o el telefono para actualizar los datos del contacto..."
        );
        informacion = prompt(
          "Introduce tus nuevos datos...(ej): juan perez,4612349178"
        );
        if (id && informacion) actualizar(id, informacion);
        break;
      case "3":
        id = prompt("Introduce el nombre o el telefono para borrar el contacto");
        if (id) eliminar(id);
        break;
      case "?":
        id = prompt("Introduce el nombre o el telefono para buscarlo:");
        if (id) buscar(id);
        break;
      default:
        console.log(`Saliendo de la aplicacion....`);
        break;
    }
    console.log(agenda)
  } while (opcion);

  function agregar(datos: string) {
    const [nombre, numero] = datos.split(",");
    if (nombre && esUnNumeroValido(numero)) {
      const registro: Contacto = {
        nombre: nombre,
        numero: Number(numero),
      };
      agenda[window.crypto.randomUUID()] = registro;
    } else {
     error();
    }
  }
  function actualizar(id: string, contacto: string) {
    console.warn("Actualizando....");
    const [nombre, numero] = contacto.split(",");
    const res = Object.entries(agenda).find(
      ([, contacto]) => contacto.nombre == id || contacto.numero == Number(id)
    );
    if (res && esUnNumeroValido(numero)) {
      const uuid = res![0];
      agenda[uuid].nombre = nombre;
      agenda[uuid].numero = Number(numero);
      console.log("Actualizado");
    }else{
  error();
    }

  }
  function eliminar(id: string) {
    console.warn("Eliminando...");
    const uuid = buscar(id);
    const res = delete agenda[uuid]
      ? "Contacto eliminado...."
      : "Perdona... quien?";
    console.log(res);
  }
  function buscar(id: string): string {
    let uuid = "";

    const res = Object.entries(agenda).find(
      ([, contacto]) => contacto.nombre == id || contacto.numero == Number(id)
    );

    if (res) {
      uuid = res[0];
      console.log(`
  Vaya! a quien tenemos aqui?.....
  ${res}
  `);
      alert(`
  Vaya! a quien tenemos aqui?.....
  ${JSON.stringify(res)}
  `);
    } else {
     error()
    }

    return uuid;
  }
  function esUnNumeroValido(numero: string): boolean {
    return !isNaN(Number(numero)) && numero.length < 11;
  }

  function error(){
     console.warn(
        "ups....algo salio mal.Revisa si tus datos son registrado correctamente, no se admiten numeros de mas de 11 digitos"
      );
      alert(
        "ups....algo salio mal.Revisa si tus datos son registrado correctamente, no se admiten numeros de mas de 11 digitos"
      );
  }