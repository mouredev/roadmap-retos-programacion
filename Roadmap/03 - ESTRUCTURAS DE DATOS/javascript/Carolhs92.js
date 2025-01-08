import logo from './logo.png';
import './App.css';


function App() {
// Crear la lista
const mi_lista = [1, 2, 3];

// Agregar un nuevo elemento a la lista
mi_lista.push(4); 

// Borrar un elemento de la lista
const lista_menos = mi_lista.splice(2, 1);

// Actualizar un elemento de la lista
const lista_mas = mi_lista[5] = 7;

// Ordenar la lista
mi_lista.sort();


//Agenda de teléfono
 // Lista de contactos inicial
  const contacts = [];

 // Función para validar el número de teléfono
function isValidPhoneNumber(number) {
  return /^[0-9]{1,11}$/.test(number);
}

 // Función para agregar un contacto
function addContact() {
  const name = document.getElementById('name').value.trim();
  const phoneNumber = document.getElementById('number').value.trim();

  if (isValidPhoneNumber(phoneNumber)) {
    contacts.push({ name, phoneNumber });
    alert('Contacto agregado.');
    clearForm();
    showContacts();
  } else {
    alert('Número de teléfono inválido. Debe ser numérico y de hasta 11 dígitos.');
  }
}

 // Función para actualizar un contacto
function updateContact() {
  const name = prompt('Introduce el nombre del contacto a actualizar:');
  const phoneNumber = prompt('Introduce el nuevo número de teléfono:');

  if (isValidPhoneNumber(phoneNumber)) {
    const index = contacts.findIndex(contact => contact.name.toLowerCase() === name.toLowerCase());
    if (index !== -1) {
      contacts[index].phoneNumber = phoneNumber;
      alert('Contacto actualizado.');
    } else {
      alert('No se encontró el contacto.');
    }
      showContacts();
  } else {
    alert('Número de teléfono inválido. Debe ser numérico y de hasta 11 dígitos.');
  }
}

 // Función para eliminar un contacto
function deleteContact() {
  const name = prompt('Introduce el nombre del contacto a eliminar:');
  const index = contacts.findIndex(contact => contact.name.toLowerCase() === name.toLowerCase());

  if (index !== -1) {
    contacts.splice(index, 1);
      alert('Contacto eliminado.');
      showContacts();
  } else {
    alert('No se encontró el contacto.');
  }
}

 // Función para mostrar todos los contactos
function showContacts() {
  const contactListDiv = document.getElementById('contact-list');
  contactListDiv.innerHTML = ''; // Limpiar lista actual

  if (contacts.length > 0) {
    const ul = document.createElement('ul');
    contacts.forEach(contact => {
      const li = document.createElement('li');
      li.textContent = `Nombre: ${contact.name}, Teléfono: ${contact.phoneNumber}`;
      ul.appendChild(li);
    });
    contactListDiv.appendChild(ul);
  } else {
    contactListDiv.textContent = 'No hay contactos.';
  }
}

 // Función para limpiar el formulario
function clearForm() {
  document.getElementById('name').value = '';
  document.getElementById('number').value = '';
}

  return (
    
    <div class="App">
      <header class="App-header">
        <img src={logo} class="App-logo" alt="logo" />
      </header>
      <main>
        <section>
          <p>Oscar es el  <small class='resultado'>[{mi_lista[0]}]</small>  de su clase.</p>
          <p>Pero ha venido una persona nueva a la clase <small class='resultado'>[{mi_lista[2]}]</small> que se llama Lucas.</p>
          <p>Este mes Andrés tuvo que abandonar. Ahora somos <small class='resultado'>[{lista_menos}]</small></p>
          <p>Han venido varias personas más a la clase y ahora somos <small class='resultado'>[{lista_mas}]</small></p>
          <p>Despues de abandonos y llegadas a la clase ahora la lista queda así: <small class='resultado'>[{mi_lista}]</small></p>
        </section>
        <section>
          <h1>Contactos</h1>
          <div>
            <div class='group-input'>
              <div class="form-group">
                  <label htmlFor="name">Nombre: </label>
                  <input type="text" id="name"/>
              </div>
              <div class="form-group">
                  <label htmlFor="number">Número de Teléfono: </label>
                  <input type="text" id="number"/>
              </div>
              <button onClick={addContact}>Agregar Contacto</button>
            </div>
              
              
              <button onClick={updateContact}>Actualizar Contacto</button>
              <button onClick={deleteContact}>Eliminar Contacto</button>
              <button onClick={showContacts}>Mostrar Contactos</button>
          </div>

          <div id="contact-list" class="contact-list"></div>
        </section>
        
      </main>
    </div>
  );
}

export default App;
