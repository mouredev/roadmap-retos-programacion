let seleccion;
const contactos = [
  {
    nombre: 'Omar Tio',
    numero: 8292854059,
  },
];

const mostrarContactos = () => {
  let lista = '';

  contactos.forEach((contacto, i) => {
    lista += `${i + 1}. ${contacto.nombre} -> ${contacto.numero}\n`;
  });

  alert(lista);
};

const mostrarContacto = (contacto) => {
  alert(`
    Nombre: ${contacto.nombre}
    Numero: ${contacto.numero}
    `);
};

const agregarContacto = () => {
  const nombreContacto = prompt('Cual es el nombre de su contacto?');
  let numeroContacto;
  do {
    numeroContacto = prompt('Cual es el numero de telefono de su contacto? ');
    numeroContacto = Number(numeroContacto);
  } while (
    isNaN(numeroContacto) ||
    toString(numeroContacto).length > 10 ||
    toString(numeroContacto).length < 10
  );
  const contactoNuevo = { nombre: nombreContacto, numero: numeroContacto };
  console.log('Agregando contacto nuevo ...');
  console.table(contactoNuevo);
  contactos.push(contactoNuevo);
  console.log('Contacto agregado!');
};

const buscarContacto = (text) => {
  if (contactos.length === 0) {
    alert('No hay contactos en la agenda');
    return NaN;
  }

  mostrarContactos();

  const busqueda = Number(prompt(text));

  return [contactos[busqueda - 1], busqueda - 1];
};

const actualizarContactos = (contacto) => {
  let confirmarCambio = false;
  if (!contacto) return;
  const [{ nombre, numero }, idContacto] = contacto;

  const nombreNuevo = prompt(`Cual nombre nuevo quiere asignarle al contacto: 
  ${nombre}
  ${numero}`);
  const numeroNuevo = prompt(`Cual numero nuevo quiere asignarle al contacto: 
  ${nombre} -> ${nombreNuevo}
  ${numero}`);

  while (!confirmarCambio) {
    const conf = Number(
      prompt(` Desea confirmar el siguiente cambio?
      ${nombre} -> ${nombreNuevo}
      ${numero} -> ${numeroNuevo}
    1.Si
    2.No
      `)
    );
    if (conf === 1) {
      confirmarCambio = true;
    } else {
      break;
    }
  }

  if (confirmarCambio) {
    contactos[idContacto] = { nombre: nombreNuevo, numero: numeroNuevo };
  }
};

const borrarContacto = (contacto) => {
  let confirmarCambio = false;
  if (!contacto) return;
  const [{ nombre, numero }, idContacto] = contacto;

  while (!confirmarCambio) {
    const conf = Number(
      prompt(` Desea borrar el siguiente contacto?
      ${nombre}
      ${numero}
    1.Si
    2.No
      `)
    );
    if (conf === 1) {
      confirmarCambio = true;
    } else {
      break;
    }
  }

  if (confirmarCambio) {
    contactos.splice(idContacto, 1);
  }
};

while (seleccion != 6) {
  seleccion = Number(
    prompt(`
  1. Agregar Contactos
  2. Buscar Contactos
  3. Actualizar Contactos
  4. Borrar Contactos
  5. Mostrar Contactos
  6. Salir
  `)
  );
  switch (seleccion) {
    case 1:
      agregarContacto();
      break;
    case 2:
      mostrarContacto(
        buscarContacto(
          'Ingrese el numero de lista del contacto que desea buscar'
        )
      );
      break;
    case 3:
      actualizarContactos(
        buscarContacto(
          'Ingrese el numero de lista del contacto que desea actualizar'
        )
      );
      break;
    case 4:
      borrarContacto(
        buscarContacto(
          'Ingrese el numero de lista del contacto que desea borrar'
        )
      );
      break;
    case 5:
      mostrarContactos();
      break;
    case 6:
      seleccion = 6;
      break;
    default:
      break;
  }
}
